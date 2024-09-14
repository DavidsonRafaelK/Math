import multiprocessing
from basic_aritmethic.multiplication import perkalian
from basic_aritmethic.division import pembagian
from basic_aritmethic.addition import pertambahan
from basic_aritmethic.substraction import pengurangan

def run_operation(operation, num1, num2):
    """Function to run a given operation with two numbers"""
    operation(num1, num2)

def main():
    while True:
        print("Select an option:")
        print("1. Basic Arithmetic")
        print("2. Exit")
        
        choice = input("Enter your choice (1/2): ")
        
        if choice == '1':   
            print("\nBasic Arithmetic Operations:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            sub_choice = input("Enter your choice (1-4): ")
            
            operations = {
                '1': pertambahan,
                '2': pengurangan,
                '3': perkalian,
                '4': pembagian
            }
            
            operation = operations.get(sub_choice)
            
            if operation:
                num1 = float(input('Add the first number to calculate: '))
                num2 = float(input('Add the second number to calculate: '))
                
                # Create a process for each operation (for demonstration)
                process = multiprocessing.Process(target=run_operation, args=(operation, num1, num2))
                process.start()
                process.join()
            else:
                print("Invalid choice. Please select a number between 1 and 4.")
        
        elif choice == '2':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    import os
    print(f"CPU Count: {os.cpu_count()}")  # Display the number of CPUs
    main()
