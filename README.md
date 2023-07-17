# scipy-optimstruct

[![Build Status](https://travis-ci.com/andrewnyu/scipy-optimstruct.svg?branch=master)](https://travis-ci.com/andrewnyu/scipy-optimstruct.svg?branch=master)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg )](https://raw.githubusercontent.com/andrewnyu/scipy-optimstruct/master/LICENSE)

scipy-optimstruct is a Python package that simplifies the implementation of variables and constraints for optimization problems using the SciPy optimization module. It provides a convenient way to define and manage problem structures, making it easier to solve optimization problems.

## Features

- **Introduction to Optimization Problem Structures:** The package includes a Jupyter notebook that provides an introduction to optimization problem structures and demonstrates how to use the SciPy optimization module to solve optimization problems.

- **Examples of Optimization Problem Structures:** The package provides examples of optimization problem structures, including linear programming, quadratic programming, and nonlinear programming.

- **Sample Code:** The package includes sample code that demonstrates how to use the optimization problem structures to solve practical problems.

- **Requirements:** The package includes a requirements.txt file that lists the required Python packages to run the example code.

## Usage

To use scipy-optimstruct, follow these steps:

1. Install the package using pip:

   ```shell
   pip install scipy-optimstruct

Make sure you have the required Python packages installed. You can find the complete list in the requirements.txt file included with the package.

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
