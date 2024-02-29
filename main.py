import math
import os

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

os.environ["XDG_SESSION_TYPE"] = "xcb"


def read_values(file_path):
    file = pd.read_csv(file_path)
    return list(map(lambda i: i[0], file.values))


def is_int(number):
    return number == int(number)


def calculate_quantile(quantile, values):
    val_length = len(values)
    index = val_length * quantile
    if is_int(index):
        return (values[index - 1] + values[index]) / 2
    return values[int(index)]


filePath = './10/r1z1.csv'
values = read_values(filePath)
values.sort()
length = len(values)
maxValue = values[-1]
minValue = values[0]
valueRange = maxValue - minValue
avg = sum(values) / length
value_popularity = dict()
most_popular = None
most_popular_count = 0
median = None
quantile25 = calculate_quantile(1 / 4, values)
quantile75 = calculate_quantile(3 / 4, values)
unbiased_variance = None
biased_variance = None
standard_deviation = None
interquartile_latitude = quantile75 - quantile25

for i, value in enumerate(values):
    if value not in value_popularity.keys():
        value_popularity[value] = 0
        continue
    value_popularity[value] += 1

for i, value in enumerate(value_popularity.keys()):
    if value_popularity[value] > most_popular_count:
        most_popular_count = value_popularity[value]
        most_popular = value

if length % 2 != 0:
    median = values[math.floor(length / 2)]
else:
    middle_index = int(length / 2)
    median = (values[middle_index - 1] + values[middle_index]) / 2

temp = 0
for i, value in enumerate(values):
    temp += (value - avg) * (value - avg)
unbiased_variance = temp / (length - 1)
biased_variance = temp / length
standard_deviation = math.sqrt(unbiased_variance)

print(values)
print('----------------')

print(f"Volume: {length}")
print(f"Maximum: {maxValue}")
print(f"Minimum: {minValue}")
print(f"Range: {valueRange}")
print("Average: " + "{:.2f}".format(avg))
print("Unbiased variance: " + "{:.2f}".format(unbiased_variance))
print("Biased variance: " + "{:.2f}".format(biased_variance))
print("Standard deviation: " + "{:.2f}".format(standard_deviation))
print(f"Mode: {most_popular}")
print(f"Median: {median}")
print(f"25% Quantile: {quantile25}")
print(f"75% Quantile: {quantile75}")
print(f"Interquartile latitude: {interquartile_latitude}")
print('------------------')

data_frame = pd.read_csv(filePath)

print(f"Maximum: {data_frame.max()}")
print(f"Minimum: {data_frame.min()}")
print(f"Average: {data_frame.mean()}")
print(f"Unbiased variance: {data_frame.var()}")
print(f"Biased variance: {data_frame.var() * (length - 1) / length}")
print(f"Standard deviation: {data_frame.std()}")
print(f"Mode: {data_frame.mode()}")
print(f"Median: {data_frame.median()}")
print(f"25% Quantile: {data_frame.quantile(0.25)}")
print(f"75% Quantile: {data_frame.quantile(0.75)}")
print(f"Interquartile latitude: {data_frame.quantile(0.75) - data_frame.quantile(0.25)}")


fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
calculations = ['max', 'min', 'avg']

ax.bar(calculations, np.random.rand(len(calculations)))
