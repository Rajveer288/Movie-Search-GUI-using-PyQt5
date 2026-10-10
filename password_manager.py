import time
def add_password(password):
    print('*******************')
    add=input('Type your password: ')
    print('adding password')
    time.sleep(1.5)
    password.append(add)
    print('password added successfully')
def delete_password(password):
    if not password:
        print("You have'nt entered any password")
    else:
        try:
            print('Saved passwords : ')
            for j in password:
                print(j)
            print('*********************')
            delete = input('Type the password you want to delete: ')
            print('deleting password')
            time.sleep(1.5)
            password.remove(delete)
            print('this password was not added')
            print('password deleted successfully')
        except ValueError:
            print("You have entered an invalid password")
def view_passwords(password):
    if not password:
        print("You have'nt entered any password")
    else:
        print('**************************')
        for i in password:
            print(i)
def main():
    password=[]
    running=True
    print('***************************')
    print('Welcome to Password Manager')
    print('***************************')
    while running:
        ask=input('1)ADD PASSWORD\n2)DELETE PASSWORD\n3)VIEW PASSWORDS\n4)QUIT\nEnter your choice(In option): ')
        if not ask.isdigit():
            print('Enter your choice in digit ')
            continue
        if ask not in ['1','2','3','4']:
            print('Enter your choice in wrong format')
            continue
        elif ask == '1':
            add_password(password)
        elif ask == '2':
            delete_password(password)
        elif ask == '3':
            view_passwords(password)
        elif ask == '4':
            print('Thank you for using Password Manager')
            running=False
        else:
            print('Invalid input')
            continue
if __name__ == '__main__':
    main()