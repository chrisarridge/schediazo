import schediazo as sc

d = sc.Drawing()

# Make the edge of the pencil
d.add(sc.Rect(0, 0, 100, 20, stroke='black', stroke_width=1, fill='rgb(244,186,0)', id='pencil-outline'))

# Make some lines on the pencil.
d.add(sc.Line(0, 20*0.35, 100, 20*0.35, stroke='black', stroke_width=0.5, id='pencil-line1'))
d.add(sc.Line(0, 20*0.65, 100, 20*0.65, stroke='black', stroke_width=0.5, id='pencil-line2'))

# Make the wood and tip of the pencil.
d.add(sc.Polygon([100,130,100], [0,10,20],
                stroke='black', stroke_width=1.0, fill='rgb(225,201,167)', id='wood'))

tip_clip_path = sc.ClipPath(id='tip-clip-path')
tip_clip_path.add(sc.Rect(120,0,130,20))
d.add_def(tip_clip_path)
d.add(sc.Polygon([100,130,100], [0,10,20], stroke='none', fill='rgb(25,25,25)', id='tip', clip_path='tip-clip-path'))

d.save('pencil')