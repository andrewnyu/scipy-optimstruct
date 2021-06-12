import numpy as np

class optim_dict:
    def __init__(self):
        self.var_dict = {}
    
    def __len__(self):
        return len(self.var_dict.keys())
    
    class optim_var:
        def __init__(self, var):
            self.var = var
            self.shape = var.shape

    
    def add_var(self, var_name, var):
        """
        Parameters:
        var_name (string): Key name of the variable
        var (np.array): N-D np.array of variable contents
        """
        self.var_dict[var_name] = self.optim_var(var)
    

    def toVector(self):
        """
        Returns:
        1-D np.array: Compresses contents of self.optim_dict into 1-D np.array required by Scipy Minimize
        """
        return np.hstack([optim_var.var.flatten() for optim_var in self.var_dict.values()])
    

    def toDict(self, x):
        """
        Parameters:
        x (1D np.array): Inputs to Scipy Minimize

        Returns:
        dictionary: Summarizes 1-D np.array from Scipy Minimize input into dictionary class with variables
            accessible by name
        """   

        def tuple_product(t):
            """
            Parameters:
            t (tuple)

            Returns:
            int: product of all elements in the tuple
            """   
            res = 1
            for x in t:
                res*=x
            return res

        return_dict = {}
        start_index = 0
        for var_name in self.var_dict.keys():
            var_shape = self.var_dict[var_name].shape
            end_index = start_index + tuple_product(var_shape)

            return_dict[var_name] = x[start_index:end_index].reshape(var_shape)
            start_index = end_index
        
        return return_dict
