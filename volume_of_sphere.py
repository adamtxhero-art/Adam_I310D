
import math

def calculate_volume_of_sphere(radius):
    return (4/3) * math.pi * radius**3

#used radii of 30 and 40 like the exersise said
radii = [30, 40]

for r in radii:
    volume = calculate_volume_of_sphere(r)
    print(f"Volume of sphere with radius {r} is: {volume}")
