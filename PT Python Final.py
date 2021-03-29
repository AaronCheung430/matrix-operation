#Created by 2595161 from Durham University Interntaional Study Centre
#Last editied on 2021/03/12 09:00 GMT
#Copyright © 2021 2595161. All rights reserved.
#Programming Techniques - Summative Assignment 1 v1.0

# import modules
import os
import time
import copy

# set up the lists for the text of numbers in English and the menu options
EngNum = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
menu_options = ["Create or Edit Matrix", "Matrix Addition", "Scalar Multiplication", "Product of Two Matrices", "Quit the Program"] 

# create empty lists to store the value for each matrix
first_matrix = []
second_matrix = []
result_matrix = []
empty_matrix = []

# set up boolean value, used to check if data entry is complete, and if is the matrices was checked
save_matrices = False
same_size_matrices = True
same_size_matrices_rc = True

# create variables for messages
valueError_message = "Oops! That was a text. Please try again with a valid number... \n"
welcome_message = "Welcome to the Matrix Operation Algorithms. \nPlease type the number below."
invalid_message = ""
user_choice = ""

# to display the time delay animation
def time_animation(t):
    for i in range(t):
        time.sleep(1)
        print(".")

# to countdown, get parameters about how many seconds is the countdown going to run, and the message that will show.
def countdown(s, message = "Returning to main menu in"): 
    
    # print countdown on the same line, until s is 0
    while s: 
        timer = "{:01d}".format(s)
        print(message, timer, end="\r") 
        time.sleep(1) 
        s -= 1

# to print matrix in rows, get parameters about which matrix is it and so on
def print_matrix(which_matrix, matrix_name = "result", result_text = ""):

    # only clear_screen() when result_test is not empty
    if result_text != "":
        clear_screen()

    # print text to tell user which matrix is it showing now
    print(f"This is your {matrix_name} matrix. {result_text}")
    
    # using a for loop to display the matrix in rows instead of in a line
    for r in which_matrix:
        print(r)

# to check which operation system is the user running this program on and clear the screen in the cell prompt
def clear_screen():

    # to check is the user using linux or mac. The os.name for lunux and mac is "posix".
    if os.name == "posix":
        _ = os.system("clear")
    else:
        # for other operation system, e.g. window.
        _ = os.system("cls")

# to clear the list of "first_matrix", "second_matrix" and "result_matrix" of any data
def clear_matrices():
    first_matrix.clear()
    second_matrix.clear()
    result_matrix.clear()

# to display message and return value back to the caller code, after check first matrix is empty in the main program
def check_first_matrix():
    invalid_message = f"\nPlease select '[1] {menu_options[0]}' to create the first matrix first. \n"
    print(f"\nYour first matrix is empty. \nPlease return to the main menu and choose '[1] {menu_options[0]}' to create the first matrix and come back later. \n")
    countdown(5)
    return invalid_message

# to display message and return value back to the caller code, telling that both matrices don't meet the requirements in order to run the matrix operation
def not_same_matrices(matrixEqual_message, options_index):
    clear_screen()
    print(f"Please try again... \n{matrixEqual_message} \n")
    print(f"You can choose '[1] {menu_options[0]}' in the main menu to re-create a new first matrix \nOR \nchoose '[{options_index + 1}] {menu_options[options_index]}' again to create the correct second matrix.")
    invalid_message = f"\nSelect '[1] {menu_options[0]}' to re-create a new first matrix \nOR \nSelect '[{options_index + 1}] {menu_options[options_index]}' again to create the correct second matrix. \n"
    time_animation(5)
    countdown(5)
    return invalid_message

# to ask the user whether they wanted to edit another matrix, and return a boolean value back to the caller code
def ask_another_edit():

    another_edit = input("Do you want to edit again? Y/N: \n")

    if another_edit == "Y" or another_edit == "y" or another_edit == "yes" or another_edit == "Yes" or another_edit == "YES":
        clear_screen()
        return False
    else:
        clear_screen()
        return True

# to ask the user to enter the rows and columns of the matrix that the user is creating and check it is a vaild input
def create_matrix(matrix_index, which_matrix, product_matrices = False, rows = None, columns = None, data_complete = False):

    # using while loop for the following part, until the user entered a vaild input, and condition no longer is true
    while not data_complete:

        # test the input for errors
        try:

            # to check is product_matrices true, if will only be true when operating the product of two matrices, and automatically creating the result matrix
            if not product_matrices:

                # asking the user to enter the number of rows and columns
                rows = int(input(f"Enter the number of rows for the {EngNum[matrix_index]} matrix: \n"))
                columns = int(input(f"Enter the number of columns for the {EngNum[matrix_index]} matrix: \n"))
            
            # checking is the input out of range or not, as the program is only able to handle a matrix from 2x2 to 10x10
            if (rows < 2 or rows > 10) and (columns < 2 or columns > 10):
                clear_screen()
                print("The number of rows and columns you entered are out of range. \nPlease try again by entering a number between 2-10. \n")
            elif rows < 2 or rows > 10:
                clear_screen()
                print("The number of rows you entered is out of range. \nPlease try again by entering a number between 2-10. \n")
            elif columns < 2 or columns > 10:
                clear_screen()
                print("The number of columns you entered is out of range. \nPlease try again by entering a number between 2-10. \n")
            else:
                clear_screen()
                print("Here is your matrix that you have just created.")
                data_complete = True

        # handle the error if an exception occurs, to prevent the program from being terminating
        except ValueError:
            clear_screen()
            print(valueError_message)

    # create the matrix through the input the user just entered, using a for loop to add the value "0" into each rows and columns
    for i in range(rows):
        which_matrix.append([0] * columns)

    # print the matrix with vaule "0" that the user had just set up
    print_matrix(which_matrix, EngNum[matrix_index])

    # return the value of rows and columns in list form
    return [rows, columns]

# to allow user to enter and store the value for the matrix
def enter_matrix(matrix_index, which_matrix):
    
    # iterate through rows and columns of the matrix
    for i in range(len(which_matrix)):
        for j in range(len(which_matrix[0])):

            # reset the variable each time
            data_complete = False

            # using while loop for the following part, until the user entered a vaild input, and condition no longer is true
            while not data_complete:

                # test the input for errors
                try:
                    matrix_value = int(input(f"Enter the number for the {EngNum[matrix_index]} matrix at {EngNum[i]} row, {EngNum[j]} column: \n"))

                    # leave the while loop
                    data_complete = True
                
                # handle the error if an exception occurs, to prevent the program from being terminating
                except ValueError:
                    clear_screen()
                    print(valueError_message)

            # clear the screen and change the value of a specific item, refered to the index number
            # cannot use .append(), because rows and columns of the matrix were created in the create_matrix(), and the value is defaulted to "0"
            clear_screen()
            which_matrix[i][j] = matrix_value

            # print the real time update of the matrix
            print_matrix(which_matrix, EngNum[matrix_index])

# to edit the matrix, get parameters about which matrix, rows, columns, index is it and so on
def edit_matrix(matrix_index, which_matrix, which_rows, which_columns, data_complete = False):
    
    clear_screen()

    # using while loop for the following part, until the user entered a vaild input, and condition no longer is true
    while not data_complete:

        # call print_matrix(), to remind the user which matrix are they trying to edit
        print_matrix(which_matrix, EngNum[matrix_index])
        
        # test the input for errors
        try:

            # asking the user to enter the number of rows and columns
            edit_rows = int(input("\nEnter the row you want to edit: \n"))
            edit_columns = int(input("\nEnter the column you want to edit: \n"))

            # to check is the user input in range or note
            if edit_rows > 0 and edit_rows <= which_rows and edit_columns > 0 and edit_columns <= which_columns:
                
                # update variables, as it need to refer to the index number of the matrix (list) later on
                edit_rows = edit_rows - 1
                edit_columns = edit_columns - 1
                
                # test the input for errors
                try:

                    # asking the user to enter the new value and change the value in the specific rows and columns of the matrix
                    edit_value = int(input("\nEnter the new value: \n"))
                    which_matrix[edit_rows][edit_columns] = edit_value

                    # call clear_screen() and print_matrix() to print the matrix, and update the variable, which will leave the loop
                    clear_screen()
                    print_matrix(which_matrix, EngNum[matrix_index])
                    data_complete = True

                # handle the error if an exception occurs, to prevent the program from being terminating
                except ValueError:
                    clear_screen()
                    print(f"\n{valueError_message}")

            # call clear_screen() and print a reminder message to the user when the the previous conditions were not true
            else:
                clear_screen()
                print(f"Please trying again by entering a number between 1-{which_rows} for row and a number between 1-{which_columns} for column. \n")

        # handle the error if an exception occurs, to prevent the program from being terminating
        except ValueError:
            clear_screen()
            print(valueError_message)

# ask user to enter the scalar value for the matrix
def input_scalar(data_complete = False):

    # using while loop for the following part, until the user entered a vaild input, and condition no longer is true
    while not data_complete:

        # test the input for errors
        try:

            # ask the user to enter the scalar value for the matrix and call clear_screen() and return value back to the caller code
            scalar = int(input(f"Enter the scalar value for your matrix: \n"))
            clear_screen()
            return scalar

        # handle the error if an exception occurs, to prevent the program from being terminating
        except ValueError:
            clear_screen()
            print(valueError_message)

# to calculate the sum of two matrices
def matrix_addition():

    # iterate through rows and columns of the matrix
    for i in range(len(first_matrix)):
        for j in range(len(first_matrix[i])):

            # replace the value in the result_matrix after addition
            result_matrix[i][j] = first_matrix[i][j] + second_matrix[i][j]

    # call print_matrix() to print matrix in rows, and send parameters
    print_matrix(result_matrix, result_text = ("\nThe sum of your two matrices.")) 

# to find the scalar product of the matrix
def scalar_multi():

    # store the return value from the function to a variable called "scalar"
    scalar = input_scalar()

    # iterate through rows and columns of the matrix
    for i in range(len(first_matrix)):
        for j in range(len(first_matrix[i])):

            # replace the value in the result_matrix after scalar multplication
            result_matrix[i][j] = first_matrix[i][j] * scalar

    # call print_matrix() and pass the text and the result matrix into it
    print_matrix(result_matrix, result_text = ("\nThe scalar product of the matrix."))

# to find the product of two matrices
def matrix_multi():

    # iterate through rows, columns and rows of the matrix
    for i in range(len(first_matrix)):
        for j in range(len(second_matrix[0])):
            for k in range(len(second_matrix)):

                # add the value in the result_matrix after matrix multplication
                result_matrix[i][j] += first_matrix[i][k] * second_matrix[k][j]

    # call print_matrix() and pass the text and the result matrix into it
    print_matrix(result_matrix, result_text = ("\nThe product of two matrices."))


# MAIN PROGRAM

# the main program will keep looping, until condition is false
while (user_choice != 5):

    # call clear_screen(), and reset variables value to false each time the loop starts
    clear_screen()
    data_complete = False
    data_complete_2 = False

    # print the welcome message
    print(welcome_message)
    print(invalid_message)

    # print the menu through the list "menu_options" using for loop
    for i in range(0,5):
        print([i+1], menu_options[i])

    # test the input for errors
    try:
        user_choice = int(input("\nEnter your choice: "))

        # check is the user_choice in range
        if 0 < user_choice <= 4:

            # run the following code if user_choice is 1
            if user_choice == 1:
                clear_screen()
                print("You have chosen Create or Edit Matrix. \n")
                
                # using while loop for the following part, until the user entered a vaild input, and condition no longer is true
                while not data_complete:

                    # print another sub-menu
                    print("[1] Create the first matrix")
                    print("[2] Edit the matrices")

                    # test the input for errors
                    try:

                        create_choice = int(input("\nEnter your choice: "))

                        # run the following code if create_choice is 1
                        if create_choice == 1:

                            # call clear_screen(), and clear the first matrix
                            # clearing first matrix is needed, as after the loop run once, and when the user decided to re-create a new first matrix
                            clear_screen()
                            first_matrix.clear()
                            print("You have chosen Create the first matrix. \n")

                            # create the first matrix by calling creae_matrix(), and it will return the rows and columns as a list, and store into the variable
                            first_matrix_rc = create_matrix(0, first_matrix)

                            # sperate the value of rows and columns into different variables
                            first_rows = first_matrix_rc[0]
                            first_columns = first_matrix_rc[1]

                            # deepcopy the first matrix to empty_matrix and result_matrix
                            empty_matrix = copy.deepcopy(first_matrix)
                            result_matrix = copy.deepcopy(first_matrix)

                            # allow the user to enter the value for the first matrix
                            enter_matrix(0, first_matrix)
                            
                            # update the variable, which will leave the loop
                            print("\nFirst matrix created. \n")
                            data_complete = True

                        # run the following code if create_choice is 2
                        elif create_choice == 2:
                            
                            # check if both matrices are empty
                            if first_matrix == [] and second_matrix == []:

                                # call clear_screen() and pritn message
                                clear_screen()
                                print("Your matrices are empty. \nPlease create one first. \n")

                                # update the variable, which will leave the loop
                                data_complete = True
                            else:

                                clear_screen()

                                # using another while loop for the following part, until the user entered a vaild input, and condition no longer is true
                                while not data_complete_2:

                                    # print another sub-menu
                                    print("[1] Edit the first matrix")
                                    print("[2] Edit the second matrix")

                                    # test the input for errors
                                    try:
                                        edit_choice = int(input("\nEnter your choice: "))

                                        # run the following code if edit_choice is 1
                                        if edit_choice == 1:

                                            # check is the first matrix empty or not and update the variable, which will leave the sub-loop if that's true
                                            if first_matrix == []:
                                                print("\nYour first matrix is empty. \nPlease create one first. \n")
                                                data_complete_2 = True

                                            else:

                                                # call edit_matrix() and maybe run the loop again depending on the return value from the ask_another_edit() function.
                                                edit_matrix(0, first_matrix, first_rows, first_columns)
                                                print("\nEdited first matrix. \n")
                                                data_complete_2 = ask_another_edit()

                                        # run the following code if edit_choice is 2
                                        elif edit_choice == 2:

                                            # check is the second matrix empty or not and update the variable, which will leave the sub-loop if that's true
                                            if second_matrix == []:
                                                print("\nYour second matrix is empty. \nPlease create one first. \n")
                                                data_complete_2 = True

                                            else:
                                                
                                                # call edit_matrix() and maybe run the loop again depending on the return value from the ask_another_edit() function.
                                                edit_matrix(1, second_matrix, second_rows, second_columns)
                                                print("\nEdited second matrix. \n")
                                                data_complete_2 = ask_another_edit()

                                        # run the following code when the the previous conditions were not true
                                        else:
                                            clear_screen()
                                            print("\nPlease trying again by entering a number between 1-2.")

                                    # handle the error if an exception occurs, to prevent the program from being terminating
                                    except ValueError:
                                        clear_screen()
                                        print("\nOops! That was a text. Please try again with a valid number...")
                 
                            # update the variable, which will leave the main loop
                            data_complete = True

                        # run the following code when the the previous conditions were not true
                        else:
                            clear_screen()
                            print("Please trying again by entering a number between 1-2. \n")

                    # handle the error if an exception occurs, to prevent the program from being terminating
                    except ValueError:
                        clear_screen()
                        print(valueError_message)

                # call countdown() and to clear the string in "invalid_message", as "invalid_message" might have value in there already
                countdown(5)
                invalid_message = ""

                # skip the rest of the code that's in the loop and go back to the start of the loop
                continue

            # run the following code if user_choice is 2
            elif user_choice == 2:

                clear_screen()
                print("You have chosen the Matrix Addition.")
                time.sleep(1)

                # check if the first matrix is empty, if true, update the variable from the return value of the function and go back to the start of the loop
                if first_matrix == []:
                    invalid_message = check_first_matrix()
                    continue
                    
                # run the following code when the the previous conditions were not true
                else:

                    # check if both variables are true
                    if save_matrices is True and same_size_matrices is True:

                        # check if the second matrix is empty
                        if second_matrix == []:

                            # deepcopy a new second matrix from empty matrix, in order to copy the inner lists as well, and update the variables with the rows and columns 
                            second_matrix = copy.deepcopy(empty_matrix)
                            second_rows = len(second_matrix)
                            second_columns = len(second_matrix[0])

                            # let user to enter and store the data for the second matrix
                            enter_matrix(1, second_matrix)

                        # check if both conditions are met, if both true, update variables and go back to the start of the loop
                        if first_columns != second_columns and first_rows != second_rows:
                            invalid_message = not_same_matrices("The number of rows and columns in the first matrix must equal to the number of rows and columns in the second matrix.", 1)
                            same_size_matrices = False
                            continue

                        # print message and call time_animation()
                        print("\nUsing saved matrices to calculate...")
                        time_animation(2)   

                        # call matrix_addition() to calculate the sum for the matrices and update variable
                        matrix_addition()
                        same_size_matrices = True

                    # run the following code when the the previous conditions were not true
                    else:

                        # print messages, call time_animation() and clear the second matrix
                        print("Creating new matrices...")
                        time_animation(2)
                        print("Created new matrices. \n")
                        second_matrix.clear()

                        # deepcopy a new second and result matrix from the empty matrix, and update the variables with the rows and columns 
                        second_matrix = copy.deepcopy(empty_matrix)
                        result_matrix = copy.deepcopy(empty_matrix)
                        second_rows = len(second_matrix)
                        second_columns = len(second_matrix[0])

                        # let user to enter and store the data for the second matrix
                        enter_matrix(1, second_matrix)

                        # call matrix_addition() to calculate the sum for the matrices and update variable
                        matrix_addition()
                        same_size_matrices = True

            # run the following code if user_choice is 3
            elif user_choice == 3:
                
                clear_screen()
                print("You have chosen the Scalar Multiplication. \n")
                time.sleep(1)

                # check if the first matrix is empty, if true, update the variable from the return value of the function and go back to the start of the loop
                if first_matrix == []:
                    invalid_message = check_first_matrix()
                    continue
                else:

                    # run the following code if save_matrices is true
                    if save_matrices is True:
                        print("Getting the first matrix that you have saved...")
                        time_animation(2)

                        # call scalar_multi() to calculate the scalar product of the first saved matrix
                        scalar_multi()
                    else:                
                        # call scalar_multi() to calculate the scalar product for the first matrix
                        scalar_multi()

            # run the following code if user_choice is 4
            elif user_choice == 4:

                clear_screen()
                print("You have chosen the Product of Two Matrices.")
                time.sleep(1)

                # check if the first matrix is empty, if true, update the variable from the return value of the function and go back to the start of the loop
                if first_matrix == []:
                    invalid_message = check_first_matrix()
                    continue   
                else:

                    # check if both conditions are met
                    if save_matrices is True and same_size_matrices_rc is True:

                        # check if the second matrix is empty
                        if second_matrix == []:
                            print("\nLet's create the second matrix... \n")

                            # deepcopy a new second matrix from empty matrix, in order to copy the inner lists as well, and update the variables with the rows and columns 
                            second_matrix_rc = create_matrix(1, second_matrix)
                            second_rows = second_matrix_rc[0]
                            second_columns = second_matrix_rc[1]

                            # check if the first_columns and second_rows are the same, if true, allow the user to enter value for the second matrix
                            if first_columns == second_rows:
                                enter_matrix(1, second_matrix)

                        # check if the first_columns and second_rows are not the same, update variables and go back to the start of the loop
                        if first_columns != second_rows:
                            invalid_message = not_same_matrices("The number of columns in the first matrix must equal to the number of rows in the second matrix.", 3)
                            same_size_matrices_rc = False
                            continue

                        # result_matrix is not empty, as when creating the first matrix in option [1] deepcopied, so need to clear it and create a new one
                        result_matrix.clear()

                        # call create_matrix() and send arguments to automatically create the result matrix
                        create_matrix(2, result_matrix, True, first_rows, second_columns)

                        # call clear_screen(), time_animation() and print messages
                        clear_screen()
                        print("Please wait while the program is creating the result list...")
                        time_animation(2)
                        print("\nUsing saved matrices to calculate...")
                        time_animation(2)      

                        # call matrix_multi() to calculate the product of two matrices, and update variable
                        matrix_multi()
                        same_size_matrices_rc = True
                    else:

                        # clear the second matrix, as user might saved it
                        second_matrix.clear()
                        print("\nLet's create the second matrix... \n")

                        # deepcopy a new second matrix from empty matrix, in order to copy the inner lists as well, and update the variables with the rows and columns 
                        second_matrix_rc = create_matrix(1, second_matrix)
                        second_rows = second_matrix_rc[0]
                        second_columns = second_matrix_rc[1]

                        # check if the first_columns and second_rows are not the same, and go back to the start of the loop
                        if first_columns != second_rows:
                            invalid_message = not_same_matrices("The number of columns in the first matrix must equal to the number of rows in the second matrix.", 3)
                            continue

                        # result_matrix is not empty, as when creating the first matrix in option [1] deepcopied, so need to clear it and create a new one
                        result_matrix.clear()

                        # call create_matrix() and send arguments to automatically create the result matrix
                        create_matrix(2, result_matrix, True, first_rows, second_columns)

                        # call clear_screen(), time_animation() and print messages
                        clear_screen()
                        print("Please wait while the program is creating the result list...")
                        time_animation(2)

                        # let user to enter and store the data for the second matrix
                        enter_matrix(1, second_matrix)

                        # call matrix_multi() to calculate the product of two matrices, and update variable
                        matrix_multi()
                        same_size_matrices_rc = True

        # run the following code when the the previous conditions were not true
        else:

            # check if user_choice is not 5 and update the variable
            if user_choice != 5:
                invalid_message = "\nPlease trying again by entering a number between 1-5. \n"

                # go back to the start of the loop, instead of running the following program
                continue

    # handle the error if an exception occurs, to prevent the program from being terminating
    except ValueError:
        invalid_message = f"\n{valueError_message}"
        continue

    # reset variable
    user_choice = ""

    # to confirm is the user want to continue the program
    continue_choice = input("\nDo you want to continue the program? Y/N: \n")

    # check if user entered any of these conditions
    if continue_choice == "Y" or continue_choice == "y" or continue_choice == "yes" or continue_choice == "Yes" or continue_choice == "YES":
        clear_screen()
        print(f"\nYou can always choose '[1] {menu_options[0]}' in the main menu to re-create a new first matrix or edit your previous matrices. \n")

        # ask the user whether they wanted to save the previous matrix or matrices
        save_choice = input("Do you want to save your previous matrix/matrices for the next calculation? Y/N: \n")

        # check if user entered any of these conditions
        if save_choice == "Y" or save_choice == "y" or save_choice == "yes" or save_choice == "Yes" or save_choice == "YES":

            # print message and update variable to True
            print("\nYour matrix/ matrices has/ have been saved. \n")
            save_matrices = True
        else:

            # print message and update variable to False
            print("\nYour matrix/ matrices has/ have been deleted. \n")
            save_matrices = False

            # call clear_matrices() to clear the list "first_matrix", "second_matrix" and "result_matrix" of any data, ready for next data entry
            clear_matrices()

        # set new value to invalid_message, so it will appear in the next loop, and call countdown()
        invalid_message = "\nIt's great to see you here again :)\n"
        countdown(5, "Restarting program in")

    # run the following code when the the previous conditions were not true
    else:
        # update the variable, and the condition of the while loop will become false, which will leave the loop
        user_choice = 5

# the user has quitted the program
print("\nThank you for using the Matrix Operation Algorithms. \nHope to see you soon. \nBye Bye")

#### END OF MAIN PROGRAM
