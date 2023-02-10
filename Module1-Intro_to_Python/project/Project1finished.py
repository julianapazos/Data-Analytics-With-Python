"""
Project 1 
This file contains the Max(), Min(), average(), that calculate this parameters on different columns of a file. It also contains the functions MaxWilderness(), MinWilderness(), averageWilderness() to calculate the parameters for each wilderness area. 

Author: Juliana Pazos (working in collaboration with Jonah Hart)

Default command line: (assuming both files are on the same folder)

    python project1finished.py covtype.data

"""

#Constants determining the different wilderness areas and their associated codes (keys)
AREAS = {
    0: 'All',
    1: 'Rawah Wilderness Area',
    2: 'Neota Wilderness Area',
    3: 'Comanche Peak Wilderness Area',
    4: 'Cache la Poudre Wilderness Area'
}

#Constants associating the different columns names (values) and their column number (keys)

COLUMNS = {
    0: 'Elevation',
    1: 'Aspect',
    2: 'Slope',
    3: 'Horizontal_Distance_To_Hydrology',
    4: 'Vertical_Distance_To_Hydrology',
    5: 'Horizontal_Distance_To_Roadways',
    6: 'Hillshade_9am',
    7: 'Hillshade_Noon',
    8: 'Hillshade_3pm',
    9: 'Horizontal_Distance_To_Fire_Points'
}




#Import of the module sys and object argv
from sys import argv


#Function for obtaining maximums
def Max(x):
    """
    This function works for identifying the maximum value of each column. x represents the desired column to analize
    
    Parameters: 
        x: integer. Stablishes the column from the dataset that is dessired to analyze
    
    Returns: 
        value1: The maximum value obtained for that column
    """
    #Working with argv object and opening data file
    script, data_file=argv
    data= open(data_file)
    #Seting up initial value of zero, that will be constantly changing through the loop
    value1=0
    for loopline in data: 
        #Loop for reading the lines and identifying the maximums. Every value is compared to value1 which will be 
        #storing the temporary maximum value (until another larger value appears)
        dataSplit=loopline.strip().split(",")
        if float(dataSplit[x])>value1:
            value1=float(dataSplit[x])
        else:
            continue
    return value1
    data.close()
    


#Minimum function
def Min(x):
    """
    This function works for identifying the minimum value of each column. x represents the desired column to analize
    
    Parameters: 
        x: integer. Stablishes the column from the dataset that is dessired to analyze
    
    Returns: 
        value1: The minimum value obtained for that column 
    """
    #Working with argv object and opening data file
    script, data_file=argv
    data= open(data_file)
    #Seting up initial value, that will be constantly changing through the loop
    value1=Max(x)
    for loopline in data: 
        #Loop for reading the lines and identifying the minimum. Every value is compared to value1 which will be 
        #storing the temporary minimum value (until another smaller value appears)
        #The initial value is the maximum given that it is known that the minimum is smaller than that
        dataSplit=loopline.strip().split(",")
        if float(dataSplit[x])<value1:
            value1=float(dataSplit[x])
        else:
                continue
    return value1
    data.close()
    


def average(x):
    """
    This function works for calculating the average value of each column. x represents the desired column to analize
    
    Parameters: 
        x: integer. Stablishes the column from the dataset that is dessired to analyze
    
    Returns: 
        Average: The average value obtained for that column
    """
        #Working with argv object and opening data file
    script, data_file=argv
    data= open(data_file)
    #Seting up initial value for the sum (denominator) and the length (numerator), that will be constantly changing through the loop
    partial=0
    length=0
    for loopline in data: 
        #Loop for reading the lines and calculating the averages. The partial variable will be storing the partial sum
        #of all the values, while the length will be contabilizing how much values were already summed, 
        #in order to get a final count of all the values in the column
        dataSplit=loopline.strip().split(",")
        partial=partial+float(dataSplit[x])
        length=length+1
    #Calculation of the average
    Average=partial/length
    return Average
    data.close()
    
def MaxWilderness(x):
    """
    This function works for calculating the maximum value of each aspect of each wilderness area . x represents the desired column to analize
    
    Parameters: 
        x: integer. Stablishes the column from the dataset that is dessired to analyze
    
    Returns: 
        value1, value2, value3, value4: The maximum value of Rawah Wilderness Area, Neota Wilderness Area, Comanche Peak Wilderness Area and Cache la Poudre Wilderness Area
    """     
        
    script, data_file=argv
    data= open(data_file)
    #Seting up initial value of zero, that will be constantly changing through the loop, for each wilderness area
    value1=0
    value2=0
    value3=0
    value4=0
    for loopline in data:
        #Loop for reading the lines. 
        #Filtering the columns that stablish the wilderness area to identify to which wilderness area each line belongs to.
        #Once identified the wilderness area it will loop in order to find the max for each wilderness area
        #Every value is compared to valuex (according to area) which will be storing the temporary maximum value (until another larger value appears)
        dataSplit=loopline.strip().split(",")
        if float(dataSplit[10])==1 and float(dataSplit[x])>value1:
            value1=float(dataSplit[x])
        elif float(dataSplit[11])==1 and float(dataSplit[x])>value2:
            value2=float(dataSplit[x])
        elif float(dataSplit[12])==1 and float(dataSplit[x])>value3:
            value3=float(dataSplit[x])
        elif float(dataSplit[13])==1 and float(dataSplit[x])>value4:
            value4=float(dataSplit[x])
        
    
    return [value1, value2, value3, value4]
    data.close()

def MinWilderness(x):
    """
    This function works for calculating the minimum value of each aspect of each wilderness area . x represents the desired column to analize
    
    Parameters: 
        x: integer. Stablishes the column from the dataset that is dessired to analyze
    
    Returns: 
        value1, value2, value3, value4: The minimum value of Rawah Wilderness Area, Neota Wilderness Area, Comanche Peak Wilderness Area and Cache la Poudre Wilderness Area
    """   
    script, data_file=argv
    data= open(data_file)
    #Seting up initial value of infinite, that will be constantly changing through the loop, for each wilderness area
    value1=float("inf")
    value2=float("inf")
    value3=float("inf")
    value4=float("inf")
    for loopline in data: 
        #Loop for reading the lines. 
        #Filtering the columns that stablish the wilderness area to identify to which wilderness area each line belongs to.
        #Once identified the wilderness area it will loop in order to find the min for each wilderness area
        #Every value is compared to valuex (according to area) which will be storing the temporary minimum value (until another smaller value appears)
        dataSplit=loopline.strip().split(",")
        if float(dataSplit[10])==1 and float(dataSplit[x])<value1:
            value1=float(dataSplit[x])
        elif float(dataSplit[11])==1 and float(dataSplit[x])<value2:
            value2=float(dataSplit[x])
        elif float(dataSplit[12])==1 and float(dataSplit[x])<value3:
            value3=float(dataSplit[x])
        elif float(dataSplit[13])==1 and float(dataSplit[x])<value4:
            value4=float(dataSplit[x])
    return [value1, value2, value3, value4]
    data.close()



def averageWilderness(x):
    """
    This function works for calculating the average value of each aspect of each wilderness area . x represents the desired column to analize
    
    Parameters: 
        x: integer. Stablishes the column from the dataset that is dessired to analyze
    
    Returns: 
        Average1, Average2, Average3, Average4: The average value of Rawah Wilderness Area, Neota Wilderness Area, Comanche Peak Wilderness Area and Cache la Poudre Wilderness Area
    """ 
    script, data_file=argv
    data= open(data_file)
    #Seting up initial value for partial sums and length, that will be constantly changing through the loop, for each wilderness area
    partial1=0
    length1=0
    partial2=0
    length2=0
    partial3=0
    length3=0
    partial4=0
    length4=0
    for loopline in data: 
        #Loop for reading the lines. 
        #Filtering the columns that stablish the wilderness area to identify to which wilderness area each line belongs to.
        #Once identified the wilderness area it will loop making a sum of each column for each wilderness area and counting all the values summed
    
        dataSplit=loopline.strip().split(",")
        if float(dataSplit[10])==1:
            partial1=partial1+float(dataSplit[x])
            length1=length1+1
        elif float(dataSplit[11])==1:
            partial2=partial2+float(dataSplit[x])
            length2=length2+1
        elif float(dataSplit[12])==1:
            partial3=partial3+float(dataSplit[x])
            length3=length3+1
        elif float(dataSplit[13])==1:
            partial4=partial4+float(dataSplit[x])
            length4=length4+1
    #Calculation of the average of each wilderness area    
    Average1=partial1/length1
    Average2=partial2/length2
    Average3=partial3/length3
    Average4=partial4/length4
    return [Average1, Average2, Average3, Average4]
    data.close()


def main():
    
    #Create a file to store results
    Results_file=open("ResultsFile.txt", "w")
    #Printing the results by using a loop, using the previously created functions in order to evaluate all the columns
    for x in range (0,10):
        col_max=Max(x)
        col_min=Min(x)
        col_average=average(x)
        print("Maximum", COLUMNS[x], "is {}".format(col_max), file=Results_file)
        print("Minimum", COLUMNS[x], "is {}".format(col_min), file=Results_file) 
        print("Average", COLUMNS[x], "is {}\r\n".format(col_average), file=Results_file)
    
    for x in range(0,10):
        #Printing the results by using a loop, using the previously created functions in order to evaluate all the columns
        wilderness_max= MaxWilderness(x)
        wilderness_min= MinWilderness(x)
        wilderness_avg = averageWilderness(x)
        print(AREAS[1], f"Maximum {COLUMNS[x]} is {wilderness_max[0]}" , "\r\n" , AREAS[2], f"Maximum {COLUMNS[x]} is {wilderness_max[1]}", "\r\n" , AREAS[3], f"Maximum {COLUMNS[x]} is {wilderness_max[2]}", "\r\n" , AREAS[4], f"Maximum {COLUMNS[x]} is {wilderness_max[3]}", "\r\n", file=Results_file)
        print(AREAS[1], f"Minimum {COLUMNS[x]} is {wilderness_min[0]}", "\r\n" ,AREAS[2], f"Minimum {COLUMNS[x]} is {wilderness_min[1]}", "\r\n" , AREAS[3], f"Minimum {COLUMNS[x]} is {wilderness_min[2]}", "\r\n" ,AREAS[4], f"Minimum {COLUMNS[x]} is {wilderness_min[3]}", "\r\n", file=Results_file)
        print (AREAS[1], f"Average {COLUMNS[x]} is {wilderness_avg[0]}", "\r\n", AREAS[2], f"Average {COLUMNS[x]} is {wilderness_avg[1]}", "\r\n" , AREAS[3], f"Minimum {COLUMNS[x]} is {wilderness_avg[2]}", "\r\n" , AREAS[4], f"Minimum {COLUMNS[x]} is {wilderness_avg[3]}","\r\n", file=Results_file)

    
if __name__ == "__main__":
    main()
    
