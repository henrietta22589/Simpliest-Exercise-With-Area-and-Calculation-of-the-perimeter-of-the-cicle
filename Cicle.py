'''
This programm will calculate the area and the perimeter of a cicle. The perimeter of the cicle can be calculated by the type:2*p*radius_of_The_Cicle and
the area of the cicle can be calculated from the type:p*(r*r)
'''
'''
Because every input value the user gives us, is a string. For this  reason, we are making this conversion to a float--
radius_of_The_Cicle=float(input("Give me the radius of the cicle\n"))
'''
radius_of_The_Cicle=float(input("Give me the radius of the cicle\n"))
'''We define Π=3.14 as a const '''
pi=3.14
print("The radius of the cicle is:")
print(radius_of_The_Cicle)
'''Calculate of the perimeter '''
perimeter=2*pi*radius_of_The_Cicle
print("The perimeter of the cicle is:")
print(perimeter)
'''Calculate of the area '''
area=pi*(radius_of_The_Cicle*radius_of_The_Cicle)
print("The are of a cicle is")
print(area)