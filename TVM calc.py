# In my attempts to use different time value of money calculators I began to struggle with their U.I.'s.
# Because of this I have been working on this calculator to simplify the U.I.
from math import e
# initialize variables
menu1 = 1
menu2a = 1
menu2b = 1
print('\nWelcome to the Time Value of Money (TVM) calculator!')
while menu1 != 3:
    print('\nPlease select a option in the menu by typing its corresponding number!')
    print('1. Calculate the future value of an investment')
    print('2. Calculate the present value of an investment')
    print('3. Quit TVM program')
    # print('4. test menu')
    menu1 = int(input())
    # Future Values
    if menu1 == 1:
        print('Is your investment a lump sum or an annuity?')
        print('1. Lump Sum')
        print('2. Annuity')
        menu2a = int(input())
        if menu2a == 1:
            # Lump Sum
            annual_compounding = input("Does the investment compound annually? ")

            if annual_compounding == "yes":
                interest = float(input("What is the interest rate (enter 5% as 5)? "))
                time = float(input("How long is the investment (in years)? "))
                principal = float(input("What is the principal investment? $"))
                number_of_compounds = 1
                final_value = principal * (1 + ((interest / 100) * number_of_compounds)) ** (time * number_of_compounds)
                print(f"The investment after {time:.1f} years is ${final_value:.2f}")
                menu1 = 3

            elif annual_compounding == "no":
                # e_compounding = input("Does the investment compound continuously? ")
                # When "no" 
                # if e_compounding.capitalize() == "Yes":
                #     interest = float(input("What is the interest rate (enter 5% as 5)? "))
                #     time = float(input("How long is the investment (in years)? "))
                #     principal = float(input("What is the principal investment? $"))
                #     final_value = principal * e ** (interest / 100 * time)
                #     print(f"The investment after {time:.1f} years is ${final_value:.2f}"
                interest = float(input("What is the interest rate (enter 5% as 5)? "))
                time = float(input("How long is the investment (in years)? "))
                principal = float(input("What is the principal investment? $"))
                number_of_compounds = float(input("How many times does the investment compound annually? "))
                final_value = principal * (1 + ((interest / 100) * number_of_compounds)) ** (
                            time * number_of_compounds)
                print(f"The investment after {time:.1f} years is ${final_value:.2f}")
                # else:
                #     print("Please enter a valid option")
            else:
                print("Please enter a valid input")

        if menu2a == 2:
            # Annuity (future Value)
            annual_compounding = input("Does the investment compound annually? ")

            if annual_compounding.capitalize() == 'Yes':
                interest = float(input("What is the interest rate (enter 5% as 5)? "))
                time = float(input("How long is the investment (in years)? "))
                principal = float(input("What is the principal investment? $"))
                payment = float(input('What is the value of your payment? '))
                final_value = payment*((1 + (interest / 100)) ** time - 1) / (interest / 100)
                print(f'The investment after {time:.1f} years is ${final_value:.2f}')

            elif annual_compounding.capitalize() == 'No':
                interest = float(input("What is the interest rate (enter 5% as 5)? "))
                time = float(input("How long is the investment (in years)? "))
                principal = float(input("What is the principal investment? $"))
                payment = float(input('What is the value of your payment? '))
                number_of_compounds = float(input("How many times does your investment compound annually? "))
                final_value = principal * ((1 + (interest / 100) / number_of_compounds) ** (time * number_of_compounds)
                                           - 1) / ((interest / 100) / number_of_compounds)

                print(f'The investment after {time:.1f} years is ${final_value:.2f}')
        else:
            menu1=3

    # Present Values
    if menu1 == 2:
        print('Is your investment a lump sum or an annuity?')
        print('1. Lump Sum')
        print('2. Annuity')
        menu2b = int(input())
        # Lump Sum
        # Double check math
        if menu2b == 1:
            annual_compounding = input("Does the investment compound annually? ")

            if annual_compounding.capitalize() == 'Yes':
                future_value = float(input("How much will your investment be worth? "))
                interest = float(input("How much is the interest? "))
                time = float(input("How long will the investment be for? "))
                present_value = future_value * pow((1 + interest / 100), -time)
                print(f"To have investment worth {future_value:.2f} after {time:.1f} years you"
                      f" will have to invest {present_value:.2f} now.")

            elif annual_compounding.capitalize() == 'No':
                # e_compounding = input("Does the investment compound continuously? ")
                # if e_compounding.capitalize() == "no":
                    future_value = float(input("How much will your investment be worth? "))
                    interest = float(input("How much is the interest? "))
                    time = float(input("How long will the investment be for? "))
                    number_of_compounds = float(input("How many times will the investment compound annually? "))
                    present_value = future_value * (1 + (interest / 100) / number_of_compounds) \
                        ** -(time * number_of_compounds)
                    print(f"To have investment worth ${future_value:.1f} after {time:.1f} years you"
                          f" will have to invest ${present_value:.2f} now.")
                # elif e_compounding.capitalize() == 'yes':
                #     future_value = float(input("How much will your investment be worth? "))
                #     interest = float(input("How much is the interest? "))
                #     time = float(input("How long will the investment be for? "))
                #     present_value = future_value * pow(e, -(interest/100) * time)
                #     print(f"To have investment worth {future_value:.2f} after {time:.1f} years you"
                #           f" will have to invest {present_value:.2f} now.")

            else:
                print('Please enter a valid option')
        #         Present value of annuity
        elif menu2b == 2:
            annual_compounding = input("Does the investment compound annually? ")
            if annual_compounding.capitalize() == "Yes":
                future_value = float(input("How much will your investment be worth? "))
                interest = float(input("How much is the interest? "))
                time = float(input('How long will the investment be for? '))
                payment = float(input('What is the value of your payment? '))
                present_value_of_annuity = payment * (1 - ((1 + interest / 100) ** - time)) / (interest / 100)
                print(f"To have ${future_value:.2f} after {time:.1f} years you will have to invest"
                      f" ${present_value_of_annuity:.2f}")

            elif annual_compounding.capitalize() == "No":
                future_value = float(input("How much will your investment be worth? "))
                interest = float(input("How much is the interest? "))
                time = float(input("How long will the investment be for? "))
                payment = float(input('What is the value of your payment? '))
                present_value_of_annuity = payment * (1 - ((1 + interest / 100) ** - time)) / (interest / 100)
                print(f"To have ${future_value:.2f} after {time:.1f} you will have"
                      f" to invest ${present_value_of_annuity:.2f}")
            else:
                print('Please enter a valid input')
        else:
            print('Please enter a valid option')
else:
    print('\nThanks for using TVM calculator!')
