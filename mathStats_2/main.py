import numpy
import pandas as pd
from scipy.stats import norm


def read_values(file_path):
    file = pd.read_csv(file_path)
    return list(map(lambda e: e[0], file.values))


def lab_2_1(file_path: str):
    values = read_values(file_path)
    mean = numpy.mean(values)
    mle = 1 / mean
    print(f'Оценка максимального правдоподобия: {mle}')


def lab_2_2(file_path: str):
    values = read_values(file_path)
    count = len(values)
    success_count = len(list(filter(lambda x: x > 117.5, values)))

    q = .975
    alpha = (1 - q)

    # Оценка вероятности
    p = success_count / count

    # Стандартное отклонение
    m = numpy.sqrt(p * (1 - p) / count)

    # Квантиль
    z_alpha = norm.ppf(q)

    # Верхняя граница
    upper_boundary = p + m * z_alpha

    print(f'Верхняя граница: {upper_boundary}')


def execute():
    lab_2_1('./data/r3z1.csv')
    lab_2_2('./data/r3z2.csv')


execute()
