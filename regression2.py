# -*- coding: utf-8 -*-


from pandas.io import wb
wb.search('gdp.*capita.*const').iloc[:,:2]

dat = wb.download(indicator='NY.GDP.PCAP.KD', country=['US', 'CA', 'MX'], start=2010, end=2013)
print(dat)

dat = wb.download(indicator='NY.GDP.PCAP.KD', country=['US', 'CA', 'MX'], start=2010, end=2013)
print(dat)

dat['NY.GDP.PCAP.KD'].groupby(level=0).mean()
wb.search('cell.*%').iloc[:,:2]

ind =['NY.GDP.PCAP.KD', 'IT.MOB.COV.ZS']
dat = wb.download(indicator=ind, country='all', start=2011, end=2011).dropna()
dat.columns = ['gdp', 'cellphone']


print(dat.tail())

import numpy as np
import statsmodels.formula.api as smf

mod = smf.ols("cellphone ~ np.log(gdp)", dat).fit()

print(mod.summary())
