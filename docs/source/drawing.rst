Drawing
=======

A `Schediazo` drawing is contained in a :py:class:`schediazo.drawing.Drawing` object to which various drawing objects, `parts`, are
added.  Each drawing item in Schediazo are subclasses of either :py:class:`schediazo.parts.PartBase` if they do not
contain other drawing items, or :py:class:`schediazo.parts.PartDict` if they do contain others (e.g., a group).

.. autoclass:: schediazo.drawing.Drawing
    :noindex:

Parts are added using the :py:class:`schediazo.drawing.Drawing.add` method.  Parts can be rearranged 
:py:class:`schediazo.drawing.Drawing.movetofront`, :py:class:`schediazo.drawing.Drawing.movetoback`,
:py:class:`schediazo.drawing.Drawing.moveforward`, and :py:class:`schediazo.drawing.Drawing.movebackward`
methods.  Saving the the drawing to an SVG file is with the :py:class:`schediazo.drawing.Drawing.save` method.


Styling
-------

There are two ways to set the stroke widths, fills, fonts, clipping and setting transforms.  CSS styling
can be directly specified via a `style` string or can be specified as CSS to :py:meth:`schediazo.Drawing.add_style`
and specifying that style with `cssclass`.  Alternatively, appropriate styling can be applied in the constructor
for each part.

Stroke
^^^^^^

The :py:class:`schediazo.attributes.Stroke` class provides all the stroke attributes as arguments
to constructors for parts that allow stroke settings.

.. autoclass:: schediazo.attributes.Stroke
    :noindex:

Line caps and line joins are specified using:

.. autoclass:: schediazo.attributes.LineCap
    :noindex:

.. autoclass:: schediazo.attributes.LineJoin
    :noindex:

Fill
^^^^

The :py:class:`schediazo.attributes.Fill` class provides all the fill attributes as arguments
to constructors for parts that allow fill settings.

.. autoclass:: schediazo.attributes.Fill
    :noindex:


Fonts and Text Rendering
^^^^^^^^^^^^^^^^^^^^^^^^

The :py:class:`schediazo.attributes.Font` class provides all the font selection attributes as arguments
to constructors for parts that allow font settings.

.. autoclass:: schediazo.attributes.Font
    :noindex:

The size of a font can be specified either directly with the size of the font in points or with an option from
:py:class:`schediazo.attributes.FontSize`

.. autoclass:: schediazo.attributes.FontSize
    :noindex:

Italic, oblique and bold settings are specified with options from the :py:class:`schediazo.attributes.FontStyle`
and :py:class:`schediazo.attributes.FontWeight` classes.

.. autoclass:: schediazo.attributes.FontStyle
    :noindex:

.. autoclass:: schediazo.attributes.FontWeight
    :noindex:

Font variants, such as all caps, or drop caps are specified with options from :py:class:`schediazo.attributes.FontVariant`

.. autoclass:: schediazo.attributes.FontVariant
    :noindex:

Horizontal stretching is specified with options from :py:class:`schediazo.attributes.FontStretch`

.. autoclass:: schediazo.attributes.FontStretch
    :noindex:


The text alignment is specified separately with the :py:class:`schediazo.attributes.TextRendering` class and specifying
either :py:attr:`schediazo.attributes.TextAnchor.Start`, :py:attr:`schediazo.attributes.TextAnchor.Middle` or :py:attr:`schediazo.attributes.TextAnchor.End`.

.. autoclass:: schediazo.attributes.TextRendering
    :noindex:

Clipping
^^^^^^^^

Specify clipping with :py:class:`schediazo.attributes.Clip` and setting the `clip_path` argument to the id of a 
:py:class:`schediazo.containers.ClipPath` part.

.. autoclass:: schediazo.attributes.Clip
    :noindex:

Transforms
^^^^^^^^^^

Transforms are covered more in another section of the documentation, but transforms for a part can be specified by
passing a :py:class:`schediazo.transforms.Affine` object in the `transform` argument supplied by the
:py:class:`schediazo.attributes.Transform` class.

.. autoclass:: schediazo.attributes.Transform
    :noindex:


Shapes
------

All the shape classes inherit from :py:class:`schediazo.parts.PartBase` which have an `id` attribute.  If these are not
set in a shape constructor then the id is generated randomly using a `uuid`.

Line
^^^^
The line class implements the `line <https://developer.mozilla.org/en-US/docs/Web/SVG/Element/line>`_ tag in
SVG.  The line class supports the :py:class:`schediazo.attributes.Stroke`, :py:class:`schediazo.attributes.Transform`,
:py:class:`schediazo.attributes.Clip`, and :py:class:`schediazo.attributes.Styling` attribute classes.

.. autoclass:: schediazo.shapes.Line
    :noindex:

Circle
^^^^^^
The circle class implements the `circle <https://developer.mozilla.org/en-US/docs/Web/SVG/Element/circle>`_ tag in
SVG.  The circle class supports the :py:class:`schediazo.attributes.Stroke`, :py:class:`schediazo.attributes.Transform`,
:py:class:`schediazo.attributes.Clip`, and :py:class:`schediazo.attributes.Styling` attribute classes.

.. autoclass:: schediazo.shapes.Circle
    :noindex:

Ellipse
^^^^^^^
The ellipse class implements the `ellipse <https://developer.mozilla.org/en-US/docs/Web/SVG/Element/ellipse>`_ tag in
SVG.  The ellipse class supports the :py:class:`schediazo.attributes.Stroke`, :py:class:`schediazo.attributes.Transform`,
:py:class:`schediazo.attributes.Clip`, and :py:class:`schediazo.attributes.Styling` attribute classes.

.. autoclass:: schediazo.shapes.Ellipse
    :noindex:

Rect
^^^^
The rect class implements the `rect <https://developer.mozilla.org/en-US/docs/Web/SVG/Element/rect>`_ tag in
SVG.  The rect class supports the :py:class:`schediazo.attributes.Stroke`, :py:class:`schediazo.attributes.Transform`,
:py:class:`schediazo.attributes.Clip`, and :py:class:`schediazo.attributes.Styling` attribute classes.

.. autoclass:: schediazo.shapes.Rect
    :noindex:

Polyline
^^^^^^^^
The polyline class implements the `polyline <https://developer.mozilla.org/en-US/docs/Web/SVG/Element/polyline>`_ tag in
SVG.  The polyline class supports the :py:class:`schediazo.attributes.Stroke`, :py:class:`schediazo.attributes.Transform`,
:py:class:`schediazo.attributes.Clip`, and :py:class:`schediazo.attributes.Styling` attribute classes.

.. autoclass:: schediazo.shapes.Polyline
    :noindex:

Polygon
^^^^^^^
The polygon class implements the `polygon <https://developer.mozilla.org/en-US/docs/Web/SVG/Element/polygon>`_ tag in
SVG.  The polygon class supports the :py:class:`schediazo.attributes.Stroke`, :py:class:`schediazo.attributes.Transform`,
:py:class:`schediazo.attributes.Clip`, and :py:class:`schediazo.attributes.Styling` attribute classes.

.. autoclass:: schediazo.shapes.Polygon
    :noindex:

EquilateralTriangle
^^^^^^^^^^^^^^^^^^^
The EquilateralTriangle class generates an equilaterial triangle via a `polygon <https://developer.mozilla.org/en-US/docs/Web/SVG/Element/polygon>`_ tag in
SVG.  The EquilateralTriangle class supports the :py:class:`schediazo.attributes.Stroke`, :py:class:`schediazo.attributes.Transform`,
:py:class:`schediazo.attributes.Clip`, and :py:class:`schediazo.attributes.Styling` attribute classes.

.. autoclass:: schediazo.shapes.EquilateralTriangle
    :noindex:


Paths
-----

More complicated shapes are generated using the :py:class:`schediazo.paths.Path` class which implements the
`path <https://developer.mozilla.org/en-US/docs/Web/SVG/Element/path>`_ tag in SVG.  The class supports the
:py:class:`schediazo.attributes.Stroke`, :py:class:`schediazo.attributes.Fill`, 
:py:class:`schediazo.attributes.Transform`, :py:class:`schediazo.attributes.Clip`, and
:py:class:`schediazo.attributes.Styling` attribute classes.

.. autoclass:: schediazo.paths.Path
    :noindex:

To specify the path we build a :py:class:`schediazo.paths.RawPath` object which is a list
to which we add various path commands.

.. autoclass:: schediazo.paths.RawPath
    :members: insert, append, extend, close
    :noindex:

The possible commands are:

Move
^^^^
.. autoclass:: schediazo.paths.MoveTo
    :noindex:

.. autoclass:: schediazo.paths.MoveToDelta
    :noindex:

Lines
^^^^^

.. autoclass:: schediazo.paths.LineTo
    :noindex:

.. autoclass:: schediazo.paths.LineToDelta
    :noindex:

.. autoclass:: schediazo.paths.PathLine
    :noindex:

.. autoclass:: schediazo.paths.HlineTo
    :noindex:

.. autoclass:: schediazo.paths.HlineToDelta
    :noindex:

.. autoclass:: schediazo.paths.Hline
    :noindex:

.. autoclass:: schediazo.paths.VlineTo
    :noindex:

.. autoclass:: schediazo.paths.VlineToDelta
    :noindex:

.. autoclass:: schediazo.paths.Vline
    :noindex:

Bezier curves
^^^^^^^^^^^^^

.. autoclass:: schediazo.paths.CubicBezierTo
    :noindex:

.. autoclass:: schediazo.paths.CubicBezierToDelta
    :noindex:

.. autoclass:: schediazo.paths.QuadraticBezierTo
    :noindex:

.. autoclass:: schediazo.paths.QuadraticBezierToDelta
    :noindex:



Text
----

The two text rendering classes inherit from :py:class:`schediazo.parts.PartBase` which have an `id` attribute.  If these are not
set in a text constructor then the id is generated randomly using a `uuid`.

Text
^^^^
The text class implements the `text <https://developer.mozilla.org/en-US/docs/Web/SVG/Element/text>`_ tag in
SVG.  The text class supports the :py:class:`schediazo.attributes.Stroke`, :py:class:`schediazo.attributes.Transform`,
:py:class:`schediazo.attributes.Clip`, and :py:class:`schediazo.attributes.Styling` attribute classes in common with
other shapes.  They also support the :py:class:`schediazo.attributes.Font` and :py:class:`schediazo.attributes.TextRendering`
attributes to control the font selection and text rendering options.

.. autoclass:: schediazo.text.Text
    :noindex:

TextPath
^^^^^^^^
The textpath class implements the `textpath <https://developer.mozilla.org/en-US/docs/Web/SVG/Element/textpath>`_ tag in
SVG.  The textpath class supports the :py:class:`schediazo.attributes.Stroke`, :py:class:`schediazo.attributes.Transform`,
:py:class:`schediazo.attributes.Clip`, and :py:class:`schediazo.attributes.Styling` attribute classes in common with
other shapes.  They also support the :py:class:`schediazo.attributes.Font` and :py:class:`schediazo.attributes.TextRendering`
attributes to control the font selection and text rendering options.

.. autoclass:: schediazo.text.TextPath
    :noindex:



Images
------

Images can be embedded using the Image class which implements the `image <https://developer.mozilla.org/en-US/docs/Web/SVG/Element/image>`_
tag in SVG.  The class supports the :py:class:`schediazo.attributes.Transform`, :py:class:`schediazo.attributes.Clip`, and
:py:class:`schediazo.attributes.Styling` attribute classes.

The image can either be supplied as a PIL.Image.Image object or a filename/URL to a resource where the image is located.  On
save the image will be embedded directly into the SVG but calling :py:meth:`schediazo.image.Image.save_image_and_generate_href`
will save the image to a file and then generate a URL.

.. autoclass:: schediazo.image.Image
    :members: save_image_and_generate_href
    :noindex:





Grouping
--------

Grouping shapes together is performed with the :py:class:`schediazo.containers.Group` which inherits
from :py:class:`schediazo.parts.PartDict` and has an `id` attribute.  If the id isn't set then the
id is randomly generated using a `uuid`.  The group can also be clipped using :py:class:`schediazo.attributes.Clip`.

Parts can be added using the :py:meth:`schediazo.containers.Group.add` method and can be deleted using the ``del`` operation
as normal for a Python container.  To preserve front-to-back rendering parts are added to the front by default but
can be rearranged arbitrarily.  Passing a part id to :py:meth:`schediazo.containers.Group.movetofront` or :py:meth:`schediazo.containers.Group.movetoback` 
will move the part to the front or back of the group.  Nudging a part towards the front or back relative to other
parts in the group can be achieved with :py:meth:`schediazo.containers.Group.moveforward` and :py:meth:`schediazo.containers.Group.movebackward`.
All the parts in a group can be removed using :py:meth:`schediazo.containers.Group.clear`.

.. autoclass:: schediazo.containers.Group
    :members: add, __iter__, __reversed__, clear, movetofront, movetoback, moveforward, movebackward
    :noindex:


Clipping
--------
To clip shapes or groups we use the :py:class:`schediazo.containers.ClipPath` class.  The id of this part must be known
as it is needed for the `clip_path` argument to the :py:class:`schediazo.attributes.Clip` constructor.

.. autoclass:: schediazo.containers.ClipPath
    :members: add, __iter__, __reversed__, clear, movetofront, movetoback, moveforward, movebackward
    :noindex:
