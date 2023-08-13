# Coordinates

SVG Coordinate system is setup with the origin $(0,0)$ at the top-left corner with $x$ increasing to the right and $y$ down the page.  [SVG specifies](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Positions) two sets of units:

* User units that are nominally in pixels: one user unit equals one screen unit unless `viewBox` defines a zoom-in.
* Absolute units such as `pt` and `cm` are also permitted in most tags except `polyline` and `polygon` where they are explicitly in user units.

Because `Schediazo` is aimed at drawing in absolute units we must translate everything on save.  Our `schediazo.shapes.polyline` classes take positions in absolute units and then convert to user units (with an assumed DPI) on save.





If we don't specify a unit (e.g., if we receive a float or int type as a position or size) then the drawing will default to
the natural units of the drawing (

    polylines, polygons, paths don't have units so will need conversation on save.