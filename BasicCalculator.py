from add import add
from subtract import subtract
from multiply import multiply
from Division import divide
from remainder import modulus

import sys

def  Calculator():
    print("************MAIN MENU**************")
    print()

    choice = int(input("""
                      1: Addition
                      2: Subtraction
                      3: Division
                      4: Multiplication
                      5: Remainder
                      6: Quit/log out
                      
                      Please enter your choice: """))
    if choice == 1:
        add()
    elif choice == 2:
        subtract()
    elif choice == 3:
        divide()
    elif choice == 4:
        multiply()
    elif choice == 5:
        modulus()
    elif choice == 6:
        sys.exit
    else:
        print("You must only select either 1,2,3,4,5, or 6.")
        print("Please try again")
        Calculator()

Calculator()