from random import randint
import math
import statistics
class stdev():
    def __init__(self): #this is the constructor which will help to declare the variables
        self.lower_range = 0
        self.higher_range = 0
        self.num_list = []
        self.mean = 0
        self.list_len = 0
        self.list_sum = 0
        self.mean_square_list = []
        self.mean_square = 0
        self.SquaredDifferencesMean = 0
        self.setRange()
    def setRange(self): #this function will set the range for list
        self.higher_range = randint(1,125)
        self.lower_range = randint(1,125)
        self.compareRange()
    def compareRange(self): #this will compare the range
         if self.lower_range == self.higher_range:
             self.setRange()
         elif self.lower_range >= self.higher_range:
             self.setRange()
         else:
            self.num_list = list(range(self.lower_range,self.higher_range))
            print(self.num_list)
            self.calculateMean()
    def calculateMean(self):
         self.list_len = len(self.num_list)
         self.list_sum = sum(self.num_list)
         self.mean = self.list_sum/self.list_len
         #print("Mean of the numbers are:",self.mean)
         self.calculateSquaredDifferences()
    def calculateSquaredDifferences(self):
        for elements in self.num_list:
            self.mean_square = (float(elements) - self.mean)**2
            self.mean_square_list.append(self.mean_square)
        #print(self.mean_square_list)
        self.calculateSquaredDifferencesMean()
    def calculateSquaredDifferencesMean(self):
        self.SquaredDifferencesMean = (sum(self.mean_square_list))/(len(self.mean_square_list))
        #print(self.SquaredDifferencesMean)
        print('standard deviation of the entered numbers are with out using pre defined functions: ',math.sqrt(self.SquaredDifferencesMean))
        print('standard deviation of the entered numbers are: ',statistics.stdev(self.num_list))
obj = stdev()
