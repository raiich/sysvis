from dataclasses import dataclass
from typing import Dict

from sysvis.shapes import Compound, Shape, ShapeAttrs


@dataclass
class Field:
    arranged: Compound
    width: float
    height: float
    parent_dict: Dict[str, Compound]
    lookup: Dict[str, Shape]

    @staticmethod
    def of(arranged: Compound):
        height = arranged.height
        width = arranged.width
        parent_dict = {}
        lookup = {}

        def flatten(a: Compound):
            for c in a.child_nodes:
                lookup[c.id] = c
                parent_dict[c.id] = a
                if isinstance(c, Compound):
                    flatten(c)
        flatten(arranged)
        return Field(arranged, width, height, parent_dict, lookup)

    def find(self, sid) -> Shape:
        return self.lookup.get(sid)

    def add(self, child: Shape) -> 'Field':
        # FIXME
        self.lookup[child.id] = child
        self.parent_dict[child.id] = self.arranged
        self.arranged.child_nodes.append(child)
        return self

    def delete(self, aid: str) -> 'Field':
        c = self.lookup.get(aid)
        p = self.parent_dict.get(aid)
        if p is None or c is None:
            raise ValueError('not found {0}'.format(aid))
        p.child_nodes.remove(c)
        del self.parent_dict[aid]
        del self.lookup[aid]
        return self

    def update(self, attrs: ShapeAttrs) -> 'Field':
        self.arranged.update(**attrs)
        return self

    def svg(self) -> str:
        return self.arranged.svg()
