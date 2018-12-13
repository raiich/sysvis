# sysvis

## Dependencies

- Python 3.7
- Pipenv

## Install

### Install Dependencies

#### Python 3.7 & Pipenv

```sh
$ sudo mkdir /usr/local/Frameworks
$ sudo chown $(whoami) /usr/local/Frameworks
$ brew install python
$ brew unlink python
$ brew link python
$ brew install pipenv
```

### Editable install

```sh
$ pipenv install -e .
```

## Execute

```sh
$ pipenv shell
$ sysvis -i examples/oauth2-authorization-code-grant.sysvis -o /tmp/oauth2-authorization-code-grant
$ open /tmp/oauth2-authorization-code-grant*
```

## Development

### ANTLR

Parser/Lexer code is generated using ANTLR. ANTLR is available with the following in macOS:

```sh
brew install antlr
```

Generating parser:
```sh
antlr4 -o sysvis/generated/ -Dlanguage=Python3 -visitor -no-listener Sysvis.g4
```
