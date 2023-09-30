#The Head of Computing at the University of Poppleton is tasked with dividing a
#group of students into lab groups. A lab group is 24 students, since this is the
#number of PCs in a lab. Write a program that calculates how many groups are
#needed for the following number of students: 113, 175, 12. Display how many full
#groups there will be, and how many students will be in the smaller "left over" group

import math

labGroup = 24
group1 = 113
group2 = 175
group3 = 12

group1Remainder = group1 % labGroup 
group1Labs = group1/labGroup
group2Remainder = group2 % labGroup
group2Labs = group2/labGroup
group3Remainder = group3 % labGroup
group3Labs = group3/labGroup

print(group1Remainder,math.ceil(group1Labs))

print("Group 1 contains ",group1," students. This results in",math.ceil(group1Labs),"rooms required, with the smaller left over lab group containing",group1Remainder,"students.")
print("Group 2 contains ",group2," students. This results in",math.ceil(group2Labs),"rooms required, with the smaller left over lab group containing",group2Remainder,"students.")
print("Group 3 contains ",group3," students. This results in",math.ceil(group3Labs),"rooms required, with the smaller left over lab group containing",group3Remainder,"students.")

