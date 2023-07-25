"""Example of using css classes"""
import schediazo as sc

d = sc.Drawing()
d.add_style("circle {\n\tfill: gold;\n\tstroke: maroon;\n\tstroke-width: 2px;\n}\n.font1 {font-size: 16px;}\n.font2 {font-size: 12px; font-weight:bold; fill: red;}")
d.add(sc.Circle(5, 5, 4))
d.add(sc.Text("This is 16px text using .font1 class", x=5, y=20, cssclass="font1"))
d.add(sc.Text("This is 12px bold text using .font2 class", x=5, y=40, cssclass="font2"))
d.save("style_example")
