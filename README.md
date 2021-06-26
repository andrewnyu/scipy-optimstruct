## Optimstruct

[![Build Status](https://travis-ci.com/andrewnyu/scipy-optimstruct.svg?branch=master)](https://travis-ci.com/andrewnyu/scipy-optimstruct.svg?branch=master)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg )](https://raw.githubusercontent.com/andrewnyu/scipy-optimstruct/master/LICENSE)

A simple helper function to enable an easier implementation of variables and constraints for Scipy Optimize
<br>
<br>
### Sample
<br>

```python
import numpy as np
from optimstruct.optim_dict import optim_dict

#initialize optim_dict
my_vars = optim_dict()

#add variables
foo1 = np.array([[1,2,3], [2,4,5], [3,5,7]])
my_vars.add_var("foo1", foo1)

foo2 = np.array([[1,12,3], [2,1,5], [3,55,7]])
my_vars.add_var("foo2", foo2)

#flatten variables into np.array ready to be used with Scipy minimize function
x = my_vars.toVector()

#return np.array into easily accessible dictionary in constrains
var_dict = my_vars.toDict(x)


```
