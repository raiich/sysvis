from abc import ABC
from functools import reduce
from typing import List

from sysvis.shapes.utils import _style, _move, Shape, Gap


class Compound(Shape, ABC):
    @property
    def child_nodes(self) -> List[Shape]:
        raise NotImplementedError

    def svg(self) -> str:
        ret = '<g {style}>'.format(style=_style(self.svg_attrs))
        for s in self.child_nodes:
            ret += s.svg()
        ret += '</g>'
        return ret

    def expand_to(self, width: float, height: float) -> 'Compound':
        raise NotImplementedError

    def find(self, sid: str) -> List[Shape]:
        ret = []
        for c in self.child_nodes:
            if c.id == sid:
                ret.append(c)
            if isinstance(c, Compound):
                ret.extend(c.find(sid))
        return ret

    def add(self, child: Shape) -> 'Compound':
        self.child_nodes.append(child)
        return self

    def delete(self, sid: str) -> 'Compound':
        target = []
        for c in self.child_nodes:
            if c.id == sid:
                target.append(c)
        for t in target:
            self.child_nodes.remove(t)
        for c in self.child_nodes:
            if isinstance(c, Compound):
                c.delete(sid)
        return self


class Zone(Compound):
    def __init__(self, x: float, y: float, cell_or_groups: List[Shape], **kwargs):
        width = max([c.width + c.margin.left + c.margin.bottom for c in cell_or_groups])
        height = reduce(lambda a, b: a + b.height + b.margin.top + b.margin.bottom, [c for c in cell_or_groups], 0)
        super().__init__(x, y, width, height, **kwargs)
        self.cell_or_groups = cell_or_groups
        self.gap = Gap.gap2(0, 0)

    @property
    def child_nodes(self) -> List[Shape]:
        return self.cell_or_groups

    def move(self, dx, dy) -> 'Zone':
        return _move(self, dx, dy)

    def expand_to(self, width: float, height: float) -> 'Zone':
        dw = width - self.width
        dh = height - self.height
        pad_x, pad_y = self.gap.left, self.gap.top
        self.gap = Gap.gap2(pad_y + dh / (2 * len(self.cell_or_groups)), pad_x + dw / 2)
        return self

    def fit(self) -> 'Zone':
        x, y = self.x, self.y
        pad_x, pad_y = self.gap.left, self.gap.top
        x += pad_x
        w = 0
        child_nodes: List[Shape] = []
        for c in self.cell_or_groups:
            y += pad_y + c.margin.top
            moved = c.move(x, y)
            if isinstance(moved, Zone) or isinstance(moved, Group):
                moved = moved.fit()
            child_nodes.append(moved)
            y += moved.height + pad_y + c.margin.bottom
            w = max(moved.width, w)
        h = y - self.y
        w = w + pad_x * 2
        self.width = w
        self.height = h
        self.cell_or_groups = child_nodes
        return self


class Group(Compound):
    def __init__(self, x: float, y: float, cell_or_zones: List[Shape], **kwargs):
        width = reduce(lambda a, b: a + b.width + b.margin.left + b.margin.right, [c for c in cell_or_zones], 0)
        height = max([c.height + c.margin.top + c.margin.bottom for c in cell_or_zones])
        super().__init__(x, y, width, height, **kwargs)
        self.cell_or_zones = cell_or_zones
        self.gap = Gap.gap2(0, 0)

    @property
    def child_nodes(self) -> List[Shape]:
        return self.cell_or_zones

    def move(self, dx: float, dy: float) -> 'Group':
        return _move(self, dx, dy)

    def expand_to(self, width: float, height: float) -> 'Group':
        dw = width - self.width
        dh = height - self.height
        pad_x, pad_y = self.gap.left, self.gap.top
        self.gap = Gap.gap2(pad_y + dh / 2, pad_x + dw / (2 * len(self.cell_or_zones)))
        return self

    def fit(self) -> 'Group':
        x, y = self.x, self.y
        pad_x, pad_y = self.gap.left, self.gap.top
        y += pad_y
        h = 0
        child_nodes: List[Shape] = []
        for c in self.cell_or_zones:
            x += pad_x + c.margin.left
            moved = c.move(x, y)
            if isinstance(moved, Zone) or isinstance(moved, Group):
                moved = moved.fit()
            child_nodes.append(moved)
            x += moved.width + pad_x + c.margin.right
            h = max(moved.height, h)
        w = x - self.x
        h = h + 2 * pad_y
        self.width = w
        self.height = h
        self.cell_or_zones = child_nodes
        return self
