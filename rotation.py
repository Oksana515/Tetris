from configuration_matrices import cf_m1, cf_m2, cf_m3, cf_m4, cf_m5, cf_m6, cf_m7


def rotate_matrix(some_config_matrix, rotation_number):
    # T-rotation
    if some_config_matrix == cf_m1:
        match rotation_number:
            case 0:
                transformed_matrix = [[x[0], x[1]] for x in some_config_matrix]
            case 1:
                transformed_matrix = [[x[1], x[0] * (-1)] for x in some_config_matrix]
            case 2:
                transformed_matrix = [[x[0] * (-1), x[1] * (-1)] for x in some_config_matrix]
            case 3:
                transformed_matrix = [[x[1] * (-1), x[0]] for x in some_config_matrix]
    # S-rotation
    elif some_config_matrix == cf_m2:
        match rotation_number:
            case 0 | 2:
                transformed_matrix = [[x[0], x[1]] for x in some_config_matrix]
            case 1 | 3:
                transformed_matrix = [[0, 0], [1, 0], [-1, -1], [0, -1]]
    # Z-rotation
    elif some_config_matrix == cf_m3:
        match rotation_number:
            case 0 | 2:
                transformed_matrix = [[x[0], x[1]] for x in some_config_matrix]
            case 1 | 3:
                transformed_matrix = [[0, 0], [1, 0], [0, 1], [-1, 1]]
    # I-rotation
    elif some_config_matrix == cf_m4:
        match rotation_number:
            case 0 | 2:
                transformed_matrix = [[x[0], x[1]] for x in some_config_matrix]
            case 1 | 3:
                transformed_matrix = [[0, 0], [1, 0], [2, 0], [3, 0]]
    # O-rotation
    elif some_config_matrix == cf_m5:
        transformed_matrix = [[x[0], x[1]] for x in some_config_matrix]
    # L-rotation
    elif some_config_matrix == cf_m6:
        match rotation_number:
            case 0:
                transformed_matrix = [[x[0], x[1]] for x in some_config_matrix]
            case 1:
                transformed_matrix = [[0, 0], [0, -1], [-1, -1], [-2, -1]]
            case 2:
                transformed_matrix = [[1, -1], [0, -1], [0, 0], [0, 1]]
            case 3:
                transformed_matrix = [[0, 0], [0, 1], [1, 1], [2, 1]]
    # J-rotation
    elif some_config_matrix == cf_m7:
        match rotation_number:
            case 0:
                transformed_matrix = [[x[0], x[1]] for x in some_config_matrix]
            case 1:
                transformed_matrix = [[0, 0], [0, 1], [1, 0], [2, 0]]
            case 2:
                transformed_matrix = [[0, 1], [0, 0], [0, 2], [1, 2]]
            case 3:
                transformed_matrix = [[1, 0], [1, 1], [0, 1], [-1, 1]]

    return transformed_matrix

