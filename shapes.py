import turtle

# Set up the turtle graphics window
window = turtle.Screen()
window.setup(800, 600)

# Function to draw a square
def draw_square(size, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

# Function to draw a triangle
def draw_triangle(size, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()

# Function to draw a circle
def draw_circle(size, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

# Function to clear the drawing and start over
def clear_drawing():
    turtle.clear()

# Main program loop
while True:
    print("1. Draw Square")
    print("2. Draw Triangle")
    print("3. Draw Circle")
    print("4. Clear Drawing")
    print("5. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        size = int(input("Enter size of square: "))
        color = input("Enter color of square: ")
        draw_square(size, color)
    elif choice == "2":
        size = int(input("Enter size of triangle: "))
        color = input("Enter color of triangle: ")
        draw_triangle(size, color)
    elif choice == "3":
        size = int(input("Enter size of circle: "))
        color = input("Enter color of circle: ")
        draw_circle(size, color)
    elif choice == "4":
        clear_drawing()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

# Keep the turtle graphics window open
turtle.done()