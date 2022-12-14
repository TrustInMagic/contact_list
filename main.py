from utility import read_contacts, write_contacts, verify_email_address


CONTACT_FILE_PATH = "contacts.json"


def add_contact():
    contact_list = read_contacts(CONTACT_FILE_PATH)    

    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    mobile_phone = input("Mobile Phone Number: ")
    home_phone = input("Home Phone Number: ")
    email = input("Email Address: ")
    address = input("Address: ")    
    
    for contact in contact_list:
        if first_name == contact["first_name"] and last_name == contact["last_name"]:
            print("A contact with this name already exists.")
            return False

    edited_mobile_phone = mobile_phone.replace("-", "")
    if len(mobile_phone) > 0 and (not edited_mobile_phone.isdigit() or len(edited_mobile_phone) != 10):
        print("Invalid mobile phone number.")
        return False
    
    edited_home_phone = home_phone.replace("-", "")
    if len(home_phone) > 0 and (not edited_home_phone.isdigit() or len(edited_home_phone) != 10):
        print("Invalid mobile phone number.")
        return False

    if len(email) > 0 and verify_email_address(email) == False:
        print("Invalid email address.")
        return False

    contact = {
        "first_name": first_name,
        "last_name": last_name,
        "mobile": mobile_phone,
        "home": home_phone,
        "email": email,
        "address": address
    }

    contact_list.append(contact)
    write_contacts(CONTACT_FILE_PATH, contact_list)
    return True



def search_for_contact(contact_list):
    contacts_found = []
    
    first_name = input("First Name: ")
    last_name = input("Last Name: ")

    for contact in contact_list:
        if first_name in contact["first_name"] and last_name in contact["last_name"]:
            contacts_found.append(contact)

    print(f"Found {len(contacts_found)} matching contacts.")
    list_contacts(contacts_found)
    return contacts_found


def delete_contact():
    contact_list = read_contacts(CONTACT_FILE_PATH)
    contacts_to_delete = []
    
    first_name = input("First Name: ") 
    last_name = input("Last Name: ") 

    for contact in contact_list:
        if contact["first_name"] == first_name and contact["last_name"] == last_name:
            contacts_to_delete.append(contact)
    
    if len(contacts_to_delete) == 0 :
        print("No contact with this name exists.")
    else:
        decision = input("Are you sure you would like to delete this contact (y/n)? ")
        if decision in ["y", "yes"]:
            contact_list.remove(contacts_to_delete[0])
            
            write_contacts(CONTACT_FILE_PATH, contact_list)



def list_contacts(contact_list):
    indent = "        "
    contact_details_edited = {"mobile": "Mobile Phone Number", "home": "Home Phone Number", "email": "Email Address", "address": "Address"}
    
    for idx, contact in enumerate(contact_list):
        print(f"{idx+1}. {contact['first_name']} {contact['last_name']}")
        for detail in contact:
            if detail != "first_name" and detail != "last_name" and len(contact[detail]) > 0:
                if detail in contact_details_edited:
                    print(f"{indent} {contact_details_edited[detail]} {contact[detail]}")          


def main():
    print("Welcome to your contact list!\n")
    print("The following is a list of useable commands:")
    print("'add': Adds a contact.")
    print("'delete': Deletes a contact.")
    print("'list': Lists all contacts.")
    print("'search': Searches for a contact by name.")
    print("'q': Quits the program and saves the contact list.")


    while True:
        contact_list = read_contacts(CONTACT_FILE_PATH)
        command = input("\nType a command: ")

        if command == "add":
            if add_contact():
                print("Contact Added!")
            else:
                print("You entered invalid information, this contact was not added.")

        elif command == "list":
            list_contacts(contact_list)
        
        elif command == "search":
            search_for_contact(contact_list)

        elif command == "delete":
            delete_contact()

        elif command == "q":
            print("Contacts were saved successfully.")
            break
        else:
            print("Unknown command")



if __name__ == "__main__":
    main()
