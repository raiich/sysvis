import copy
from dataclasses import dataclass
from typing import NewType, Optional

ShapeAttrs = NewType('ShapeAttrs', dict)
SvgAttrs = NewType('SvgAttrs', dict)


@dataclass(frozen=True)
class Gap:
    top: float
    right: float
    bottom: float
    left: float

    @staticmethod
    def zero() -> 'Gap':
        return Gap.gap1(0)

    @staticmethod
    def parse(string: str) -> Optional['Gap']:
        if not string:
            return None

        g = list(map(int, string.split(' ')))
        if len(g) == 4:
            return Gap.gap4(g[0], g[1], g[2], g[3])
        elif len(g) == 2:
            return Gap.gap2(g[0], g[1])
        elif len(g) == 1:
            return Gap.gap1(g[0])
        else:
            raise ValueError(string)

    @staticmethod
    def gap1(gap) -> 'Gap':
        return Gap(gap, gap, gap, gap)

    @staticmethod
    def gap2(tb, rl) -> 'Gap':
        return Gap(tb, rl, tb, rl)

    @staticmethod
    def gap4(top, right, bottom, left) -> 'Gap':
        return Gap(top, right, bottom, left)

    def add_x(self, rl) -> 'Gap':
        return Gap(self.top, self.right + rl, self.bottom, self.left + rl)

    def add_y(self, tb) -> 'Gap':
        return Gap(self.top + tb, self.right, self.bottom + tb, self.left)


@dataclass
class Text:
    label: str = None
    content: str = None

    @staticmethod
    def empty():
        return Text('', '')

    def update(self, other: 'Text') -> 'Text':
        if other:
            return Text(other.label or self.label, other.content or self.content)
        else:
            return self

    def svg(self, x: float, y: float, attrs: SvgAttrs) -> str:
        label, content = self.label, self.content
        if label:
            if content is None:
                text = label
            else:
                text = label + '\\n' + content
        else:
            if content is None:
                return ''
            else:
                text = content
        return _text(x, y, text, attrs)


class Shape:
    def __init__(self, x: float, y: float, width: float, height: float, sid: str=None,
                 text: Text=None, margin: Gap=None, padding: Gap=None, **kwargs):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        prefix = self.__class__.__name__
        self._id = sid or '{prefix}-{x}-{y}-{w}-{h}'.format(prefix=prefix, x=x, y=y, w=width, h=height)
        self.text = text or Text.empty()
        self.margin = margin or Gap.zero()
        self.padding = padding or Gap.zero()
        self.attrs = SvgAttrs(kwargs)

    @property
    def kwargs(self) -> dict:
        return {
            'sid': self._id,
            'text': self.text,
            'margin': self.margin,
            'padding': self.padding,
            **self.attrs
        }

    @property
    def id(self) -> str:
        return self._id

    @property
    def svg_attrs(self) -> SvgAttrs:
        return self.attrs or SvgAttrs({})

    @property
    def cx(self) -> float:
        return self.x + self.width / 2

    @property
    def cy(self) -> float:
        return self.y + self.height / 2

    def svg(self) -> str:
        raise NotImplementedError

    def move(self, dx: float, dy: float) -> 'Shape':
        raise NotImplementedError

    def update(self, text: Text=None, margin: Gap=None, padding: Gap=None, **kwargs) -> 'Shape':
        self.text = self.text.update(text)
        self.margin = margin or self.margin
        self.padding = padding or self.padding
        self.attrs = SvgAttrs({
            **self.attrs,
            **kwargs
        })
        return self

    def visible(self, is_visible: bool = True) -> 'Shape':
        # FIXME
        if self.attrs.get('visibility') is None:
            if is_visible:
                self.attrs['visibility'] = 'visible'
            else:
                self.attrs['visibility'] = 'hidden'
        return self


def _style(kwargs: dict) -> str:
    kwargs = {
        'stroke-width': 5,
        **kwargs
    }
    return ' '.join(['{k}="{v}"'.format(k=k, v=v) for k, v in kwargs.items()])


def _move(obj, dx, dy):
    moved = copy.copy(obj)
    moved.x += dx
    moved.y += dy
    return moved


def _text(x, y, text, kwargs):
    if not text:
        return ''

    text_id = 'text' + kwargs.get('id', str(hash(text)))
    kwargs = copy.copy(kwargs)
    kwargs = {k[len('text.'):]: v for k, v in filter(lambda a: a[0].startswith('text.'), kwargs.items())}
    kwargs['id'] = text_id
    kwargs['fill'] = kwargs.get('fill') or 'black'
    kwargs['stroke-width'] = '1'
    style = ' '.join(['{k}="{v}"'.format(k=k, v=v) for k, v in kwargs.items()])
    text = ''.join(map(
        lambda t: '<tspan x="{x}" dy="1em" {style}>{text}</tspan>'.format(x=x, text=t, style=style),
        text.split('\\n')))
    return """
    <text
    x="{x}"
    y="{y}"
    {style}
    >{text}</text>
    """.format(x=x, y=y, style=style, text=text)
