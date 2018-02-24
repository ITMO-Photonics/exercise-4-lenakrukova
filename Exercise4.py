
# coding: utf-8

# In[7]:



PI = 3.14    
def calculate(R, L):
    sa = 2 * PI * R * (R + L)
    volume = PI * R * R * L 
    return ('Surface area: ' +  str(sa),
            'Volume: ' +  str(volume))
    
    
radius = float(input('Please Enter the radius of a Cylinder: '))
length = float(input('Please Enter the length of a Cylinder: '))

print(calculate(radius, length))

