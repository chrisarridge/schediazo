"""Example text rendering - implementing examples given in
https://developer.mozilla.org/en-US/docs/Web/SVG/Element/text
https://developer.mozilla.org/en-US/docs/Web/SVG/Element/textPath
"""

import schediazo as sc

d = sc.Drawing()

d.add(sc.Text("My", x=20*sc.mm, y=35*sc.mm, font_family="sans-serif", font_size=13*sc.pt, font_style=sc.FontStyle.Italic, fill="black"))
d.add(sc.Text("cat", x=40*sc.mm, y=35*sc.mm, font_family="sans-serif", font_size=30*sc.pt, font_weight=sc.FontWeight.Bold, fill="black"))
d.add(sc.Text("is", x=55*sc.mm, y=55*sc.mm, font_family="sans-serif", font_size=13*sc.pt, font_style=sc.FontStyle.Italic, fill="black"))
d.add(sc.Text("Grumpy!", x=65*sc.mm, y=55*sc.mm, font_family="serif", font_size=40*sc.pt, font_style=sc.FontStyle.Italic, fill="red"))

d.save('example_text1')

d = sc.Drawing()

# path = sc.RawPath([sc.MoveTo(10,90),sc.QuadraticBezierTo(90,90,90,45),sc.QuadraticBezierTo(90,10,50,10),
#                     sc.QuadraticBezierTo(10,10,10,40),sc.QuadraticBezierTo(10,70,45,70),sc.QuadraticBezierTo(70,70,75,50)])
# d.add(sc.Path(path, id="MyPath", fill="none", stroke="red"))
# d.add(sc.TextPath("Quick brown fox jumps over the lazy dog.", href="#MyPath"))
# d.save('example_text2')

d = sc.Drawing()
d.add(sc.Line(100*sc.mm, 0*sc.mm, 100*sc.mm, 80*sc.mm, stroke="grey", stroke_width=2*sc.pt))
d.add(sc.Text("Left-aligned", x=100*sc.mm, y=20*sc.mm, text_anchor=sc.TextAnchor.Start, fill="black", font_family="sans-serif", font_size=14*sc.pt))
d.add(sc.Text("Centred", x=100*sc.mm, y=40*sc.mm, text_anchor=sc.TextAnchor.Middle, fill="black", font_family="sans-serif", font_size=14*sc.pt))
d.add(sc.Text("Right-aligned", x=100*sc.mm, y=60*sc.mm, text_anchor=sc.TextAnchor.End, fill="black", font_family="sans-serif", font_size=14*sc.pt))
d.save('example_text3')
