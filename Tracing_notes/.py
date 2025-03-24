#print("i made this whole world up and i am the only real one here ")
#print("you know how to code thats so tuff :heartbreak: ")

#Aiden Challenger, Tracing Notes

#What is tracing?
# allows you to know where your functions are called and when they are called 
#lets you see what is happening with your functions 

# python -m trace --trace C:\Users\aiden.challenger\CP2-Projects\debugging_code.py
# python -m trace --count C:\Users\aiden.challenger\CP2-Projects\debugging_code.py
# python -m trace --listfuncs C:\Users\aiden.challenger\CP2-Projects\debugging_code.py
# python -m trace --trackcalls C:\Users\aiden.challenger\CP2-Projects\debugging_code.py
"""
--trace (displays function ines as they are executed )
--count (dispalys the number of times each function is executed )
--listfuncs (lists what functions you have)
--trackcalls(shows relations between functions )
"""
import sys 
import trace 

#tracer.run('sub(8,2)')


#What are some ways we can debug by tracing?
    #by creating a function that lets us see how our functions are interacting and running 


#How do you access the debugger in VS Code?
    #f5 or the play button in top right 

#What is testing?
    #

#What are boundary conditions?


#How do you handle when users give strange inputs?


def sub(num1,num2):
    print (num1, num2)


def add(num1,num2):
    sub(num1,num2)
    return num1+num2


print(add(5,4))



print(sub(5,4))

tracer = trace.Trace(count =False, trace=True )

tracer.run('sub(8,2)')
print(tracer)


import sys 
import trace 
tracer = trace.Trace(count =False, trace=True )
def trace_calls(frame,event,arg):
    if event =='call':
        print(f"Calling function {frame.f_code.co_name}")
    elif event == 'line':
        print(f'Executing line: {frame.f_lineno} in {frame.f_code.co_name}')
    elif event == 'return':
        print((f"{frame.f_code.co_name} returned {arg}"))
    elif event == 'exeception':
        print (f"Exeception in {frame.f_code.co_name} {arg}")
sys.settrace(trace_calls)

''''
Event type s 
call - when the function is called 
line -when ta new line is execute 
return -when the function returns a value 
exception - when there is an exception raised 

'''
