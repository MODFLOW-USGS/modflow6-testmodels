This example is included in the XT3D documentation.  It demonstrates the
application of the "XT3D" option to a 2D grid that consists of an
irregular, triangular grid nested within a coarser, regular grid. The
grid does not satisfy the standard CVFD requirements because, as a rule,
the straight-line connection between the centers of two adjacent triangular
cells, or between the center of a square cell and the center of an adjacent
triangular cell, does not intersect the corresponding cell interface at a
right angle. In this case, use of the "XT3D" option is expected to improve
solution accuracy compared to the standard, conductance-based formulation
used by the NPF Package.

This version of the problem uses the "XT3D" option.
