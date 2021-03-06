Features
========

The features in Mushroom are 1-D arrays computed applying a specified function
to a raw input, e.g. polynomial features of the state of an MDP.
Mushroom supports three types of features:

* basis functions;
* tensor basis functions;
* tiles.

The GPU-accelerated basis functions are a Pytorch implementation of the standard
basis functions. They are less straightforward than the standard ones, but they
are faster to compute as they can exploit parallel computing, e.g. GPU-acceleration
and multi-core systems.

All the types of features are exposed by a single factory method ``Features``
that builds the one requested by the user.

.. automodule:: mushroom.features.features
    :members:
    :private-members:
    :inherited-members:
    :undoc-members:
    :show-inheritance:

The factory method returns a class that extends the abstract class
``FeatureImplementation``.

.. automodule:: mushroom.features._implementations.features_implementation
    :members:
    :private-members:
    :inherited-members:
    :undoc-members:
    :show-inheritance:

Components
----------

.. toctree::

    mushroom.features.basis
    mushroom.features.tensors
    mushroom.features.tiles
