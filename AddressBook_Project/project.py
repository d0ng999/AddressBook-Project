# AddressBook Program
import os # Os Module

class Contact:
    # Constructor - Name, Mobile Number, Email, Address
    def __init__(self, name, phonenum, email, addr) -> None:
        self.__Name = name
        self.__phoneNum = phonenum
        self.__Email = email
        self.__Address = addr

    # __str__ Redifine
    def __str__(self) -> str:
        str_res = (f'Name : {self.__Name}\n'
                   f'Number : {self.__phoneNum}\n'
                   f'E-mail : {self.__Email}\n'
                   f'Address : {self.__Address}')
        return str_res
    
    # Check whether the object exists
    def isNameExist(self, name):
        if self.__Name == name:
            return True
        else:
            return False
    
    # Method to be able to access to the each of member variable
    def getName(self) -> str:
        return self.__Name
    def getphoneNum(self) -> str:
        return self.__phoneNum
    def getEmail(self) -> str:
        return self.__Email
    def getAddress(self) -> str:
        return self.__Address

# Input user's address
def set_contact(): 
    name, phonenum, email, addr = input('Address Input(Name/Mobile Number/E-mail/Address) : ').split('/')
    contact = Contact(name = name, phonenum=phonenum,email=email,addr=addr)
    return(contact)

# Save the address file
def save_contacts(list):
    file = open('C:/Source/Address-Book-Project/AddressBook_Project/contacts.txt', 'w', encoding = 'utf-8')

    for item in list:
        text = f'{item.getName()}/{item.getphoneNum()}/{item.getEmail()}/{item.getAddress()}'
        file.write(f'{text}\n')

    file.close()

# Load the file and rewrite or read it
def load_contacts(list):
    try:
        file = open('C:/Source/Address-Book-Project/AddressBook_Project/contacts.txt', 'r', encoding = 'utf-8')
    except Exception as e:
        f = open('C:/Source/Address-Book-Project/AddressBook_Project/contacts.txt', 'w', encoding = 'utf-8')
        f.close()
        return

    while True:
        line = file.readline().replace('\n','')

        if not line:
            break
        lines = line.split('/')
        contact = Contact(lines[0], lines[1], lines[2], lines[3])
        list.append(contact)
    file.close()

# Show menu
def get_menu():
    str_menu = ('Address Book App. : 0.5v\n'
                '1. Add Address\n'
                '2. Address Output\n'
                '3. Delete Address\n'
                '4. Exit the App.')
    print(str_menu)

    try:
        menu = int(input('Menu Input : '))
    except Exception as e:
        menu = 0

    clear_console()
    return menu

# Delete the address
def del_contact(list, name):
    count = 0
    for i, item in enumerate(list):
        if item.isNameExist(name):
            count += 1
            del list[i]
    if count > 0:
        print('Deleted.')
    else:
        print('There is no data.')

# AddressBook Output
def get_contacts(list):
    for item in list:
        print(item)
        print('==============')

# Clear the screen(Optional)
def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

# Run program
def run():
    contacts = [] # Make an empty list to save the addresses
    load_contacts(contacts)
    clear_console()
    while True:
        sel_menu = get_menu()
        if sel_menu == 1:
            try:
                contact = set_contact()
                contacts.append(contact)
                input('Address Addition Successful')
            except Exception as e:
                print('Please, Type your Name/Mobile Number/E-mail/Address in order')
                input()
            finally:
                clear_console()

        elif sel_menu == 2:
            get_contacts(contacts)
            input('AddressBook Output')
            clear_console()

        elif sel_menu == 3:
            name = input('Type a name to delete : ')
            del_contact(contacts, name)
            input()
            clear_console()

        elif sel_menu == 4:
            save_contacts(contacts)
            break
        else:
            clear_console()

if __name__ == '__main__':
    run()