# Source data - 2D array to store electricity consumption matrix
electricity_matrix = [
    [50, 120, 250],
    [80, 150, 280],
    [110, 180, 310]
]

# Function to calculate and display cost for slab 1
def costSlab1():
    unit_cost = 10
    slab_units = electricity_matrix[0]
    total_cost = sum(unit * unit_cost for unit in slab_units)
    print(f"Total cost for Slab 1: Rs. {total_cost}")

# Function to calculate and display cost for slab 2
def costSlab2():
    unit_cost = 15
    slab_units = electricity_matrix[1]
    total_cost = sum(unit * unit_cost for unit in slab_units)
    print(f"Total cost for Slab 2: Rs. {total_cost}")

# Function to calculate and display cost for slab 3
def costSlab3():
    unit_cost = 20
    slab_units = electricity_matrix[2]
    total_cost = sum(unit * unit_cost for unit in slab_units)
    print(f"Total cost for Slab 3: Rs. {total_cost}")

# Main menu
while True:
    student_id = input("Enter student's ID: ")
    print("\nMenu:")
    print("1. Display the bill of slab 1 and slab 2")
    print("2. Display the bill of slab 3")
    print("Any other key to exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        costSlab1()
        costSlab2()
    elif choice == '2':
        costSlab3()
    else:
        print("Program terminated.")
        break