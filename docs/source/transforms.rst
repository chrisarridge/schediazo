Transforms
==========

All drawing parts can be transformed using any combination of affine transformations using the :py:class:`schediazo.transforms.Affine`
class.  The :py:func:`schediazo.transforms.identity` function returns an empty (identity) affine transformation object to which
other transforms can be added::

    affine_identity = schediazo.transforms.identity()
    affine_translate = affine_identity.translate(1.0,0.0)
    affine_rotate = schediazo.transforms.identity().rotate(90.0)
    affine_multiple = schediazo.transforms.identity().scale(2.0,3.0).translate(1.0,1.0).rotate(90.0)

To transform points using the affine object simply call::

    x_transformed, y_transformed = affine_translate(5.0, 2.0)

.. autoclass:: schediazo.transforms.Affine
    :members:
    :noindex:

.. autofunction:: schediazo.transforms.identity
    :noindex:

