"""Demonstrate converting built-in shapes to paths"""
import schediazo as sc

d = sc.Drawing(width=200*sc.mm, height=450*sc.mm)

col1 = 50*sc.mm
col2 = 150*sc.mm
row1 = 50*sc.mm
row2 = 150*sc.mm
row3 = 250*sc.mm
row4 = 350*sc.mm

# All the shapes we will add.
shapes = [sc.Rect(col1-25*sc.mm, row1-25*sc.mm, 50*sc.mm, 50*sc.mm, stroke="black", stroke_width=1*sc.pt, fill="red", id="rectangle"),
            sc.Rect(col2-25*sc.mm, row1-25*sc.mm, 50*sc.mm, 50*sc.mm, rx=5*sc.mm, ry=5*sc.mm, stroke="black", stroke_width=1*sc.pt, fill="orange", id="rounded-rectangle"),
            sc.Circle(col1, row2, 25*sc.mm, stroke="black", stroke_width=1*sc.pt, fill="yellow", id="circle"),
            sc.Ellipse(col2, row2, 25*sc.mm, 12.5*sc.mm, stroke="black", fill="green", stroke_width=1*sc.pt, id="ellipse"),
            sc.Polygon([col1-25*sc.mm,col1,col1+25*sc.mm,col1,col1-25*sc.mm],[row3-25*sc.mm,row3-25*sc.mm,row3,row3+25*sc.mm,row3+25*sc.mm], stroke='black', stroke_width=1*sc.pt, fill='yellow'),
            sc.Polyline([col2-25*sc.mm,col2,col2+25*sc.mm,col2,col2-25*sc.mm],[row3-25*sc.mm,row3-25*sc.mm,row3,row3+25*sc.mm,row3+25*sc.mm], stroke='black', stroke_width=1*sc.pt, fill='orange'),
            sc.EquilateralTriangle(col1, row4, 50*sc.mm, stroke="black", stroke_width=1*sc.pt, fill="red")]

# Add the shapes, and their path versions, to the drawing.
for s in shapes:
    d.add(s)
    d.add(sc.Path(s.to_path(), stroke='black', stroke_width=4*sc.pt, id=s.id+'-as-path'))

d.save('example_shapes_to_path')
