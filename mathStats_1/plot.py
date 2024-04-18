import numpy as np


def get_bounds(values, steps_count, step):
    result = [values[0] + step / 2]

    for i in range(1, steps_count - 2):
        result.append(result[i - 1] + step)

    result.append(result[len(result) - 1] + step)
    return np.array(result)


def get_counts_in_bounds(values, bounds):
    result = []

    left_bound = float('-inf')
    right_bound = bounds[0]

    result.append(__get_counts_in_bounds(values, left_bound, right_bound))
    elements_counted = result[0]

    for i in range(bounds.size - 1):
        left_bound = bounds[i]
        right_bound = bounds[i + 1]
        result.append(__get_counts_in_bounds(values, left_bound, right_bound, elements_counted))
        elements_counted += result[len(result) - 1]

    left_bound = bounds[bounds.size - 1]
    right_bound = float('inf')
    result.append(__get_counts_in_bounds(values, left_bound, right_bound, elements_counted))
    return np.array(result)


def get_probs(values, counts_in_bounds):
    result = []
    for i in counts_in_bounds:
        result.append(i / len(values))

    return np.array(result)


def __get_counts_in_bounds(values, left_boundary, right_boundary, start_index=0):
    result = 0

    for i in range(start_index, len(values)):
        if left_boundary <= values[i] < right_boundary:
            result += 1
        else:
            break

    return result
