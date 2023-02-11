"""
This file contains the project 1 for the AFS 505 class Module 1. 

This assignments is done by Juliana Pazos

Default command line: 

python project1.py data_file

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

def main (): 
    """
    This function helps in importing the data file 
    
    Parameters
    ???
    
    Returns
    None
    """
    from sys import argv

    script, data_file=argv

    data= open(data_file)
    dataSplit=data.readline().strip().split()
    print(dataSplit)
    
    

    if __name__ == "__main__":
    main()








    
