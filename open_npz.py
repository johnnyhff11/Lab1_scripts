def open_npz(captured_data, arr_1, arr_2):
    import numpy as np #Package needed for opening npz file!
    if type(captured_data) != 'str':
        package = f'{captured_data}'

    elif type(captured_data) = 'str':
        package = captured_data
        
    npz_opened = np.load(package, arr_1, arr_2)
