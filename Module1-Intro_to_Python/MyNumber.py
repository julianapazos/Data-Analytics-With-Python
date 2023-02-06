"""
This file creates the MyNumber class
This class that only works with integers, prints the sentence "The number is: ..." according to the numbers that are assigned to the functions. 
Author: Juliana Pazos


"""
class MyNumber:
     """
    This class stores a number and performs basic mathematics on the number.
    
    Attributes
    ----------
    x : int
        The number that this class works with.

    Methods
    -------
    print():
        Prints the number    
    add(y):
        Adds the number in y to the number of this object.
    subtract(y):
        Subtacts the number in y to the number of this object.
        """
    
    def __init__(self, x):
        """ Sets the condition of being an integer"""
        if not type(x) == int:
            raise Exception("Please provide an integer when using the MyNumber object")
        self.x = x
    """prints the value inside the sentence "the number is..""""
    def print(self):
        print("The number is: {}".format(self.x))
     """defines the add function, in which self and y are added"""   
    def add(self, y):
        self.x = self.x + y
    """defines the subtract action in which self and y are subtracted"""
    def subtract(self, y):
        self.x = self.x - y


def main():
    """sets the values for working inside MyNumber, but these are not global numbers, so they wont be applied whenever the class is ran in other files"""
    xval = 3
    yval = 2
    number = MyNumber(2)
    number.print()
    number.add(yval)
    number.print()
    number.subtract(yval)
    number.print()

if __name__ == "__main__":
    main()