# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import pandas
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

x = np.linspace(-5, 5, 20)

np.random.seed(1)

y = -5 + 3*x + 4 * np.random.normal(size=x.shape)

plt.figure(figsize=(5, 4))
plt.plot(x, y, 'o')




data = pandas.DataFrame({'x': x, 'y': y})
model = ols("y ~ x", data).fit()

print(model.summary())

print('\nANOVA results')


offset, coef = model._results.params
plt.plot(x, x*coef + offset)
plt.xlabel('x')
plt.ylabel('y')

plt.show()