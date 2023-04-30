from typing import List, Tuple, Union
import math
import numpy as np

from .transforms import identity

def two_point_align(xa: Union[List[float],Tuple,np.ndarray], ya: Union[List[float],Tuple,np.ndarray],
                    xb: Union[List[float],Tuple,np.ndarray], yb: Union[List[float],Tuple,np.ndarray],
                    max_iter: int=50, rate_drop: float=0.95, tolerance: float=1e-6, verbose: bool=False):
    """For a pair of points we solve Wahba's problem in 2D for rotation and translation to align the points

    Points [a] are rotated and translated so that they align with points [b].

    Args:
        :param array xa: X coordinates for point set a.
        :param array ya: Y coordinates for point set a.
        :param array xb: X coordinates for point set b.
        :param array yb: Y coordinates for point set b.
        :param int max_iter: maximum number of iterations.
        :param int num_points: number of points used to find a solution.
        :param bool plot_end: plot the points for the terminal solution
        :return tuple angle, translate_x, translate_y: rotation angle and translation vector
    """
    def cost(xa,ya,xb,yb,th):
        tmp_x = (xa[0]-xa[1])*np.cos(th) - (ya[0]-ya[1])*np.sin(th) - xb[0] + xb[1]
        tmp_y = (xa[0]-xa[1])*np.sin(th) + (ya[0]-ya[1])*np.cos(th) - yb[0] + yb[1]
        rms = np.sqrt(tmp_x**2 + tmp_y**2)
        return rms

    def deriv(xa,ya,xb,yb,th):
        tmp_x = (xa[0]-xa[1])*np.cos(th) - (ya[0]-ya[1])*np.sin(th) - xb[0] + xb[1]
        tmp2_x = -(xa[0]-xa[1])*np.sin(th) - (ya[0]-ya[1])*np.cos(th)
        tmp_y = (xa[0]-xa[1])*np.sin(th) + (ya[0]-ya[1])*np.cos(th) - yb[0] + yb[1]
        tmp2_y = (xa[0]-xa[1])*np.cos(th) - (ya[0]-ya[1])*np.sin(th)
        return 2*tmp_x*tmp2_x + 2*tmp_y*tmp2_y

    # Find starting guess.
    th = np.linspace(0.0, 2*math.pi, 360)
    rms = cost(xa,ya,xb,yb,th)
    this_th = th[np.argmin(rms)]
    if verbose:
        print('starting guess {}'.format(this_th))
        # plt.plot(th,rms)
        # plt.show()

    # Gradient descent step.
    if np.abs(cost(xa,ya,xb,yb,this_th))<1e-7:
        done = True
    else:
        done = False
    iter = 0
    rate = 1*np.pi/180.0
    while iter<max_iter and not done:

        descended = False
        descend_check_iter=0
        while not descended and descend_check_iter<10:
            dth = np.abs(deriv(xa,ya,xb,yb,this_th)*rate)
            next_th = this_th - deriv(xa,ya,xb,yb,this_th)*rate
            if cost(xa,ya,xb,yb,next_th)<cost(xa,ya,xb,yb,this_th):
                descended = True
            else:
                if verbose:
                    print('finding best rate {}: this_th={} next_th={} rate={} cost(this_th)={} cost(next_th)={}'.format(descend_check_iter,this_th, next_th, rate, cost(xa,ya,xb,yb,this_th), cost(xa,ya,xb,yb,next_th)))
                rate /= 2.0
                descend_check_iter += 1

        if descend_check_iter==20:
            raise ValueError

        if verbose:
            print(iter, this_th, next_th, cost(xa,ya,xb,yb,next_th), dth/this_th)

        this_th = next_th
        if np.abs(dth/this_th)<tolerance:
            done = True

        rate *= rate_drop
        iter += 1

    # Now we have the angle, find the translation
    tx = xb[0] - xa[0]*np.cos(this_th) + ya[0]*np.sin(this_th)
    ty = yb[0] - xa[0]*np.sin(this_th) - ya[0]*np.cos(this_th)

    # Now we have the rotation angle and the translation, construct an affine transform and
    # return.
    return identity().rotate(np.degrees(this_th)).translate(tx, ty)
