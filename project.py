import math
import csv
from collections import Counter

with open('SOCR_HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)


data = file_data[0]

# function for mean :
def mean(data):
    n= len(data)
    total =0
    for x in data:
        total += int(x)

    mean = total / n
    return mean
new_data=[]

# function for mode
def mode(data):

    file_data.pop(0)

    
    for i in range(len(file_data)):
        n_num = file_data[i][1]
        new_data.append(n_num)



    #Calculating Mode
    data = Counter(new_data)
    mode_data_for_range = {
                            "75-85": 0,
                            "85-95": 0,
                            "95-105": 0
                        }
    for height, occurence in data.items():
        if 75 < float(height) < 85:
            mode_data_for_range["75-85"] += occurence
        elif 85 < float(height) < 95:
            mode_data_for_range["85-95"] += occurence
        elif 95 < float(height) < 105:
            mode_data_for_range["95-105"] += occurence

    mode_range, mode_occurence = 0, 0
    for range, occurence in mode_data_for_range.items():
        if occurence > mode_occurence:
            mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
    mode = float((mode_range[0] + mode_range[1]) / 2)
    
def median(data):
    for i in range(len(file_data)):
        n_number = file_data[i][1]
        new_data.append(float(n_number))

        n = len(new_data)
        new_data.sort()

        if n % 2 == 0 :
            median1 = float(new_data[n//2])
            median2 = float(new_data[n//2-1])
            median = (median1 + median2)/2

        else :
            median = new_data[n//2]

print("Median is: "+ str(median))
print("Mean is: "+ str(mean))
print("Mode is: "+ str(mode))
