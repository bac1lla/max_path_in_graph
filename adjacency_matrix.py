def adjacency_matrix_is_empty(mx):
    for row in mx:
        if any(row):
            return False
    else:
        return True