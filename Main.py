"""
In this program we can manage the password og websites
Also first you have to enter the correct name and password to start
Here we have given importance to security also, at some places you have to enter the password to proceed
Here you can read the existing password as well as modify it
Also able to delete one or all passwords at once
Not only this you can also see all passwords at once
"""
import json                          #This is used to access the json file.
NAME = 'Kaustubh'                    #As always defining the constants.
PASSWORD = 1234

def main():
    existing = get_data()

    x = verification()    #In this your name and password will be verified.

    if x == 'Yes':
        printing_starting_commands()   #In this fuction we are writing all sentences at once.

        while (True):       #Here we have used true to work out the loop. You can also write a expression which makes boolean true.

            taking_input(existing)   #Also in bracket writing the parameter because without this fuctions can't use given values.

            value = (input("Would you like to continue? Enter Y for yes; Enter N for no: "))
            print('')

            if value == "N":
                break

            if value == "Y":
                print('')

                printing_options()

    elif x == 'No':
        print('')            #You are going to see this print statement a lot times in the code.This is used to skip a line.

        print("Your entered password is incorrect!")

    write_data(existing)
    print("Bye bye! Have a nice day Kaustubh.")

def get_data():                    
    try:
        with open("data.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}  # Start with an empty dictionary if the file doesn't exist
        write_data(data)  # Create the file with the empty dictionary
    return data
                #Here it returns the value.

def write_data(alist):               #At here we are writing into our json file means we are adding elements into it.
    data = alist

    with open("data.json", "w") as f:

        json.dump(data, f, indent=4)        #As dictionaries are mutable so we don't have to return anything.


def taking_input(existing):                #At this place we are taking input from the user and it will be proceeded.
    option = int(input('Enter here: '))

    if option == 1:           #If user chooses the 1st option then this loop will be executed.
        print('')

        inp1 = str(input('Which website password do you want? '))

        print('')

        print(existing.get(inp1))          #In this code block the value of the key is going to be printed in output.

        print('')

    if option == 2:          #If user chooses the 2nd option then this loop will be executed.
        print('')

        web = input('Enter website name here: ')

        web_pass = input('Enter password here: ')

        existing[web] = web_pass          #In this code block the key value pair will be stored in the json file.

        print("")

        print('Hurray! Your password is successfully saved. ')

        print('')

    if option == 3:           #If user chooses the 3rd option then this loop will be executed.
        print('')

        change_web = input('Enter the name of website: ')

        change_pass = input('Enter your new password: 1')

        existing[change_web] = change_pass        #In this code block the value of the key will be changed in json file.

        print('')

        print('Congrats! Your password is successfully modified. ')

        print('')

    if option == 4:          #If user chooses the 4th option then this loop will be executed.
        print('')

        print('To get the list of your all passwords saved you have to enter your password again.')

        y = int(input('Enter your password:'))

        if y == PASSWORD:
            ver = ['', 'Verified successfully!', '', 'Here is your password list: ', '']

            for elem in ver:       #To reduce the code space we have used list fuction here.
                print(elem)

            for key in existing:
                print(str(key), '->', str(existing[key]))         #Here all the key value pairs will be printed in output.

                print('')

            print('-----------------------------------------------------------------------------------------')

            print('')

        elif y != PASSWORD:
            print('Your entered password is incorrect! ')

            print('')

    if option == 5:            #If user chooses the 5th option then this loop will be executed.

        del_list = ['', 'To delete one password enter 1', 'To delete all passwords enter 2', '']

        for elem in del_list:        #To reduce the code space we have used list fuction here.
            print(elem)

        del_inp = int(input('Enter here: '))
        print('')                   #This code block is made for user to choose whether he wants to delete one or all passwords.

        if del_inp == 1:
            del_inp1(existing)              #This line is going to execute the another code block
                                            #We have done this to make the code a lot more easier to understand.
        if del_inp == 2:
            del_inp2(existing)

    if option not in [1, 2, 3, 4, 5]:         #Here if you have given icorrect input, this will be executed.
        print('Please! Enter valid option')

def del_inp2(existing):                    #Here in this code all the key value pairs are going to be deleted.
    ask2 = str(input('Do you really want to delete? Enter Y for yes; Enter N for no: '))

    if ask2 == 'Y':
        ask_pass2 = int(input('Enter your password to process: '))

        print('')

        if ask_pass2 == PASSWORD:
            existing.clear()            #This function is used to delete all key value pairs & doesn't returns anything.

            print('All website passwords are successfully deleted. ')

            print('')

        elif ask_pass2 != PASSWORD:
            print("Your entered password is incorrect! ")

            print('')

    elif ask2 == 'N':
        print('Ok :)')


def del_inp1(existing):           #Here in this code you are able to delete one key value pair.
    ask1 = str(input('Do you really want to delete? Enter Y for yes; Enter N for no: '))

    if ask1 == 'Y':
        ask_pass1 = int(input('Enter your password to process: '))

        if ask_pass1 == PASSWORD:
            print('')
            del_web = input('Enter website name: ')

            del existing[del_web]      #This is used to delete the one key value pair & it doesn't returns anything.

            del_print_list = ['', 'Website password is successfully deleted. ', '']

            for elem in del_print_list:
                print(elem)

        elif ask_pass1 != PASSWORD:
            print("Your entered password is incorrect! ")

            print('')

    elif ask1 == 'N':
        print('Ok :)')

def printing_starting_commands():           #Here it prints out all the oening statements of program.

    alist = ['Select among the following options:', '',

             'To get existing one enter 1', 'To add new one enter 2', 'To modify existing password enter 3', 'To get list of all passwords enter 4', 'To delete password enter 5', '']

    for elem in alist:              #We have used the list function here to reduce the code space and to make easy to understand.
        print(elem)

def printing_options():
    options = ['',  'Select among the following options:', '',

             'To get existing one enter 1', 'To add new one enter 2', 'To modify existing password enter 3', 'To get list of all passwords enter 4', 'To delete password enter 5', '']
    for elem in options:
        print(elem)

def verification():                 #Here is the place where the verification takes place.
    name = input('Enter your name: ')

    if name == NAME:
        user_password = int(input('Enter your password here: '))
        if user_password == PASSWORD:        #This will return YES if function is true
            print('')

            print('Hello ' + str(name) + '!' + ' Welcome to your own Password Manager.')

            return 'Yes'

        elif user_password != PASSWORD:       #This will return NO if function is true
            return 'No'

    if name != NAME:
        print("Name is incorrect!")




if __name__ == '__main__':
    main()                     #Never forget this to write because without this your program is not going to be executed.

