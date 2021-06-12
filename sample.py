import numpy as np
from .optimstruct.optim_dict import optim_dict

my_vars = optim_dict()

#Add a variable
foo1 = np.array([[1,2,3], [2,4,5], [3,5,7]])
my_vars.add_var("foo1", foo1)

foo2 = np.array([[1,12,3], [2,1,5], [3,55,7]])
my_vars.add_var("foo2", foo2)

#flatten into np.array ready to be used with Scipy Minimize
x = my_vars.toVector()
print(x)

#return np.array into vector easily readible
var_dict = my_vars.toDict(x)
print(var_dict)
