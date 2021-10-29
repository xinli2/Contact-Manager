###
### Author: Xin Li
### Description:  In this short PA, you will be writing a program
### to implement a very simple contact organizer application
### in Python. You should write a program called contact_manager.py.
### Using this application, you will be able to request contact
### information, as well as add new contacts to the contact manager.
###

def read_file():
    contact_set = set()
    contact_file = open('contacts.txt', 'r')
    lines = contact_file.readlines()
    for line in lines:
        line = line.strip('\n')
        information = line.split(' | ')
        contact_tuples = (information[0], information[1], information[2])
        contact_set.add(contact_tuples)
    return contact_set


def showing_contacts(contact_set,command):
    command_tuples=()

    if 'name' in command:
        keyword = command[24:]
    elif 'phone' in command or 'email' in command:
        keyword = command[25:]
    point=True
    for i in sorted(contact_set):
        if keyword in i:
            print(i[0]+"'s contact info:")
            print('  email:',i[1])
            print('  phone:',i[2])
            point=False
    if point:
        print('None')

def adding_a_contact (contact_set):
    name = input('name:\n')
    email = input('email:\n')
    phone = input('phone:\n')
    contact_tuples = (name, email, phone)
    if contact_tuples in contact_set:
        print('Contact already exists!')
    else:
        contact_set.add(contact_tuples)
        print('Contact added!')
    return contact_set


def exitt(index):
    print('Goodbye!')
    return -1

def saving(contact_set):
    line = ''
    file=open('contacts.txt', 'w')
    for k in sorted(contact_set):
        file.write(k[0]+' | '+k[1]+' | '+k[2]+'\n')
    file.close()


def main():
    print('Welcome to the contacts app!')
    index = 1
    contact_set = read_file()
    while index > 0 :
        command = input('>\n')
        if 'show contacts with' in command:
            showing_contacts(contact_set,command)
        if command == 'add contact':
            contact_set = adding_a_contact(contact_set)
        if command == 'exit':
            saving(contact_set)
            index = exitt(index)

main()
