import unittest
import xml.etree.ElementTree as ET

import schediazo.attributes
from schediazo.units import ureg, mm, pt, px, inch

class TestBase:
    def set_element_attributes(self, element, device_per_length=None, device_per_pixel=None):
        pass

class TestClippable(schediazo.attributes.Clip,TestBase):
    def set_element_attributes(self, element, device_per_length=72*ureg.device/inch, device_per_pixel=1*ureg.device/px):
        super(TestClippable, self).set_element_attributes(element, device_per_length=device_per_length, device_per_pixel=device_per_pixel)

class TestStylable(schediazo.attributes.Styling,TestBase):
    def set_element_attributes(self, element, device_per_length=72*ureg.device/inch, device_per_pixel=1*ureg.device/px):
        super(TestStylable, self).set_element_attributes(element, device_per_length=device_per_length, device_per_pixel=device_per_pixel)

class TestStrokable(schediazo.attributes.Stroke,TestBase):
    def set_element_attributes(self, element, device_per_length=72*ureg.device/inch, device_per_pixel=1*ureg.device/px):
        super(TestStrokable, self).set_element_attributes(element, device_per_length=device_per_length, device_per_pixel=device_per_pixel)

class TestFillable(schediazo.attributes.Fill,TestBase):
    def set_element_attributes(self, element, device_per_length=72*ureg.device/inch, device_per_pixel=1*ureg.device/px):
        super(TestFillable, self).set_element_attributes(element, device_per_length=device_per_length, device_per_pixel=device_per_pixel)

class TestFontable(schediazo.attributes.Font,TestBase):
    def set_element_attributes(self, element, device_per_length=72*ureg.device/inch, device_per_pixel=1*ureg.device/px):
        super(TestFontable, self).set_element_attributes(element, device_per_length=device_per_length, device_per_pixel=device_per_pixel)

class TestTextRenderable(schediazo.attributes.TextRendering,TestBase):
    def set_element_attributes(self, element, device_per_length=72*ureg.device/inch, device_per_pixel=1*ureg.device/px):
        super(TestTextRenderable, self).set_element_attributes(element, device_per_length=device_per_length, device_per_pixel=device_per_pixel)



class TestClipping(unittest.TestCase):
    def test_bad_inputs(self):
        self.assertRaises(TypeError, TestClippable, 42)

    def test_element(self):
        root = ET.Element("test")
        TestClippable("hello").set_element_attributes(root)
        self.assertEqual(root.attrib['clip-path'], "url(#hello)")


class TestStyling(unittest.TestCase):
    def test_bad_inputs(self):
        self.assertRaises(TypeError, TestStylable, style=42)
        self.assertRaises(TypeError, TestStylable, cssclass=21)
        self.assertRaises(TypeError, TestStylable, style=42, cssclass=21)

    def test_element(self):
        root = ET.Element("test")

        TestStylable().set_element_attributes(root)
        self.assertEqual(len(root.attrib), 0)

        TestStylable(style="font-size: 14px; fill: #43311a;", cssclass="myclass").set_element_attributes(root)
        self.assertEqual(len(root.attrib), 2)
        self.assertEqual(root.attrib['style'], "font-size: 14px; fill: #43311a;")
        self.assertEqual(root.attrib["class"], "myclass")


class TestStroke(unittest.TestCase):
    def test_bad_inputs(self):
        self.assertRaises(TypeError, TestStrokable, stroke=42)

        self.assertRaises(TypeError, TestStrokable, stroke_dash_array=42)
        self.assertRaises(TypeError, TestStrokable, stroke_dash_array=[42,13,11,"hello"])

        self.assertRaises(TypeError, TestStrokable, stroke_dash_offset=42)

        self.assertRaises(TypeError, TestStrokable, stroke_linecap="butt")

        self.assertRaises(TypeError, TestStrokable, stroke_linejoin="bevel")

        self.assertRaises(TypeError, TestStrokable, stroke_miterlimit="hello")

        self.assertRaises(TypeError, TestStrokable, stroke_opacity="hello")

        self.assertRaises(TypeError, TestStrokable, stroke_width="hello")
        self.assertRaises(TypeError, TestStrokable, stroke_width=42)
        self.assertRaises(TypeError, TestStrokable, stroke_width=ureg.device)
        self.assertRaises(TypeError, TestStrokable, stroke_width=ureg.percent)

    def test_element(self):
        root = ET.Element("test")

        TestStrokable().set_element_attributes(root)
        self.assertEqual(len(root.attrib), 0)

        TestStrokable(stroke="green",
                    stroke_dash_array=[40*ureg.percent, 20*ureg.percent, 20*ureg.percent, 20*ureg.percent],
                    stroke_dash_offset=4*mm,
                    stroke_linecap=schediazo.attributes.LineCap.ROUND,
                    stroke_linejoin=schediazo.attributes.LineJoin.BEVEL,
                    stroke_miterlimit=0.5,
                    stroke_opacity=1.1,
                    stroke_width=2*pt).set_element_attributes(root)
        self.assertEqual(len(root.attrib),8)
        self.assertEqual(root.attrib["stroke"], "green")
        self.assertEqual(root.attrib["stroke-dasharray"].strip(), "40.000000% 20.000000% 20.000000% 20.000000%")
        self.assertEqual(root.attrib["stroke-dashoffset"], "4.000000mm")
        self.assertEqual(root.attrib["stroke-linecap"], "round")
        self.assertEqual(root.attrib["stroke-linejoin"], "bevel")
        self.assertEqual(root.attrib["stroke-miterlimit"], "0.5")
        self.assertEqual(root.attrib["stroke-opacity"], "1.0")
        self.assertEqual(root.attrib["stroke-width"], "2.000000pt")

class TestFill(unittest.TestCase):
    def test_bad_inputs(self):
        self.assertRaises(TypeError, TestFillable, fill=42)
        self.assertRaises(TypeError, TestFillable, fill_opacity="hello")
        self.assertRaises(TypeError, TestFillable, fill=42, fill_opacity="hello")

    def test_element(self):
        root = ET.Element("test")

        TestFillable().set_element_attributes(root)
        self.assertEqual(len(root.attrib), 1)

        TestFillable(fill="green", fill_opacity=1.1).set_element_attributes(root)
        self.assertEqual(len(root.attrib),2)
        self.assertEqual(root.attrib["fill"], "green")
        self.assertEqual(root.attrib["fill-opacity"], "1.0")

        TestFillable(fill_opacity=1.1).set_element_attributes(root)
        self.assertEqual(len(root.attrib),2)
        self.assertEqual(root.attrib["fill"], "none")
        self.assertEqual(root.attrib["fill-opacity"], "1.0")


class TestFont(unittest.TestCase):
    def test_bad_inputs(self):
        self.assertRaises(TypeError, TestFontable, font_family=42)
        self.assertRaises(TypeError, TestFontable, font_size=14)
        self.assertRaises(TypeError, TestFontable, font_size="12pt")
        self.assertRaises(ValueError, TestFontable, font_stretch=42*mm)
        self.assertRaises(TypeError, TestFontable, font_stretch="42mm")
        self.assertRaises(TypeError, TestFontable, font_stretch="condensed")
        self.assertRaises(TypeError, TestFontable, font_style="oblique")
        self.assertRaises(TypeError, TestFontable, font_variant="smallcaps")
        self.assertRaises(TypeError, TestFontable, font_weight="bold")
        self.assertRaises(TypeError, TestFontable, font_weight=700.0)
        self.assertRaises(ValueError, TestFontable, font_weight=-42)

    def test_element(self):
        root = ET.Element("test")
        TestFontable(font_family="Arial, sans-serif",
                 font_size=14*pt,
                 font_stretch=10*ureg.percent,
                 font_style=schediazo.attributes.FontStyle.Oblique,
                 font_variant=schediazo.attributes.FontVariant.Normal,
                 font_weight=900).set_element_attributes(root)
        self.assertEqual(len(root.attrib), 6)
        self.assertEqual(root.attrib['font-family'], "Arial, sans-serif")
        self.assertEqual(root.attrib['font-size'], "14.000000pt")
        self.assertEqual(root.attrib['font-stretch'], "10.000000%")
        self.assertEqual(root.attrib['font-style'], "oblique")
        self.assertEqual(root.attrib['font-variant'], "normal")
        self.assertEqual(root.attrib['font-weight'], "900")

        root2 = ET.Element("test")
        TestFontable(font_family="Arial, sans-serif",
                 font_size=schediazo.attributes.FontSize.XLarge,
                 font_stretch=schediazo.attributes.FontStretch.SemiCondensed,
                 font_style=schediazo.attributes.FontStyle.Oblique,
                 font_variant=schediazo.attributes.FontVariant.Normal,
                 font_weight=schediazo.attributes.FontWeight.Bolder).set_element_attributes(root2)
        self.assertEqual(len(root2.attrib), 6)
        self.assertEqual(root2.attrib['font-family'], "Arial, sans-serif")
        self.assertEqual(root2.attrib['font-size'], "x-large")
        self.assertEqual(root2.attrib['font-stretch'], "semi-condensed")
        self.assertEqual(root2.attrib['font-style'], "oblique")
        self.assertEqual(root2.attrib['font-variant'], "normal")
        self.assertEqual(root2.attrib['font-weight'], "bolder")



class TestTextRendering(unittest.TestCase):
    def test_bad_inputs(self):
        self.assertRaises(TypeError, TestTextRenderable, text_anchor="start")

    def test_element(self):
        root = ET.Element("test")

        TestTextRenderable().set_element_attributes(root)
        self.assertEqual(len(root.attrib), 0)

        TestTextRenderable(text_anchor=schediazo.attributes.TextAnchor.Middle).set_element_attributes(root)
        self.assertEqual(len(root.attrib),1)
        self.assertEqual(root.attrib["text-anchor"], "middle")




if __name__=='__main__':
    unittest.main()
