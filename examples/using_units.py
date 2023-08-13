import schediazo as sc

d = sc.Drawing(width=10*sc.cm, height=10*sc.cm)

# d.add(sc.Rect(1*sc.cm, 1*sc.cm, 9*sc.cm, 9*sc.cm, stroke="black", stroke_width=0.25*sc.pt, fill_opacity=0, id="surrounding-rect"))
# d.add(sc.Circle(50, 50, 10, stroke="black", stroke_width=1*sc.pt, fill="yellow", units=sc.mm))

d.save('example_using_units')
