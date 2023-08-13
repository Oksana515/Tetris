from configuration_matrices import cf_m1, cf_m2, cf_m3, cf_m4, cf_m5, cf_m6, cf_m7


def rotate_matrix(some_config_matrix, rotation_number):
    # T-rotation
    if some_config_matrix == cf_m1:
        if rotation_number == 0:
            transformed_matrix = [[x[0], x[1]] for x in some_config_matrix]
        elif rotation_number == 1:
            transformed_matrix = [[x[1], x[0] * (-1)] for x in some_config_matrix]
        elif rotation_number == 2:
            transformed_matrix = [[x[0] * (-1), x[1] * (-1)] for x in some_config_matrix]
        elif rotation_number == 3:
            transformed_matrix = [[x[1] * (-1), x[0]] for x in some_config_matrix]
    # S-rotation
    elif some_config_matrix == cf_m2:
        if rotation_number == 0:
            transformed_matrix = [[x[0], x[1]] for x in some_config_matrix]
        elif rotation_number == 1:
            transformed_matrix = [[0, 0], [1, 0], [-1, -1], [0, -1]]
        elif rotation_number == 2:
            transformed_matrix = [[x[0], x[1]] for x in some_config_matrix]
        elif rotation_number == 3:
            transformed_matrix = [[0, 0], [1, 0], [-1, -1], [0, -1]]
    # Z-rotation
    elif some_config_matrix == cf_m3:
        if rotation_number == 0:
            transformed_matrix = [[x[0], x[1]] for x in some_config_matrix]
        elif rotation_number == 1:
            transformed_matrix = [[0, 0], [1, 0], [0, 1], [-1, 1]]
        elif rotation_number == 2:
            transformed_matrix = [[x[0], x[1]] for x in some_config_matrix]
        elif rotation_number == 3:
            transformed_matrix = [[0, 0], [1, 0], [0, 1], [-1, 1]]
    # I-rotation
    elif some_config_matrix == cf_m4:
        if rotation_number == 0:
            transformed_matrix = [[x[0], x[1]] for x in some_config_matrix]
        elif rotation_number == 1:
            transformed_matrix = [[0, 0], [1, 0], [2, 0], [3, 0]]
        elif rotation_number == 2:
            transformed_matrix = [[x[0], x[1]] for x in some_config_matrix]
        elif rotation_number == 3:
            transformed_matrix = [[0, 0], [1, 0], [2, 0], [3, 0]]
    # O-rotation
    elif some_config_matrix == cf_m5:
        if rotation_number == 0 or rotation_number == 1 or rotation_number == 2 or rotation_number == 3:
            transformed_matrix = [[x[0], x[1]] for x in some_config_matrix]
    # L-rotation
    elif some_config_matrix == cf_m6:
        if rotation_number == 0:
            transformed_matrix = [[x[0], x[1]] for x in some_config_matrix]
        elif rotation_number == 1:
            transformed_matrix = [[0, 0], [0, -1], [-1, -1], [-2, -1]]
        elif rotation_number == 2:
            transformed_matrix = [[1, -1], [0, -1], [0, 0], [0, 1]]
        elif rotation_number == 3:
            transformed_matrix = [[0, 0], [0, 1], [1, 1], [2, 1]]
    # J-rotation
    elif some_config_matrix == cf_m7:
        if rotation_number == 0:
            transformed_matrix = [[x[0], x[1]] for x in some_config_matrix]
        elif rotation_number == 1:
            transformed_matrix = [[0, 0], [0, 1], [1, 0], [2, 0]]
        elif rotation_number == 2:
            transformed_matrix = [[0, 1], [0, 0], [0, 2], [1, 2]]
        elif rotation_number == 3:
            transformed_matrix = [[1, 0], [1, 1], [0, 1], [-1, 1]]

    return transformed_matrix

