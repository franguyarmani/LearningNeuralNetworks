# time period of volatility will be a week in which the high and low are 5% apart
#volatility occurs in the next 7 days
import numpy as np



highVol = 0
highValue = 0

def ImportData(file):
    f = open(file, 'r')
    return f.readlines()[1:]

def AddFields(List):
    toArray = []
    for x in List:
        y = [float(i) for i in x.split(',')[1:]] #convert all values to floats + exclude headers
        y.append(y[3]-y[0]) #add intra day change
        toArray.append(y)
    return toArray

Array = AddFields(ImportData("daily_.DJI.csv"))


def ComputeType(arr, H):
    labels = []
    for x in range(len(arr)):
        updateGlobals(arr[x])
        if isNextWeekVolatile(x,arr,H):
            #print(arr[x])
            labels.append([1,0])
            #print(arr[x])

        else:
            #print(arr[x])
            labels.append([0,1])
            #print(arr[x])
        #print(arr[x])
    return labels

def ScaleValues(arr):
    global highValue
    global highVol
    for x in range(len(arr)):
        arr[x][0:4] = [y/highValue for y in arr[x][0:4]]
        arr[x][4] = arr[x][4]/highVol
    return arr
        
    

def updateGlobals(line):
    global highValue
    global highVol
    if line[1] > highValue:
        highValue = line[1]
    if line[4] > highVol:
        highVol = line[4]
        

def isNextWeekVolatile(i, arr, H): #i is the index of the current day
    high = 0.0
    low = 100000000.0 #a vakue that is hopefully higher than any value that will be encountered
    for y in range(7): #iterate through to next 7 days
        if arr[abs(i-y-H)][1] > high: 
            high = arr[abs(i-y-H)][1]
        if arr[abs(i-y-H)][2] < low:
            low = arr[abs(i-y-H)][2]
        if (high - low)/high > 0.07:
            return True

    if (high - low) < 0:
        raise ValueError ('Low should never be greater than high')
    return False

labels = np.array(ComputeType(Array, 10))
cleanData = np.array(ScaleValues(Array)).astype(np.uint8)


   

