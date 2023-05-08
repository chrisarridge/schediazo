import schediazo as sc

d = sc.Drawing()

d.add(sc.Rect(0,0,50,50, stroke='black', stroke_width=1, fill='red', id='rectangle'))
d.add(sc.Circle(100, 25, 25, stroke='black', stroke_width=1, fill='yellow', id='circle'))
d.add(sc.Ellipse(175, 25, 50, 25, stroke='black', stroke_width=1, fill='green', id='ellipse'))
d.add(sc.Rect(0,100,50,50, rx=10, ry=10, stroke='black', stroke_width=1, fill='orange', id='rounded-rectangle'))
d.add(sc.EquilateralTriangle(100, 100, 50, stroke='black', stroke_width=1, fill='red'))
d.add(sc.Polyline([200,250,300,250,200],[100,100,125,150,150], stroke='black', fill='orange'))
d.add(sc.Polygon([200,250,300,250,200],[200,200,225,250,250], stroke='black', fill='yellow'))

d.save('example_shapes')
