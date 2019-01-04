"""
Assignment #3 : Function to check equality of three parameters and return 'True'
if two or more parametrers are same and return 'False' if none of the parameters
are equal. [Note : if a parameter is a string and contains a numeric value,
it should be consider as valid parameter for comparison]
"""

# The function checkEquality crated for parameters comparison
def checkEquality(param1,param2,param3):
    param1 = int(param1);param2 = int(param2);param3 = int(param3)
    if(param1 == param2 == param3 or param1 == param2 or param1 == param3 or param2 == param3):
        return True
    else:
        return False

#Print different scenarios.

# All three parameters are different. Output is : False
print(checkEquality(1,3,4))

# All three parameters are equal. Output is : True
print(checkEquality(3,3,3))

# Two parameters are equal. Output is : True
print(checkEquality(3,3,5))

"""Two parameters are number and one parameter is string which contains numeric value.
 All three values are different. Output is : False"""
print(checkEquality("1",3,5))

"""Two parameters are number and one parameter is string which contains numeric value.
 Two values are Equal. Output is : True"""
print(checkEquality("1",1,5))



