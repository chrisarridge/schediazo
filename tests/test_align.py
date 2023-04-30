import unittest
import copy

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches

import schediazo.align

DRAW_RESULTS = True

class TestAlign(unittest.TestCase):
    def test_seven_segment(self):
        NUM_SEGMENTS = 7
        RADIUS = 10
        PHI_WIDTH = 2*np.pi/NUM_SEGMENTS
        TX = 1.0
        TY = 2.0

        # These are the coordinates of the triangle.
        x_origin = np.array([0,RADIUS*np.sin(PHI_WIDTH*0.5),-RADIUS*np.sin(PHI_WIDTH*0.5)])
        y_origin = np.array([0,-RADIUS*np.cos(PHI_WIDTH*0.5),-RADIUS*np.cos(PHI_WIDTH*0.5)])

        # These are our starting coordinates - we translate the first triangle to (1,2)
        x = copy.copy(x_origin) + TX
        y = copy.copy(y_origin) + TY

        if DRAW_RESULTS:
            c = ['r','g','b','k','r','g','b','k','r','g','b','k']
            ax=plt.figure().add_subplot()
            ax.add_patch(matplotlib.patches.Polygon(np.vstack((x, y)).T, closed=True, color=c[0], alpha=0.3))

        for i in range(1,NUM_SEGMENTS):
            aff = schediazo.align.two_point_align(x_origin[[0,2]], y_origin[[0,2]], x[[0,1]],y[[0,1]], tolerance=1e-7)
            print(aff)

            x, y = aff.transform(x_origin, y_origin)

            # Check the rotation and translation
            self.assertAlmostEqual(np.radians(aff._operations[1]._angle), PHI_WIDTH*i, 6)
            self.assertAlmostEqual(aff._operations[0]._x, TX, 5)
            self.assertAlmostEqual(aff._operations[0]._y, TY, 5)

            if DRAW_RESULTS:
                ax.add_patch(matplotlib.patches.Polygon(np.vstack((x, y)).T, closed=True, color=c[i], alpha=0.3))
                plt.scatter(x[[0,2]],y[[0,2]],c=['g','r'])

        if DRAW_RESULTS:
            ax.set_xlim(-10,10)
            ax.set_ylim(-10,10)
            ax.set_aspect('equal')
            plt.show()

if __name__=='__main__':
    unittest.main()