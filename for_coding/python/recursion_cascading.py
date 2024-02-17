# Understand this about recursion.
# Calls can cascade ontop of one another, 
# it doesn't just iterate top down line by line.

def the_function(i):
    if i >  4: 
        return 

    print(i) 
    the_function(i + 1) #
    print(f"End call where i = {i}") #
    return 

the_function(1)

# When the above code is ran, the print text is executed 
# in reverse.
