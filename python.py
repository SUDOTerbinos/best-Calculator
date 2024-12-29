def calculator():
    print("Welcome to the Basic Calculator!")
    print("Available operations: +, -, *, /")
    
    while True:
        
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Enter the operation (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))
            
            
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Error: Division by zero is not allowed.")
                    continue
            else:
                print("Invalid operator. Please use +, -, *, or /.")
                continue
            
            print(f"The result {result}")
            
        except ValueError:
            print("Invalid input. Please enter numbers only.")
        
        
        again = input("Do you want to perform another calculation? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break

calculator()
