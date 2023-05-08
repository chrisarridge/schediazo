# Schediazo
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

`Schediazo` is a vector drawing package in Python which writes to `SVG` files.  There are other SVG writers/readers, for example [Orsinium-labs/svg.py](https://github.com/orsinium-labs/svg.py) but I already had my own SVG code and routines that did additional vector drawing tasks, for example to align drawing objects or to fit Bezier curves (not yet included) so this repo exists mainly for my own use.  I've also used it as an exercise in type hinting and multiple inheritance.

The word `Schediazo` is related to the Greek word for drawing.

## Features:
### Alignment
This package includes a 2D alignment facility that can align edges of parts via rotation and translation.  This is performed by solving Wahba's problem by finding (through gradient descent minimisation) the rotation that provides a consistent translation and then solving for the translation.

### Ordering of drawing parts
A specific facility that is used is that since `SVG` uses Painter's algorithm for drawing, we need to be able to order the elements in a drawing.  This package uses a re-implementation and extension of `OrderedDict` for all drawing parts that can contain other parts.  For example, an `SVG` group (`g`) tag can contain a set of renderable shapes and we want to be able to control this.  The `PartDict` base class is similar to an `OrderedDict` in that it is a dictionary that retains memory about the insertion order but this order can be manipulated at will.  Parts can be moved forwards, backwards, to the front, to the back arbitrarily, but still retrieved using a key as a standard dictionary.

## Installation
To install `schediazo` use pip.

``pip install .``

or to install in editable mode:

``pip install --editable .``
