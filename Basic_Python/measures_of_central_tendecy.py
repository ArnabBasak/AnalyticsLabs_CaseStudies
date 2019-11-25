#In this program will try to solve the measures of central tendency
from random import randint
from collections import Counter

#generating the random numbers
numbers = []
#lower_range = 0
#higher_range = 0

def input():
    lower_range = int(input('enter the lower range: '))
    print()
    higher_range = int(input('enter the higher range: '))

def creatingnumbers():
    for _ in range(lower_range,higher_range):
        if lower_range < higher_range:
            print('lower_range is higher than higher range invalid input please enter again')
            input()
        value = randint(1,999)
        numbers.append(value)

def viewingnumbers():
#viewing the generated numbers
    print()
    print("Total how many numbers are there",len(numbers))
    print()
    print("Sum of the total numbers",sum(numbers))
    print()
    print("Numbers generated as per user input",numbers)
    print()

def creatingmean():
    #calculating the mean
    print('mean of the given number is',sum(numbers)/(len(numbers)))

def creatingmedian():
    #calculating the medi#calculating the mearnan
    numbers.sort()
    if len(numbers) % 2 == 0:
        median1 = numbers[len(numbers)//2]
        median2 = numbers[len(numbers)//2-1]
        median = (median1+median2)/2
        print(median1)
        print(median2)
    else:
        median = numbers[len(numbers)//2]
    print("Median is",median)

def creatingmode():
    #calculating the mode
    data = Counter(numbers)
    get_mode = dict(data)
    mode = [k for k,v in get_mode.items() if v == max(list(data.values()))]
    if len(mode) == len(numbers):
        get_mode = "No mode found"
        print(get_mode)
    else:
        print("Mode is / are: " + ', '.join(map(str, mode)))

input()
creatingnumbers()
viewingnumbers()
creatingmean()
creatingmedian()
creatingmode()
