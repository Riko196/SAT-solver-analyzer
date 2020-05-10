from matplotlib import pyplot
from pandas import DataFrame

class Graph:
    def __init__(self, iterations, averages, maximums, title):
        self.iterations = iterations
        self.averages = averages
        self.maximums = maximums
        self.title = title

    def render(self):
        data = DataFrame({'Iteration': self.iterations, 'Average': self.averages, 'Maximum': self.maximums})
        pyplot.title(self.title)

        pyplot.plot('Iteration', 'Average', data=data, color='blue')
        pyplot.plot('Iteration', 'Maximum', data=data, color='black')

        pyplot.xlabel('Iteration')
        pyplot.ylabel('Time(s)')

        pyplot.legend()
        pyplot.show()
