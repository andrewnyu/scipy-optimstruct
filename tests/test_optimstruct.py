
def add_src_to_path():
    import sys
    sys.path.append("src/")
    print("Added ../src/ to path")

def test_init():
    
    add_src_to_path()

    from scipy_optimstruct  import optim_dict
    var_dict = optim_dict()

    assert isinstance(var_dict, optim_dict)

