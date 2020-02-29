# 032 - Ask for the radius and the depth of a cylinder and work out the total volume (circle area*depth)
# rounded to three decimal places.

import math
def cylinder():
    radius = int(input("Enter radius: "))
    depth = int(input("Enter depth: "))

    print(round(math.pi * radius**2 * depth,3))




cylinder()
