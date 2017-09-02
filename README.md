# ipython-notebooks
My iPython Notebooks

<b>Monoids 101 for Apache Spark</b>
<p>This notebook describes what monoids are and the role they play in reduction and aggregation in Spark, specifically PySpark.  The following types of examples are included here, using reduce and reduceByKey to illustrate the use of the monoid concept:
* Word count
* Max/Min as monoids
* Histogram calculation using vectors as monoids
* Calculating sample means and standard deviations
* Calculating covariances and correlations using vectors and matrices as monoids
* Sets as monoids
* A HyperLogLog monoid (a "sketch method" for approximating set cardinality)
</p>

<b>Extreme Value Theory (EVT)</b>
<p>Describes EVT calculations using an example from Stuart Cole's book, "An Introduction to Statistical Modeling of Extreme Values".  The calculations are done using both Python and R.  It is noted that there does not appear to be a standard representation of the GEV distribution. Representations differ on how the shape parameter, ξ, should be expressed. Specifically, the shape parameter in the 'ismev' package in R is the negative of the shape parameter in the Python 'scipy.stats.genextreme' module.</p>

<b>Quantile Example using R-8 Method</b>
<p>Someone asked me once how to compute quantiles. This notebook represents a partial answer to that question.  It provides examples of quantiles for a specific random sample using two versions of the R-8 method: (1) the 'mquantile' function found in the Python 'scipy.stats.mstats' module, and (2) a simple Python implementation based on Wikipedia's description of the R-8 method.</p>
