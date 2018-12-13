import copy
import math

from sysvis.shapes.utils import Shape, SvgAttrs, _style, _move


class Person(Shape):
    def svg(self) -> str:
        shape = _person(self.x + self.width / 4, self.y, self.width / 2, self.height, self.svg_attrs)
        y0 = self.y - 32  # FIXME
        text_attrs = SvgAttrs({
            'text.text-anchor': 'middle',
            **self.svg_attrs
        })
        text = self.text.svg(self.cx, y0, text_attrs)
        return '<g {style}>{shape}{text}</g>'.format(style=_style(self.svg_attrs), shape=shape, text=text)

    def move(self, dx: float, dy: float) -> 'Person':
        return _move(self, dx, dy)


class Cylinder(Shape):
    def svg(self) -> str:
        x, y, cx, cy, w, h = self.x, self.y, self.cx, self.cy, self.width, self.height
        shape = _cylinder(cx, cy, w, h, self.svg_attrs)
        text = self.text.svg(x + self.padding.left, y + self.padding.top, self.svg_attrs)
        return '<g {style}>{shape}{text}</g>'.format(style=_style(self.svg_attrs), shape=shape, text=text)

    def move(self, dx, dy) -> Shape:
        return _move(self, dx, dy)


class Rect(Shape):
    def svg(self) -> str:
        x, y, cx, cy, w, h = self.x, self.y, self.cx, self.cy, self.width, self.height
        shape = _rect(cx, cy, w, h, self.svg_attrs)
        text = self.text.svg(x + self.padding.left, y + self.padding.top, self.svg_attrs)
        return '<g {style}>{shape}{text}</g>'.format(style=_style(self.svg_attrs), shape=shape, text=text)

    def move(self, dx, dy) -> 'Rect':
        return _move(self, dx, dy)


class Arrow(Shape):
    def __init__(self, x1: float, y1: float, x2: float, y2: float, **kwargs):
        x, y = min(x1, x2), min(y1, y2)
        width, height = abs(x1 - x2), abs(y1 - y2)
        super().__init__(x, y, width, height, **kwargs)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def svg(self) -> str:
        tx, ty = self.cx, self.cy
        x1, y1, x2, y2 = self.x1, self.y1, self.x2, self.y2
        shape = _arrow(x1, y1, x2, y2, self.svg_attrs)
        # text_kwargs = {'text-anchor': 'middle', **self.kwargs}
        text_kwargs = self.svg_attrs
        v = _Vector2d(x1, y1, x2, y2).normalize()
        if v.dy > 0:
            v = v.rotate(-90).multiple(20)
        else:
            v = v.rotate(90).multiple(20)
        text = self.text.svg(tx + v.dx, ty + v.dy, text_kwargs)
        return '<g {style}>{shape}{text}</g>'.format(style=_style(self.svg_attrs), shape=shape, text=text)

    def move(self, dx, dy) -> 'Arrow':
        moved = _move(self, dx, dy)
        moved.x1 += dx
        moved.x2 += dx
        moved.y1 += dy
        moved.y2 += dy
        return moved

    def populate(self, tail: Shape, head: Shape) -> 'Arrow':
        def cut(v: _Vector2d, box: Shape) -> _Vector2d:
            candidates = []
            if v.dx < 0:
                dx = v.x1 - box.cx + box.width / 2
                ratio = -dx / v.dx
                candidates.append(v.multiple(ratio))
            elif v.dx > 0:
                dx = box.cx - v.x1 + box.width / 2
                ratio = dx / v.dx
                candidates.append(v.multiple(ratio))
            if v.dy < 0:
                dy = v.y1 - box.cy + box.height / 2
                ratio = -dy / v.dy
                candidates.append(v.multiple(ratio))
            elif v.dy > 0:
                dy = box.cy - v.y1 + box.height / 2
                ratio = dy / v.dy
                candidates.append(v.multiple(ratio))

            if len(candidates) == 1:
                return candidates[0]
            elif len(candidates) == 2:
                a, b = candidates
                if a.length() < b.length():
                    return a
                else:
                    return b
            else:
                raise NotImplementedError

        x1, y1, x2, y2 = self.x1, self.y1, self.x2, self.y2
        vec = _Vector2d(x1, y1, x2, y2)
        tail_cut = cut(vec, tail)
        head_cut = cut(vec.reverse(), head)
        ret = copy.copy(self)
        ret.x1 = x1 + tail_cut.dx
        ret.y1 = y1 + tail_cut.dy
        ret.x2 = x2 + head_cut.dx
        ret.y2 = y2 + head_cut.dy
        return ret


def _person(x, y, width, height, kwargs):
    cx = x + width / 2
    xx = x + width
    yy = y + height
    cr = height // 5
    rx = cr
    ry = cr
    style = _style({
        'fill': 'none',
        'stroke': 'black',
        **kwargs
    })
    return """
    <path
    d="
    M{xa} {cy}
    A{rx} {ry} 0 1 0 {xb} {cy}
    A{rx} {ry} 0 1 0 {xa} {cy}
    M{cx},{y1}
    L{cx},{y3}
    M{x0},{y2}
    L{xx},{y2}
    M{cx},{y3}
    L{x0},{yy}
    M{cx},{y3}
    L{xx},{yy}
    "
    {style}
    />
    """.format(
        x0=x, y0=y,
        xx=xx, yy=yy,
        y1=y + cr * 2, y2=y + cr * 3, y3=cr * 4 + y,
        cx=cx, cy=y + cr,
        rx=rx, ry=ry,
        xa=(cx - rx), xb=(cx + rx),
        style=style
    )


def _cylinder(cx, cy, width, height, kwargs):
    curve = 8 + (width * 1.2) // 20  # FIXME
    xl = cx - (width // 2)
    xr = cx + (width // 2)
    yum = cy - (height // 2)
    yuu = yum - curve
    yud = yum + curve
    ydm = cy + (height // 2)
    ydd = ydm + curve
    style = _style({
        'fill': 'none',
        'stroke': 'black',
        **kwargs
    })
    return """
    <path
    d="
    M {xr},{yum}
    C {xr},{yud}
      {xl},{yud}
      {xl},{yum}
    M {xr},{yum}
    C {xr},{yuu}
      {xl},{yuu}
      {xl},{yum}
    M {xr},{yum}
    L {xr},{ydm}
    C {xr},{ydd}
      {xl},{ydd}
      {xl},{ydm}
    L {xl},{yum}
    "
    {style}
    />
    """.format(
        xl=xl,
        xr=xr,
        yuu=yuu,
        yum=yum,
        yud=yud,
        ydm=ydm,
        ydd=ydd,
        style=style
    )


def _rect(cx, cy, width, height, kwargs):
    x = cx - (width // 2)
    y = cy - (height // 2)
    style = _style({
        'fill': 'none',
        'stroke': 'black',
        **kwargs
    })
    return """
    <rect
    x="{x}"
    y="{y}"
    width="{width}"
    height="{height}"
    {style}
    />
    """.format(x=x, y=y, width=width, height=height, style=style)


def _arrow(x1, y1, x2, y2, kwargs):
    def rotate_base(deg, pump):
        v1 = _Vector2d(x1, y1, x2, y2).normalize().multiple(pump).rotate(deg).negate()
        return v1.move(x2, y2)

    va = rotate_base(27, 27)
    vb = rotate_base(-27, 27)
    style = _style({
        'stroke': 'black',
        'stroke-width': '3',
        **kwargs
    })
    return """
    <path d="
    M {x1} {y1}
    L {x2} {y2}
    M {xa} {ya}
    L {x2} {y2}
    M {xb} {yb}
    L {x2} {y2}
    " {style}></path>
    """.format(x1=x1, y1=y1, x2=x2, y2=y2, xa=va.x2, ya=va.y2, xb=vb.x2, yb=vb.y2, style=style)


class _Vector2d(object):
    # FIXME
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def rotate(self, degree):
        def deg2rad(deg):
            return deg * math.pi / 180

        x1, y1 = self.x1, self.y1
        th = deg2rad(degree)
        rotate = math.cos(th) + 1j * math.sin(th)
        rotated = (self.dx + self.dy * 1j) * rotate
        return _Vector2d(x1, y1, x1 + rotated.real, y1 + rotated.imag)

    def negate(self):
        x1, y1 = self.x1, self.y1
        return _Vector2d(x1, y1, x1 - self.dx, y1 - self.dy)

    def reverse(self):
        x1, y1, x2, y2 = self.x1, self.y1, self.x2, self.y2
        return _Vector2d(x2, y2, x1, y1)

    def move(self, dx, dy):
        x1, y1, x2, y2 = self.x1, self.y1, self.x2, self.y2
        return _Vector2d(x1 + dx, y1 + dy, x2 + dx, y2 + dy)

    def normalize(self):
        d = self.length()
        return _Vector2d(0, 0, self.dx / d, self.dy / d)

    def multiple(self, n):
        x1, y1 = self.x1, self.y1
        return _Vector2d(x1, y1, x1 + self.dx * n, y1 + self.dy * n)

    def length(self):
        return math.sqrt(self.dx ** 2 + self.dy ** 2)

    @property
    def dx(self) -> float:
        return self.x2 - self.x1

    @property
    def dy(self) -> float:
        return self.y2 - self.y1
