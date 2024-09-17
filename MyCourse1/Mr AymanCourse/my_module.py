import math

# Function to calculate the area of a circle and the volume of a sphere
def circle_and_sphere_calculations(radius):
    area_of_circle = math.pi * radius ** 2
    volume_of_sphere = (4/3) * math.pi * radius ** 3
    return area_of_circle, volume_of_sphere

# Prompt the user to enter the radius
radius = float(input("Enter the radius: "))

# Calculate the area of the circle and the volume of the sphere
area, volume = circle_and_sphere_calculations(radius)

# Display the results
print(f"The area of the circle with radius {radius} is {area}")
print(f"The volume of the sphere with radius {radius} is {volume}")
