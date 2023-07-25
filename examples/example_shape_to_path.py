"""Demonstrate converting built-in shapes to paths"""
import schediazo as sc

d = sc.Drawing()

# All the shapes we will add.
shapes = [sc.Rect(0,0,50,50, stroke='red', stroke_width=3, fill_opacity=0.0, id='rectangle'),
    sc.Circle(100, 25, 25, stroke='red', stroke_width=3, fill_opacity=0.0, id='circle'),
    sc.Ellipse(175, 25, 50, 25, stroke='red', stroke_width=3, fill_opacity=0.0, id='ellipse'),
    sc.Rect(0,100,50,50, rx=10, ry=10, stroke='red', stroke_width=3, fill_opacity=0.0, id='rounded-rectangle'),
    sc.EquilateralTriangle(100, 100, 50, stroke='red', stroke_width=3, fill_opacity=0.0, id='equilateral-triangle'),
    sc.Polyline([200,250,300,250,200],[100,100,125,150,150], stroke='red', stroke_width=3, fill_opacity=0.0, id='polyline'),
    sc.Polygon([200,250,300,250,200],[200,200,225,250,250], stroke='red', stroke_width=3, fill_opacity=0.0, id='polygon'),
    sc.Line(0,400, 200, 400, stroke='red', stroke_width=3, fill_opacity=0.0, id='line')]

# Add the shapes, and their path versions, to the drawing.
for s in shapes:
    d.add(s)
    d.add(sc.Path(s.to_path(), stroke='black', stroke_width=1, fill_opacity=0.0, id=s.id+'-as-path'))

d.save('example_shapes_to_path')
