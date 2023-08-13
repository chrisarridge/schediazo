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

path = sc.RawPath([sc.MoveTo(10*sc.mm,90*sc.mm),sc.QuadraticBezierTo(90*sc.mm,90*sc.mm,90*sc.mm,45*sc.mm),
                    sc.QuadraticBezierTo(90*sc.mm,10*sc.mm,50*sc.mm,10*sc.mm),
                    sc.QuadraticBezierTo(10*sc.mm,10*sc.mm,10*sc.mm,40*sc.mm),
                    sc.QuadraticBezierTo(10*sc.mm,70*sc.mm,45*sc.mm,70*sc.mm),
                    sc.QuadraticBezierTo(70*sc.mm,70*sc.mm,75*sc.mm,50*sc.mm)])
d.add(sc.Path(path, id="MyPath", fill="none", stroke="red"))
d.add(sc.TextPath("Quick brown fox jumps over the lazy dog.", href="#MyPath", fill="black", font_size=14*sc.pt))
d.save('example_text2')



d = sc.Drawing()
d.add(sc.Line(100*sc.mm, 0*sc.mm, 100*sc.mm, 80*sc.mm, stroke="grey", stroke_width=2*sc.pt))
d.add(sc.Text("Left-aligned", x=100*sc.mm, y=20*sc.mm, text_anchor=sc.TextAnchor.Start, fill="black", font_family="sans-serif", font_size=14*sc.pt))
d.add(sc.Text("Centred", x=100*sc.mm, y=40*sc.mm, text_anchor=sc.TextAnchor.Middle, fill="black", font_family="sans-serif", font_size=14*sc.pt))
d.add(sc.Text("Right-aligned", x=100*sc.mm, y=60*sc.mm, text_anchor=sc.TextAnchor.End, fill="black", font_family="sans-serif", font_size=14*sc.pt))
d.save('example_text3')
