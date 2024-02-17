# Demonstrates recursive algorithm. 
# Each time the function is called it prints the first i
# i begins at 1.

# The issue with the below code is that it would run infinitley.

#def the_function(i):
    #print(i)
    #the_function(i + 1)
    #return

#the_function(1)

# To prevent this we need what is called a base case.
# Base case are conditions at the start of recursive functions
# that terminate calls.

# Runs until 10.
def the_function(i):
    if i > 10:
        return

    print(i)
    the_function(i + 1)
    return

the_function(1)

