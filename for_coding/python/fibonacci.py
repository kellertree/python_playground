# Recursion is good when you want break down problems
# into subproblems. That you can than solve and use/combine
# the solutions to solve the original problem.


# In this function we are trying to solve what is 
# the nth Fibonacci number?
def F(n):
    if n <=1:
        return n
    
    oneBack = F(n - 1)
    twoBack = F(n - 2)

    return oneBack + twoBack

F(10)