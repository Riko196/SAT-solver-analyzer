from matplotlib import pyplot as plt

class Graph:
    def __init__(self, iterations, times):
        self.iterations = iterations
        self.times = times

    def render(self):
        plt.title("SAT-solver computing time")
        plt.plot(self.iterations, self.times)
        plt.show()
