from trigonometry.trigonometry_calculator import TrigonometryCalculator
from utils.common import clear_screen

def main_menu():
    """Displays the main menu and handles user input."""
    while True:
        clear_screen()
        print("\n================== Calculus Calculator ==================")
        print("1. Trigonometry Calculator")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            trigonometry_menu()
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def trigonometry_menu():
    """Displays the trigonometry calculator menu and handles user input."""
    trig_calculator = TrigonometryCalculator()

    while True:
        clear_screen()
        print("\n================== Trigonometry Calculator ==================")
        print("1. Calculate triangle")
        print("2. Back to main menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            angle_A = float(input("Enter angle A (in degrees): "))
            side_a = float(input("Enter side a: "))
            side_c = float(input("Enter side c: "))
            trig_calculator.calculate_triangle(angle_A, side_a, side_c)
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
