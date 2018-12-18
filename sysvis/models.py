import copy
from dataclasses import dataclass
from typing import List, Dict, NewType, Union

from sysvis.field import Field
from sysvis.shapes import (
    Text, Rect, Cylinder, Person, Group as GroupShape, Arrow, Zone as ZoneShape, Shape, Gap, ShapeAttrs
)

ModelAttrs = NewType('ModelAttrs', dict)


# FIXME
class AttributeMap(object):
    def __init__(self, attr_map: Dict[str, dict]):
        self.map = attr_map

    def shape_attrs(self, model: object) -> ShapeAttrs:
        key = type(model).__name__.lower()
        return ShapeAttrs(self.map.get(key, {}))

    def model_attrs(self, model: object) -> ModelAttrs:
        key = type(model).__name__.lower()
        return ModelAttrs(self.map.get(key, {}))

    def update(self, others: 'AttributeMap') -> 'AttributeMap':
        dic = {**self.map}
        for k, v in others.map.items():
            base = dic.get(k)
            if base is not None:
                dic[k] = {
                    **base,
                    **v
                }
            else:
                dic[k] = v
        return AttributeMap(dic)


# FIXME
class UpdateModel(object):
    def update(self, base: Field, attrs: AttributeMap) -> Field:
        raise NotImplementedError


# FIXME
class ShapeModel(object):
    def shape(self, attrs: AttributeMap) -> Shape:
        raise NotImplementedError


class Group(ShapeModel):
    def __init__(self, gid: str, setups: List[ShapeModel], attrs: AttributeMap, label: str=None,
                 margin: str=None, padding: str=None, **kwargs):
        self._id = gid
        self.setups = setups
        self.attributes = attrs
        self.text = Text(label=label)
        self.margin = Gap.parse(margin)
        self.padding = Gap.parse(padding)
        self.shape_attrs = ShapeAttrs(kwargs)

    @property
    def id(self) -> str:
        return self._id

    def shape(self, attrs: AttributeMap) -> GroupShape:
        a_map = attrs.update(self.attributes)
        children = [m.shape(a_map) for m in self.setups]
        a = a_map.shape_attrs(self)
        m = self.margin or Gap.parse(a.get('margin')) or Gap.gap2(100.0, 20.0)
        p = self.padding or Gap.parse(a.get('padding')) or Gap.gap2(20.0, 16.0)
        return (
            GroupShape(0, 0, children, margin=m, padding=p, sid=self._id)
            .update(**a_map.shape_attrs(self))
            .update(text=self.text, **self.shape_attrs)
        )


class Zone(ShapeModel):
    def __init__(self, zid: str, setups: List[ShapeModel], attrs: AttributeMap, label: str=None,
                 margin: str=None, padding: str=None, **kwargs):
        self._id = zid
        self.setups = setups
        self.attributes = attrs
        self.text = Text(label=label)
        self.shape_attrs = ShapeAttrs(kwargs)
        self.margin = Gap.parse(margin)
        self.padding = Gap.parse(padding)

    @property
    def id(self) -> str:
        return self._id

    def shape(self, attrs: AttributeMap) -> ZoneShape:
        a_map = attrs.update(self.attributes)
        children = [m.shape(a_map) for m in self.setups]
        a = a_map.shape_attrs(self)
        m = self.margin or Gap.parse(a.get('margin')) or Gap.gap2(20.0, 150.0)
        p = self.padding or Gap.parse(a.get('padding')) or Gap.gap2(20.0, 16.0)
        return (
            ZoneShape(0, 0, children, margin=m, padding=p, sid=self._id)
            .update(**a_map.shape_attrs(self))
            .update(text=self.text, **self.shape_attrs)
        )


class Node(ShapeModel, UpdateModel):
    def __init__(self, node_id: str, label: str=None, t: str=None, shape: str=None, width: str=None, height: str=None,
                 margin: str=None, padding: str=None, **kwargs):
        self._id = node_id
        self.text = Text(label, t)
        self._shape = shape
        self.width = width
        self.height = height
        self.margin = Gap.parse(margin)
        self.padding = Gap.parse(padding)
        self.shape_attrs = ShapeAttrs(kwargs)

    @property
    def id(self) -> str:
        return self._id

    def shape(self, attrs: AttributeMap) -> Shape:
        a = attrs.shape_attrs(self)
        shape = self._shape or attrs.model_attrs(self).get('shape', 'box')
        w = int(self.width or a.get('width') or 200)  # FIXME
        h = int(self.height or a.get('height') or 150)  # FIXME

        m = self.margin or Gap.parse(a.get('margin')) or Gap.gap2(20.0, 20.0)
        p = self.padding or Gap.parse(a.get('padding')) or Gap.gap2(20.0, 16.0)
        ret = Rect(0, 0, w, h, self._id, margin=m, padding=p)

        if shape == 'box':
            pass
        elif shape == 'cylinder':
            ret = Cylinder(0, 0, w, h, self._id)
        elif shape == 'person':
            ret = Person(0, 0, w, h, self._id)
        else:
            raise NotImplementedError('shape: ' + shape)

        label = self.text.label or attrs.model_attrs(self).get('label')
        if label is None:
            label = self._id

        text = Text(label, self.text.content)
        a = {k: v for k, v in a.items() if k != 'width' and k != 'height'}  # FIXME
        return (
                ret
                .update(**a)
                .update(text=text, margin=m, padding=p, **self.shape_attrs)
        )

    def update(self, base: Field, attrs: AttributeMap) -> Field:
        shape = base.find(self._id)
        shape.visible()
        shape.update(self.text, **attrs.shape_attrs(self))
        return base


def _edge_id(tail_id, head_id):
    return 'edge_' + tail_id + '_to_' + head_id


class Edge(UpdateModel):
    def __init__(self, tail_id, op, head_id, t=None, dx=None, dy=None, **kwargs):
        self.tail_id = tail_id
        self.head_id = head_id
        self.op = 'tail -> head' if op == '->' else None
        self.text = Text(content=t)
        self.dx = float(dx or 0)
        self.dy = float(dy or 0)
        self.shape_attrs = ShapeAttrs(kwargs)
        self._id = _edge_id(tail_id, head_id)

    @property
    def id(self) -> str:
        return self._id

    def update(self, base: Field, attrs: AttributeMap) -> Field:
        head, tail = base.find(self.head_id).visible(), base.find(self.tail_id).visible()
        arrow = (
            Arrow(tail.cx, tail.cy, head.cx, head.cy, sid=self.id, text=self.text)
            .move(self.dx, self.dy)
            .visible()
            .populate(tail, head)
            .update(**attrs.shape_attrs(self))
            .update(**self.shape_attrs)
        )
        base.add(arrow)
        return base


class DeleteMob(UpdateModel):
    def __init__(self, sid: str):
        self._id = sid

    @property
    def id(self) -> str:
        return self._id

    def update(self, base: Field, attrs: AttributeMap) -> Field:
        return base.delete(self._id)


class DeleteEdge(UpdateModel):
    def __init__(self, tail_id, head_id):
        self._id = _edge_id(tail_id, head_id)

    @property
    def id(self) -> str:
        return self._id

    def update(self, base: Field, attrs: AttributeMap) -> Field:
        return base.delete(self._id)


@dataclass
class Assignment:
    key: str
    value: str


class Attribute(object):
    def __init__(self, element, **kwargs):
        self.element = element
        self.attrs = ModelAttrs(kwargs)


class StatementList(object):
    def __init__(self, setups: List[ShapeModel], attrs: AttributeMap, assignments: List[Assignment]):
        self.setups = setups
        self.attributes = attrs
        self.assignments = {a.key: a.value for a in assignments}

    @staticmethod
    def of(statements: List[any]) -> 'StatementList':
        setups = []
        attributes = []
        assignments = []
        for s in statements:
            if isinstance(s, Node) or isinstance(s, Group) or isinstance(s, Zone):
                setups.append(s)
            elif isinstance(s, Edge):
                setups.append(s)
            elif isinstance(s, DeleteMob) or isinstance(s, DeleteEdge):
                setups.append(s)
            elif isinstance(s, Attribute):
                attributes.append(s)
            elif isinstance(s, Assignment):
                assignments.append(s)
            else:
                raise ValueError(s)
        attrs = AttributeMap({s.element: s.attrs for s in attributes})
        return StatementList(setups, attrs, assignments)


class Moment(object):
    def __init__(self, setups: List[Union[ShapeModel, UpdateModel]], attrs: AttributeMap, config='',
                 padding: str=None, margin: str=None, **kwargs):
        def assign(eq: str):
            k, v = eq.split('=')
            return k.strip(), v.strip()

        self.config = {k: v for k, v in map(assign, filter(lambda x: x, config.split(',')))}
        self.centering = self.config.get('align', None) == 'center'
        self.setups = setups
        self.attributes = attrs
        self.shape_attrs = ShapeAttrs(kwargs)
        self.margin = Gap.parse(margin) if margin else None
        self.padding = Gap.parse(padding) if padding else None

    def field(self) -> Field:
        # FIXME
        children = [m.shape(self.attributes) for m in self.setups if isinstance(m, ShapeModel)]
        # FIXME
        max_width = max(map(lambda cc: _width(cc), children))
        for c in children:
            if self.centering and (isinstance(c, ZoneShape) or isinstance(c, GroupShape)):
                # FIXME
                c.expand_to(max_width, c.height)
        field = Field.of(
            ZoneShape(0, 0, children, margins=self.margin, padding=self.padding)
            .update(**self.shape_attrs)
            .fit()
        )
        for edge in self.setups:
            if isinstance(edge, Edge):
                # FIXME
                field = edge.update(field, self.attributes)
        return field

    def update(self, base: Field, attrs: AttributeMap) -> Field:
        for m in self.setups:
            m.update(base, attrs).update(self.attributes.shape_attrs(m))

        for _ in self.shape_attrs:
            raise NotImplementedError

        return base


class Story(object):
    def __init__(self, moments: List[Moment]):
        init = moments[0]
        self.init = init
        self.diff_mode = False
        self.diff_mode = init.config.get('mode') == 'diff'
        self.updates = moments[1:]

    def play(self, outfile):
        field = self.init.field()
        n = 0
        self._write(field.width, field.height, field.svg(), outfile + '.{:04}.svg'.format(n))
        for update in self.updates:
            n += 1
            updated = update.update(copy.deepcopy(field), self.init.attributes)
            self._write(updated.width, updated.height, updated.svg(), outfile + '.{:04}.svg'.format(n))
            if self.diff_mode:
                field = updated

    @staticmethod
    def _write(width, height, svg, outfile):
        ret = """<?xml version="1.0" encoding="UTF-8"?>
        <svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">{body}</svg>
        """.format(
            width=width,
            height=height,
            body=svg
        )
        with open(outfile, 'w') as f:
            f.write(ret)


def _width(shape: Shape) -> float:
    return shape.margin.left + shape.width + shape.margin.right


def _height(shape: Shape) -> float:
    return shape.margin.top + shape.height + shape.margin.bottom

