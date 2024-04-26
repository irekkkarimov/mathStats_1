import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy


# def read_values(file_path):
#     file = pd.read_csv(file_path)
#     return list(map(lambda e: e[0], file.values))


def lab_4_2(file_path: str):
    values = pd.read_csv(file_path)

    y_const = 82
    x_values = values['X']
    y_values = values['Y']
    x_mean = x_values.mean()
    y_mean = y_values.mean()
    d_x = sum((i - x_mean) ** 2 for i in x_values) / len(x_values)
    d_y = sum((i - y_mean) ** 2 for i in y_values) / len(y_values)

    cov = sum((x_values[i] - x_mean) * (y_values[i] - y_mean)
              for i in range(len(x_values))) / len(x_values)
    cor = cov / (math.sqrt(d_x) * math.sqrt(d_y))
    cor_func = numpy.corrcoef(y_values, x_values)

    print("Коэффициент корреляции", cor)
    print(cor_func[0, 1])

    variance_y = sum((y - y_mean) ** 2 for y in y_values) / len(y_values)
    reg = cov / variance_y

    print("Коэффициент регрессии:", reg)

    intercept = x_mean - reg * y_mean
    x_point = reg * y_const + intercept

    plt.scatter(y_values, x_values, color="green", label="Исходные данные")
    plt.title('Диаграмма рассеивания')
    plt.xlabel('Y')
    plt.ylabel('X')
    plt.grid()
    plt.plot(y_values, reg * numpy.array(y_values) + intercept, color="orange", label="Линия регрессии")
    plt.scatter(y_const, x_point, color="black", label=f"Точка {y_const}, {x_point}")
    # trend = numpy.polyfit(y_values, x_values, 1)
    # trend_poly = numpy.poly1d(trend)
    # plt.plot(y_values, trend_poly(y_values))
    # plt.legend(['Данные', 'Линия регрессии'])
    plt.show()


lab_4_2('./data/r4z2.csv')
