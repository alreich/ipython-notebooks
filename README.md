# ipython-notebooks
My iPython Notebooks

[Monoids 101 for Apache Spark](http://nbviewer.ipython.org/gist/alreich/132e9bd0a396168aa1d0) -- This notebook describes what monoids are and the role they play in reduction and aggregation in Spark, specifically PySpark.  The following types of examples are included here, using reduce and reduceByKey to illustrate the use of the monoid concept:
* Word count
* Max/Min as monoids
* Histogram calculation using vectors as monoids
* Calculating sample means and standard deviations
* Calculating covariances and correlations using vectors and matrices as monoids
* Sets as monoids
* A HyperLogLog monoid (a "sketch method" for approximating set cardinality)

[Extreme Value Theory (EVT)](http://nbviewer.ipython.org/gist/alreich/8854279) -- Describes EVT calculations using an example from Stuart Cole's book, "An Introduction to Statistical Modeling of Extreme Values".  The calculations are done using both Python and R.  It is noted that there does not appear to be a standard representation of the GEV distribution. Representations differ on how the shape parameter, ξ, should be expressed. Specifically, the shape parameter in the 'ismev' package in R is the negative of the shape parameter in the Python 'scipy.stats.genextreme' module.

[Quantile Example using R-8 Method](http://nbviewer.ipython.org/gist/alreich/8984544) -- Examples of quantiles for a random sample of integers are computed here using two versions of the R-8 method: (1) the 'mquantile' function found in scipy.stats.mstats and (2) a simple implementation based on the description of the R-8 method in Wikipedia.
