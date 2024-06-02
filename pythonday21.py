#🐍 Day 21: Stay Connected: Your Very Own Contact Book 🐍
contact_book = []
def add_contact(name, phone_number, email):
    contact = {'name': name, 'phone_number': phone_number, 'email': email}
    contact_book.append(contact)
def display_contacts():
    for contact in contact_book:
        print(contact)
while True:
    name = input("Choose an option:add,view,find,delete a, delete,edit,q: ")
    if name == 'q':
        break
    elif name == '':
        print("You must enter a name")
        continue
    elif name == 'view':
        display_contacts()
    elif name == 'delete a':
        contact_book.clear() #will delete all contacts in the contact book,
    elif name == 'delete':
        name = input("Enter a name: ")
        for contact in contact_book:
            if contact['name']==name:
                contact_book.remove(contact)#will delete the first contact that matches the name entered
                print("Contact deleted")
    elif name == 'find':
        name = input("Enter a name:")
        for contact in contact_book:
            if contact['name']==name:
                print(contact)
    elif name == 'edit':
        name = input("Enter a name: ")
        phone_number = input("Enter a phone number: ")#will edit the first contact that matches the name entered
        email = input("Enter an email: ")
        for contact in contact_book:
            if contact['name']==name:
                contact['phone_number']=phone_number#
                contact['email']=email
                print("Contact edited") 
    elif name == 'add':
        name = input("Enter a name: ")
        phone_number = input("Enter a phone number: ")
        email = input("Enter an email: ")
    add_contact(name, phone_number, email)
    print("Contact added succesfully")