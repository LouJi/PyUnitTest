from math import pi

def circle_area(r):
    return pi*(r**2)

#Test Function
'''
radii = [2, 0, -3, 2+5j, True, "Hello"]
message = 'Area of circles with r = {radius} is {area}.'

for r in radii:
    A= circle_area(r)
    print(message.format(radius=r, area=A))

'''
#Same as function that is commented out
radii = [2, 0, -3, 2+5j, True, "Hello"]


for r in radii:
    A= circle_area(r)
    message = f'Area of circles with r = {r} is {A}.'
    print(message) #.format(radius=r, area=A))
    
