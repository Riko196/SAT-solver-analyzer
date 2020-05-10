from matplotlib import pyplot
from pandas import DataFrame

class Bar:
    def __init__(self, arangeData1, data1, arangeData2, data2, xticks, labelx):
        self.arangeData1 = arangeData1
        self.data1 = data1
        self.arangeData2 = arangeData2
        self.data2 = data2
        self.xticks = xticks
        self.labelx = labelx

    def render(self):
        pyplot.bar(self.arangeData1, self.data1, width = 0.2, color = 'blue')

        if len(self.arangeData2) != 0:
            pyplot.bar(self.arangeData2, self.data2, width = 0.2, color = 'red')

        pyplot.xticks(self.arangeData1, self.xticks)
        pyplot.xlabel(self.labelx)
        pyplot.ylabel('Times(s)')

        pyplot.show()
