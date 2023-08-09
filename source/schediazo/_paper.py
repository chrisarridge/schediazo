import enum

from .units import mm

class PaperSize(enum.Enum):
    """Paper size definitions.

    Attributes
    ----------
    A0
        ISO 216 A0 size 841x1189 mm
    A1
        ISO 216 A1 size 594x811 mm
    A2
        ISO 216 A2 size 420x594 mm
    A3
        ISO 216 A3 size 297x420 mm
    A4
        ISO 216 A4 size 210x297 mm
    A5
        ISO 216 A5 size 148x210 mm
    A6
        ISO 216 A6 size 105x148 mm
    A7
        ISO 216 A7 size 74x105 mm
    A8
        ISO 216 A8 size 52x74 mm
    A9
        ISO 216 A9 size 37x52mm
    A10
        ISO 216 A10 size 26x37mm
    """
    A0 = (841.0*mm, 1189.0*mm)
    A1 = (594.0*mm, 841.0*mm)
    A2 = (420.0*mm, 594.0*mm)
    A3 = (297.0*mm, 420.0*mm)
    A4 = (210.0*mm, 297.0*mm)
    A5 = (148.0*mm, 210.0*mm)
    A6 = (105.0*mm, 148.0*mm)
    A7 = (74.0*mm, 105.0*mm)
    A8 = (52.0*mm, 74.0*mm)
    A9 = (37.0*mm, 52.0*mm)
    A10 = (26.0*mm, 37.0*mm)


