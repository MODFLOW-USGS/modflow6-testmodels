This is Steffen Mehl's LGR test problem.  The original LGR model is included in the lgr folder here.  There is an ipython notebook up one folder and in the python directory that can be used to view head plots and head difference plots between MODFLOW-2015 and MODFLOW-LGR.

For the MODFLOW-2015 simulation, the parent and child models can be coupled in several different ways.  It seems that all of the ways are working now and the budget terms look correct, and include the effects of ghost nodes.  There is still one small issue with the ghost nodes in that the vertical ghost nodes are based on an inverse distance weighting scheme.  This should probably be switched to bilinear interpolation.  The flopy2015 code was used to create some of these data sets.  This is test2 in the flopy2015 examples.

With MODFLOW-2015 this LGR problem can be coupled in the following ways:

  1.  Parent and child models implicitly coupled in the same solution.  The following SOLUTION_GROUP block shows how this is specified in the simulation name file.
  
      #implicit coupling
      BEGIN SOLUTION_GROUP 1
        MXITER 1
        NUMERICAL ex3_parent.sms PARENT CHILD
      END SOLUTION_GROUP
      
      Ghost node correction is added implicitly, by expanding the global solution matrix.  An implicit ghost node correction is activated in the  simulation.exg file within the ghost node section.  The IMPLICIT keyword is added to the ghost node options.
      
      #ghost nodes
      BEGIN OPTIONS
        IMPLICIT
        ECHO
        PRINT
      END OPTIONS

  2.  Same as (1.) except ghost nodes are added to the right-hand side as a correction term, instead of implicitly by expanding the matrix.  The model still behaves well, although additional outer iterations are required.  Ghost nodes are added explicitly by removing the "IMPLICIT" keyword from the ghost node options.
  
  3.  (4/19/2015 Explicit coupling not supported) Parent and child models are coupled explicitly as is done in MODFLOW-LGR.  The following SOLUTION_GROUP block shows how this is specified in the simulation name file.
  
      #explicit coupling
      BEGIN SOLUTION_GROUP 1
        MXITER 500
        NUMERICAL ex3_parent.sms PARENT 
        NUMERICAL ex3_parent.sms CHILD
      END SOLUTION_GROUP
  
      In this case, an outer iteration loop is required to run repeatedly until there is convergence on the exchange between the two models.  For explicitly coupled models, ghost nodes must also be explicit.  