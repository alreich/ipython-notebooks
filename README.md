# ipython-notebooks
My iPython Notebooks

[Extreme Value Theory (EVT)](http://nbviewer.ipython.org/gist/alreich/8854279) -- Describes EVT calculations using an example from Stuart Cole's book, "An Introduction to Statistical Modeling of Extreme Values".  The calculations are done using both Python and R.  It is noted that there does not appear to be a standard representation of the GEV distribution. Algorithms appear to differ on how the shape parameter, ξ, should be represented. Specifically, the shape parameter in the ismev package in R is the negative of the shape parameter in scipy.stats.genextreme.

[Quantile Example using R-8 Method](http://nbviewer.ipython.org/gist/alreich/8984544) -- Examples of quantiles for a random sample of integers are computed here using two versions of the R-8 method: (1) the 'mquantile' function found in scipy.stats.mstats and (2) a simple implementation based on the description of the R-8 method in Wikipedia.
