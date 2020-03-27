# ipython-notebooks
My iPython Notebooks

<b>Covid-19 and Blood Types</b>

In the recent paper by Jiao Zhao, et al. it was reported that blood group (e.g., A, B, AB, or O) appears to have an effect on the likelihood of becoming infected with the Covid-19 virus. Basically, people with blood type A appear to be more susceptible to the virus, while people with blood type O appear to be less susceptible.

The authors of the paper performed several types of statistical analyses to arrive at their conclusion: one-way ANOVA, 2-tailed chi-square, and a meta-analysis using random effects models.  In this notebook, I've performed a different type of analysis, Bayesian Data Analysis (BDA), using the data reported in their paper.

[CAVEAT: No one has checked my work, so there could be errors in it] This BDA appears to support their conclusion, but also provides posterior density estimates for the proportions of A, B, AB, and O blood groups among the infected, along with credible intervals for those proportions. See the four posterior density plots at the end of this notebook.

<b>Monoids 101 for Apache Spark</b>
<p>This notebook describes what monoids are and the role they play in reduction and aggregation in Spark, specifically PySpark.  The following types of examples are included here, using reduce and reduceByKey to illustrate the use of the monoid concept:
  
* Word count
* Max/Min as monoids
* Histogram calculation using vectors as monoids
* Calculating sample means and standard deviations
* Calculating covariances and correlations using vectors and matrices as monoids
* Sets as monoids
* A HyperLogLog monoid (a "sketch method" for approximating set cardinality).  NOTE: Uses the implementation, <i>hllx.py</i> at https://github.com/Parsely/python-pds, which has been modified here to remove the dependency on the "smhasher" module and so that it can be run using the Anaconda Python distribution.</p>

<b>Extreme Value Theory (EVT)</b>
<p>Describes EVT calculations using an example from Stuart Cole's book, "An Introduction to Statistical Modeling of Extreme Values".  The calculations are done using both Python and R.  It is noted that there does not appear to be a standard representation of the GEV distribution. Representations differ on how the shape parameter, ξ, should be expressed. Specifically, the shape parameter in the 'ismev' package in R is the negative of the shape parameter in the Python 'scipy.stats.genextreme' module.</p>

<b>Quantile Example using R-8 Method</b>
<p>Someone asked me once how to compute quantiles. This notebook represents a partial answer to that question.  It provides examples of quantiles for a specific random sample using two versions of the R-8 method: (1) the 'mquantile' function found in the Python 'scipy.stats.mstats' module, and (2) a simple Python implementation based on Wikipedia's description of the R-8 method.</p>
