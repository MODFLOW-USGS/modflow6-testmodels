This is a simple unstructured model (the first example in usg document)
for testing the new gwf process.

Using a rotated anistropic K to test the case where the edge normal
is not the same as the connection normal (this occurs along interfaces
between changes in refinement).

HK is 10. and HANI is 0.1.  This makes the K value along the column
equal to 1.0, which is the value we want to assign to rows, so that
we get the same answer as gwf3_disv.  So then we set angle1 to 90
degrees, which rotates our 1 value to point along rows.

For this 1D flow problem, should get the same flows as the gwf3_disv
problem.
