# time period of volatility will be a week in which the high and low are 5% apart
#volatility occurs in the next 7 days
import numpy as np


def ImportData(file):
    f = open(file, 'r')
    return f.readlines()


rawData = ImportData("daily_.DJI.csv")[1:]
 
toArray = []
for x in rawData:
    y = [float(i) for i in x.split(',')[1:]] #convert all values to floats
    y.append(y[4]-y[1]) #add intra day change
    y.apendd 
    toArray.append(y)


for x in toArray:
    for y in x:
        




Array = np.array(toArray)

print(Array.shape)
print(Array[1])

   

    
    
    
