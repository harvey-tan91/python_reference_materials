#%%
# Start of script # this script is stored in "calc.py"
def add(x,y):
    return x + y

def substract(x,y):
    return x - y

def mutiply(x,y):
    return x * y 

def divide(x,y):
    if y == 0:
        raise ValueError('You cannot divide by zero')
    return x / y
# End of script

#%%
import unittest
import calc
# the normal convention for naming test file is as follows: test_xxxx.py

# to conduct test cases, we need to create a test class inherited from the unittest.TestCase
class testcalc(unittest.TestCase): 
    
    # we will need to write a method and MUST start with test_
    # then following by the function that we want to test
    def test_add(self): 
        # result = calc.add(10,5) # calc is the name of the py file that we imported at the top and add is the function in calc.py
        self.assertEqual(calc.add(10,5), 15)
        self.assertEqual(calc.add(-1,1), 0)
        self.assertEqual(calc.add(-1,-1), -2)

    # each method equals to one test result when we run the test file
    # when any of the test cases in the method fails the testing, it render the entire case as fail even if the rest of the case passes

    def test_substract(self): 
        # result = calc.add(10,5) # calc is the name of the py file that we imported at the top and add is the function in calc.py
        self.assertEqual(calc.substract(10,5), 5)
        self.assertEqual(calc.substract(-1,1), -2)
        self.assertEqual(calc.substract(-1,-1), 0)

    def test_mutiply(self): 
        # result = calc.add(10,5) # calc is the name of the py file that we imported at the top and add is the function in calc.py
        self.assertEqual(calc.mutiply(10,5), 50)
        self.assertEqual(calc.mutiply(-1,1), -1)
        self.assertEqual(calc.mutiply(-1,-1), 1)

    def test_divide(self): 
        # result = calc.add(10,5) # calc is the name of the py file that we imported at the top and add is the function in calc.py
        self.assertEqual(calc.divide(10,5), 2)
        self.assertEqual(calc.divide(-1,1), -1)
        self.assertEqual(calc.divide(-1,-1), 1)
        self.assertEqual(calc.divide(5,2), 2.5) # this ensure that we catch floor division


        # Writing test cases for exception handling
        self.assertRaises(ValueError, calc.divide, 10, 0)
        # 1st arg ---> the type of error we expect
        # 2rd arg ---> the function
        # 3rd and 4th arg ---> agruements for the test cases

        with self.assertRaises(ValueError): # this is the alternative method of writing the above 
            calc.divide(10,0)

if __name__ == '__main__':
    unittest.main()
