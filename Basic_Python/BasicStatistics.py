import statistics
numbers = list(range(101,1234))

def calculateMean():
    print("Mean is: ",statistics.mean(numbers))

def calculateMedian():
    print("Median is: ",statistics.median(numbers))

def calculateMode():
    num = [2,4,7,7,6,6,8,8,2,2]
    print("Mode is: ",statistics.mode(num))

def calculateStd():
    print("Standard Deviation: ",statistics.stdev(numbers))

def calculateMedianLow():
    print("Low median is: ",statistics.median_low(numbers))

def calculateMedianHigh():
    print("Median High is: ",statistics.median_high(numbers))


calculateMean()
calculateMedian()
calculateMode()
calculateStd()
calculateMedianLow()
calculateMedianHigh()