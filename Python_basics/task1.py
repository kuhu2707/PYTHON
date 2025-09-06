#TASK 1 -WRITE A PYTHON SCRIPT AND CREATE 3 FUNCTIONS AND PASSING VALUES IN EACH OTHER AND SHOW THE RESULT.

def add(x,y):
    return x+y

def multiply(x):
    return x*2

def divide(x,y):
    return x/y

def show_result(x,y):
    sum_result = add(x,y)
    multiply_result = multiply(sum_result)
    result = divide(multiply_result,y)
    print("Final Result is: " , result)
    
show_result(15,3)