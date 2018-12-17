from dataclasses import dataclass

from sysvis.shapes import Compound, Shape, ShapeAttrs


@dataclass
class Field:
    arranged: Compound
    width: float
    height: float

    @staticmethod
    def of(arranged: Compound):
        height = arranged.height
        width = arranged.width
        return Field(arranged, width, height)

    def find(self, sid) -> Shape:
        return self.arranged.find(sid)[0]

    def add(self, child: Shape) -> 'Field':
        return Field.of(self.arranged.add(child))

    def delete(self, aid: str) -> 'Field':
        return Field.of(self.arranged.delete(aid))

    def update(self, attrs: ShapeAttrs) -> 'Field':
        self.arranged.update(**attrs)
        return self

    def svg(self) -> str:
        return self.arranged.svg()
