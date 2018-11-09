#locals() is used for getting all local variables

for i in range(4):
    name='v'+str(i)
    locals()['v'+str(i)]=i

print v1,v2,v3
#[out]: 1,2,3


'''
Note: The built-in functions globals() and locals() return the 
current global and local dictionary, respectively,
which may be useful to pass around for use as 
the second and third argument to exec(). 
'''

#exec() function is similar with eval(),This function supports dynamic execution of Python code.
