import schediazo as sc

d = sc.Drawing(width=200*sc.mm, height=450*sc.mm)

col1 = 50*sc.mm
col2 = 150*sc.mm
row1 = 50*sc.mm
row2 = 150*sc.mm
row3 = 250*sc.mm
row4 = 350*sc.mm

d.add(sc.Rect(col1-25*sc.mm, row1-25*sc.mm, 50*sc.mm, 50*sc.mm, stroke="black", stroke_width=1*sc.mm, fill="red", id="rectangle"))
d.add(sc.Rect(col2-25*sc.mm, row1-25*sc.mm, 50*sc.mm, 50*sc.mm, rx=5*sc.mm, ry=5*sc.mm, stroke="black", stroke_width=1*sc.mm, fill="orange", id="rounded-rectangle"))
d.add(sc.Circle(col1, row2, 25*sc.mm, stroke="black", stroke_width=1*sc.mm, fill="yellow", id="circle"))
d.add(sc.Ellipse(col2, row2, 25*sc.mm, 12.5*sc.mm, stroke="black", stroke_width=2*sc.mm, fill="green", id="ellipse"))
d.add(sc.Polygon([col1-25*sc.mm,col1,col1+25*sc.mm,col1,col1-25*sc.mm],[row3-25*sc.mm,row3-25*sc.mm,row3,row3+25*sc.mm,row3+25*sc.mm], stroke='black', fill='yellow'))
d.add(sc.Polyline([col2-25*sc.mm,col2,col2+25*sc.mm,col2,col2-25*sc.mm],[row3-25*sc.mm,row3-25*sc.mm,row3,row3+25*sc.mm,row3+25*sc.mm], stroke='black', fill='orange'))
d.add(sc.EquilateralTriangle(col1, row4, 50*sc.mm, stroke="black", stroke_width=1*sc.mm, fill="red"))

d.save('example_shapes')
