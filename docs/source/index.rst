.. Schediazo documentation master file, created by
   sphinx-quickstart on Fri Aug  4 22:23:10 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Schediazo's documentation!
=====================================
Version |release|.

**Schediazo** is a vector drawing package in Python which writes to `SVG` files.  The word `Schediazo` is
related to the Greek word for drawing.

Features
--------
* Alignment of shapes by rotation and translation.
* Control over front-to-back ordering of shapes and drawing elements.

Why Schediazo?
--------------
There are other SVG writers/readers, for example [Orsinium-labs/svg.py](https://github.com/orsinium-labs/svg.py) but
I already had my own SVG code and routines that did additional vector drawing tasks, for example to align
drawing objects or to fit Bezier curves (not yet included) so this repo exists mainly for my own use.  I've also
used it as an exercise in type hinting and multiple inheritance.

Contributing
------------
Contributions to Schediazo are welcome.

Licence
-------
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.


Contents
========

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   getting-started
   drawing
   transforms
   alignment
   fullapi


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


   