
# Login System To Enter Username and Password in 3 chances else Access Denied

def login():
    '''Enter User and Password in 3 chances other then chances Denied'''

    login_System = {
        'Username' : 'Hamza Khan',
        'Password' : 'Hamza'
    }
    
    chances = 3
    chance_user = 0
    chance_pass = 0
    a = True
    while a:
        user_name = input("Enter User Name:")

        chance_user += 1  
        if user_name == login_System['Username']:
            
            print('User Name Match')

            while True:
                password = input("Enter Password:")
                chance_pass += 1

                if password == login_System['Password']:
                    print("Password Match")
                    print('You Have Been Logined Successfully')
                    a = False
                    break

                elif chance_pass == chances:
                    print('Password Not Match ***')

                else:
                    print('Wrong Password')
                   


        elif chance_user == chances:
            print('Access Denied')
            break

        else:
            print('Try Again')    

login()            