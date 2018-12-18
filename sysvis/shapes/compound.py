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
    def __init__(self, x: float, y: float, cell_or_groups: List[Shape], margin: Gap=None, padding: Gap=None, **kwargs):
        p = padding or Gap.zero()
        m = margin or Gap.zero()
        width = (
                m.left +
                p.left +
                max([c.width + c.margin.left + c.margin.right for c in cell_or_groups])
                + p.right
                + m.right
        )
        height = (
                m.top +
                p.top +
                reduce(lambda a, b: a + b.margin.top + b.height + b.margin.bottom, [c for c in cell_or_groups], 0)
                + p.bottom
                + m.bottom
        )
        super().__init__(x, y, width, height, margin=m, padding=p, **kwargs)
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
        gx, gy = self.gap.left, self.gap.top
        self.gap = Gap.gap2(gy + dh / (2 * len(self.cell_or_groups)), gx + dw / 2)
        return self

    def fit(self) -> 'Zone':
        p = self.padding
        g = self.gap
        x, y = self.x, self.y
        x += p.left + g.left
        y += p.right
        w = 0
        child_nodes: List[Shape] = []
        for c in self.cell_or_groups:
            y += g.top + c.margin.top
            moved = c.move(x + c.margin.left, y)
            if isinstance(moved, Zone) or isinstance(moved, Group):
                moved = moved.fit()
            child_nodes.append(moved)
            y += moved.height + g.bottom + c.margin.bottom
            w = max(c.margin.left + moved.width + c.margin.right, w)
        y += p.bottom
        x += w + g.right + p.right
        self.width = x - self.x
        self.height = y - self.y
        self.cell_or_groups = child_nodes
        return self


class Group(Compound):
    def __init__(self, x: float, y: float, cell_or_zones: List[Shape], margin: Gap=None, padding: Gap=None, **kwargs):
        p = padding or Gap.zero()
        m = margin or Gap.zero()
        width = (
                m.left +
                p.left +
                reduce(lambda a, b: a + b.margin.top + b.width + b.margin.bottom, [c for c in cell_or_zones], 0)
                + p.right
                + m.right
        )
        height = (
                m.top +
                p.top +
                max([c.height + c.margin.top + c.margin.bottom for c in cell_or_zones])
                + p.bottom
                + m.bottom
        )
        super().__init__(x, y, width, height, margin=m, padding=p, **kwargs)
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
        p = self.padding
        g = self.gap
        x, y = self.x, self.y
        y += p.top + g.top
        x += p.left
        h = 0
        child_nodes: List[Shape] = []
        for c in self.cell_or_zones:
            x += g.left + c.margin.left
            moved = c.move(x, y)
            if isinstance(moved, Zone) or isinstance(moved, Group):
                moved = moved.fit()
            child_nodes.append(moved)
            x += moved.width + g.right + c.margin.right
            h = max(moved.height, h)
        x += p.right
        y += h + g.bottom + p.bottom
        self.height = y - self.y
        self.width = x - self.x
        self.cell_or_zones = child_nodes
        return self
