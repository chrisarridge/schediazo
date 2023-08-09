Full API
========

Shapes
------

.. autoclass:: schediazo.shapes.Line
    :members:
    :inherited-members:

.. autoclass:: schediazo.shapes.Circle
    :members:
    :inherited-members:

.. autoclass:: schediazo.shapes.Ellipse
    :members:
    :inherited-members:

.. autoclass:: schediazo.shapes.Rect
    :members:
    :inherited-members:

.. autoclass:: schediazo.shapes.Polyline
    :members:
    :inherited-members:

.. autoclass:: schediazo.shapes.Polygon
    :members:
    :inherited-members:

.. autoclass:: schediazo.shapes.EquilateralTriangle
    :members:
    :inherited-members:


Paths
-----

.. autoclass:: schediazo.paths.Path
    :members:
    :inherited-members:

.. autoclass:: schediazo.paths.RawPath
    :members:
    :inherited-members:

RawPath Commands: Moving the pointer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: schediazo.paths.MoveTo
    :members:

.. autoclass:: schediazo.paths.MoveToDelta
    :members:

RawPath Commands: Drawing lines
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: schediazo.paths.LineTo
    :members:

.. autoclass:: schediazo.paths.LineToDelta
    :members:

.. autoclass:: schediazo.paths.PathLine
    :members:

.. autoclass:: schediazo.paths.HlineTo
    :members:

.. autoclass:: schediazo.paths.HlineToDelta
    :members:

.. autoclass:: schediazo.paths.Hline
    :members:

.. autoclass:: schediazo.paths.VlineTo
    :members:

.. autoclass:: schediazo.paths.VlineToDelta
    :members:

.. autoclass:: schediazo.paths.Vline
    :members:

RawPath Commands: Bezier curves
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: schediazo.paths.CubicBezierTo
    :members:

.. autoclass:: schediazo.paths.CubicBezierToDelta
    :members:

.. autoclass:: schediazo.paths.QuadraticBezierTo
    :members:

.. autoclass:: schediazo.paths.QuadraticBezierToDelta
    :members:

Images
------

.. autoclass:: schediazo.image.Image


Attributes
----------
.. autoclass:: schediazo.attributes.AttributeBase

.. autoclass:: schediazo.attributes.Styling

.. autoclass:: schediazo.attributes.Transform

.. autoclass:: schediazo.attributes.Clip

Fill and Stroke attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: schediazo.attributes.Fill

.. autoclass:: schediazo.attributes.Stroke

.. autoclass:: schediazo.attributes.LineCap

.. autoclass:: schediazo.attributes.LineJoin

Font and Text Rendering
^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: schediazo.attributes.Font

.. autoclass:: schediazo.attributes.FontStyle

.. autoclass:: schediazo.attributes.FontVariant

.. autoclass:: schediazo.attributes.FontStretch

.. autoclass:: schediazo.attributes.FontWeight

.. autoclass:: schediazo.attributes.FontSize

.. autoclass:: schediazo.attributes.TextAnchor

.. autoclass:: schediazo.attributes.TextRendering



Parts
-----
.. autoclass:: schediazo.part.PartBase

.. autoclass:: schediazo.part.PartDict


Containers
----------

.. autoclass:: schediazo.containers.Group
    :members: add, __iter__, __reversed__, clear, movetofront, movetoback, moveforward, movebackward

.. autoclass:: schediazo.containers.ClipPath
    :members: add, __iter__, __reversed__, clear, movetofront, movetoback, moveforward, movebackward



Drawing
-------

.. autoclass:: schediazo.drawing.Drawing
    :members:

.. autoclass:: schediazo.drawing.Definitions
    :members:

.. autoclass:: schediazo.svg.Versions
    :members:


Align
-----

.. autofunction:: schediazo.align.two_point_align
