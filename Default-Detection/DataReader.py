

jobType = {'admin': 0,
           'blue-collar':1,
           'entrepreneur':2,
           'housemaid':3,
           'management':4,
           'retired':5,
           'self-employed':6,
           'services':7,
           'student':8,
           'technician':9,
           'unemployed':10,
           'unknown':11}

maritalStatus = {}

education = {}

numericalData = []

filename = 'bank-marketing-data/bank-additional-full.csv'

file = open(filename, 'r')
headers = file.readline().split(';')
print(headers)

for header in headers:
    

data = file.readlines()


for line in data:
    


    
    
    
    
    


