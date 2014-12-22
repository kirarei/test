# -*- coding: utf-8 -*-
import numpy as np

import pandas
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from pandas import DataFrame, Series

import statsmodels.formula.api as sm
from sklearn.linear_model import LinearRegression

import scipy, scipy.stats

 
data =pandas.read_csv('C:/anova_test3.csv', sep=',', na_values=".")
print data


df = pandas.DataFrame(data, columns=['gender', 'num', 'value'])
formula = 'value ~ C(gender) + C(num)+ C(gender):C(num)'
lm = ols(formula, df).fit()
print(anova_lm(lm))


