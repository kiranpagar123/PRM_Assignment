# Your task is to complete the validate_triangle and the validate_rectangle functions for 
# the classes. Hint for validating is given in the comments of the code. Also you will 
# have to fill the following after validation in respective functions:


class Triangle:
    def __init__(self, sides):
        self.sides = sides

    def validate_triangle(self):
        a, b, c = self.sides
        if a + b > c and b + c > a and c + a > b:
            return "Valid Triangle"
        else:
            return "Invalid Triangle"

class Rectangle:
    def __init__(self, sides):
        self.sides = sides

    def validate_rectangle(self):
        a, b, c, d = self.sides
        if a == c and b == d:
            return "Valid Rectangle"
        else:
            return "Invalid Rectangle"

triangle_sides = input("Enter the sides of the triangle (space-separated): ")
triangle_sides = list(map(int, triangle_sides.split()))

rectangle_sides = input("Enter the sides of the rectangle (space-separated, in the format 'l b l b'): ")
rectangle_sides = list(map(int, rectangle_sides.split()))

triangle = Triangle(triangle_sides)
triangle_validation_result = triangle.validate_triangle()
print(triangle_validation_result)

rectangle = Rectangle(rectangle_sides)
rectangle_validation_result = rectangle.validate_rectangle()
print(rectangle_validation_result)


# Output:-

# Enter the sides of the triangle (space-separated): 4 3 5
# Enter the sides of the rectangle (space-separated, in the format 'l b l b'): 2 4 2 4

# Valid Triangle
# Valid Rectangle