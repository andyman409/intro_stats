import numpy
from matplotlib import pyplot as plt
import stats_module_3 as s3


def plot_points(x_values, y_values):
    array = []
    for i in range(len(x_values)):
        array.append([x_values[i], y_values[i]])
    data = numpy.asarray(array)
    x, y = data.T
    plt.scatter(x,y)
    plt.show()
    pass
