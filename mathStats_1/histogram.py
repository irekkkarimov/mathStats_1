import numpy as np
from matplotlib.patches import Rectangle
from scipy.stats import norm

import plot

style = 'seaborn-v0_8'
color = '#1846a1'
fs_big = 24
fs_little = 16


def configure(axis, title, x_label, y_label):
    axis.set_title(title, fontdict={'fontsize': fs_big, 'fontweight': 'bold', 'color': color})
    axis.set_xlabel(x_label, fontdict={'fontsize': fs_little, 'color': color})
    axis.set_ylabel(y_label, fontdict={'fontsize': fs_little, 'color': color})


def build_histogram(axis, values, step, boundaries, col_heights):
    axis.add_patch(Rectangle((values[0], 0), step, col_heights[0], color=color))
    b_index = 0
    for i in range(1, col_heights.size - 1):
        axis.add_patch(Rectangle((boundaries[b_index], 0), step, col_heights[i], color=color))
        b_index += 1

    axis.add_patch(Rectangle((boundaries[b_index], 0), step, col_heights[col_heights.size - 1], color=color))


def build_normal_distribution(axis, step, min_value, max_value, avg, standard_deviation):
    dist_range = np.arange(min_value - 2 * step, max_value + 2 * step, 0.001)
    axis.plot(dist_range, norm.pdf(dist_range, avg, standard_deviation),
              color='red', label='Нормальное распределение')


def build_data_info(axis, quantile25, median, avg, quantile75, y_max, y_min=0):
    axis.vlines(x=quantile25, ymin=y_min, ymax=y_max, color='#b064c4', label='Квантиль 25%')
    axis.vlines(x=median, ymin=y_min, ymax=y_max, color='#4f96b8', label='Медиана')
    axis.vlines(x=avg, ymin=y_min, ymax=y_max, color='#32a852', label='Математическое ожидание')
    axis.vlines(x=quantile75, ymin=y_min, ymax=y_max, color='#b064c4', label='Квантиль 75%')


def build_freq_hist(freq_hist_axis, values, steps_count, step, quantile25, median, avg, quantile75):
    bounds = plot.get_bounds(values, steps_count, step)
    counts_in_boundaries = plot.get_counts_in_bounds(values, bounds)
    build_histogram(freq_hist_axis, values, step, bounds, counts_in_boundaries)
    freq_hist_axis.plot()
    build_data_info(freq_hist_axis, quantile25, median, avg, quantile75, y_max=max(counts_in_boundaries) * 1.2)
    configure(freq_hist_axis, 'Частотная гистограмма', 'Данные', 'Частота')


def build_prob_hist(prob_hist_axis, values, steps_count, step, min_value, max_value,
                    quantile25, median, avg, quantile75, standard_deviation):
    bounds = plot.get_bounds(values, steps_count, step)
    counts_in_bounds = plot.get_counts_in_bounds(values, bounds)
    probs_in_bounds = plot.get_probs(values, counts_in_bounds)
    heights_in_bounds = probs_in_bounds / step
    build_histogram(prob_hist_axis, values, step, bounds, heights_in_bounds)
    build_normal_distribution(prob_hist_axis, step, min_value, max_value, avg, standard_deviation)
    build_data_info(prob_hist_axis, quantile25, median, avg, quantile75, y_max=max(heights_in_bounds) * 1.2)
    configure(prob_hist_axis, 'Вероятностная гистограмма', 'X', 'Y')


def build_dist_function(dist_func_axis, values, step, min_value, max_value, avg, standard_deviation):
    unique_elements = list(set(values))
    counts = list({
                      i: list(values).count(i) for i in values
                  }.values())

    probs = []
    for i in counts:
        probs.append(i / len(values))

    probs_sums = [sum(probs[:e + 1]) for e in range(len(probs))]
    probs_sums = [np.round(item, 4) for item in probs_sums]
    unique_elements = sorted(unique_elements)

    dist_func_axis.plot([unique_elements[0] - step, unique_elements[0]], [0, 0], color='blue')
    dist_func_axis.plot([unique_elements[0], unique_elements[0]], [0, probs[0]], color='blue')
    dist_func_axis.plot(unique_elements, probs_sums, drawstyle='steps', color='blue')
    dist_func_axis.plot([unique_elements[-1], max_value + step], [1, 1], color='blue')
    dist_func_range = np.arange(min_value - step, max_value + step)
    dist_func_axis.plot(dist_func_range, norm.cdf(dist_func_range, avg, standard_deviation),
                        color='red', label='Функция распределения')
    configure(dist_func_axis, 'Фукнция распределения', 'Интервалы', 'Вероятность попасть левее')


def build_dist_polygon(dist_poly_axis, values):
    dist_poly_axis.scatter(np.arange(0, len(values)), values)
    configure(dist_poly_axis, 'Полигон распределения', 'Индексы', 'Данные')


def build_box_plot(box_plot_axis, values):
    box_plot_axis.boxplot(values)
    configure(box_plot_axis, 'Box Plot', '', 'Данные')
