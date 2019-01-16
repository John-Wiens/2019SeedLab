import numpy as np

# Open the File
with open('datafile.txt','r') as f:
        #Read the file contents and convert to a list
        b = eval(f.read())
        data = np.array(b)

        minimum = data.min()
        maximum = data.max()

        #Calculate Min and Max
        print("Maximum: ", maximum)
        print("Minimum: ", minimum)

        #Calculate Data Frequency
        bin_count = np.bincount(data)
        print("Most Frequent:", bin_count.argmax())
        print("Number of Occurences:", bin_count.max())
	
        #Calculate Other Parameters
        print("38 is Located at: ",b.index(38))
        data = np.sort(data)
        print("Sorted",data)
        print("Evens:",data[data % 2 ==0])
        print("Evens: ", [data[k] for k in data if data[k]%2 ==0])
f.close

