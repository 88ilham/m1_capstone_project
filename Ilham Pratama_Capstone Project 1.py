import pandas as pd

## CONTACT LIST
yellow_pages = {
    'Contact ID': [101, 102, 103, 104, 105],
    'First Name': ['Fyodor', 'Anaïs', 'RM Pagi Sore','RM Garuda', 'dr John'],
    'Last Name': ['Dostoevsky', 'Nin', '', '', 'Doe'],
    'Phone Number': ['081234567890', '081798765432', '02156781234'],
    'Category': ['Personal', 'Personal', 'Business', 'Business', 'Personal']
}

## MENU OPTIONS
menu_0 = '0. Search Existing Contact'
menu_1 = '1. Display Contact List'
menu_2 = '2. Add New Contact'
menu_3 = '3. Update Existing Contact'
menu_4 = '4. Delete Contact'
menu_5 = '5. Yellow Page Info'
menu_6 = '6. Exit Program'

## MAIN MENU
def display_menu():
    print(menu_0)
    print(menu_1)
    print(menu_2)
    print(menu_3)
    print(menu_4)
    print(menu_5)
    print(menu_6)

## MENU 0 SEARCH BAR
def search_contact():
    find_contact=input('Input the Name, Phone Number, or Contact ID to search: ')

    # search by contact ID (integer)
    if find_contact.isdigit():
        find_contact=int(find_contact)  # Convert to integer if it is a number
        for i, contact_id in enumerate(yellow_pages['Contact ID']):
            if contact_id==find_contact:
                # print matching contact details
                print(f"Contact found: ID: {contact_id}, Name: {yellow_pages['First Name'][i]} {yellow_pages['Last Name'][i]}, "
                    f"Phone Number: {yellow_pages['Phone Number'][i]}, Category: {yellow_pages['Category'][i]}")
                break
        else:
            print("No contact found with that ID.")

    # search by phone number (string)
    elif find_contact.isnumeric():
        for i, phone_number in enumerate(yellow_pages['Phone Number']):
            if phone_number==find_contact:
                # print matching contact details
                print(f"Contact found: ID: {yellow_pages['Contact ID'][i]}, Name: {yellow_pages['First Name'][i]} {yellow_pages['Last Name'][i]}, "
                    f"Phone Number: {phone_number}, Category: {yellow_pages['Category'][i]}")
                break
        else:
            print("No contact found with that phone number.")

    # search by name (string)
    else:
        for i, first_name in enumerate(yellow_pages['First Name']):
            last_name=yellow_pages['Last Name'][i]
            
            if find_contact.lower()==first_name.lower() or find_contact.lower()==last_name.lower():
                # print matching contact details
                print(f"Contact found: ID: {yellow_pages['Contact ID'][i]}, Name: {yellow_pages['First Name'][i]} {yellow_pages['Last Name'][i]}, "
                    f"Phone Number: {yellow_pages['Phone Number'][i]}, Category: {yellow_pages['Category'][i]}")
                break
        else:
            print("No contact found with that first or last name.")

## MENU 1 DISPLAYING CONTACT LIST
def display_contact_list():
    print('\nContact List ---------')
    print()
    contact_list=pd.DataFrame(yellow_pages)
    print(contact_list)

## MENU 2 ADD NEW CONTACT
def add_new_contact():
    print('\n--- Add New Contact ---')
    first_name=input('Enter the contact first name: ')
    last_name=input('Enter the contact last name (press Enter to keep blank): ')
    phone_number=input('Enter the phone number: ') 
    category=input('Enter the category (e.g., Personal, Business): ')
    
    if category.isalpha():  # to check if it's contain only letters
        yellow_pages['Category'].append(category.title())  # title case
    else:
        print("Invalid category. Please enter letters only.")
        return  # return the function if the category input is invalid
    
    # generate new ID for the new contact
    new_id=len(yellow_pages['Contact ID']) + 101
    yellow_pages['Contact ID'].append(new_id)
    yellow_pages['First Name'].append(first_name)
    yellow_pages['Last Name'].append(last_name if last_name else "")
    yellow_pages['Phone Number'].append(phone_number)

    print(f"\nNew contact '{first_name} {last_name if last_name else ''}' has been added successfully!\n")
    display_contact_list()
    print()

## MENU 3 UPDATE EXISTING CONTACT
def update_existing_contact():
    print('\n--- Update Existing Contact ---')
    display_contact_list()
    contact_id=int(input("Enter the contact ID to update: "))
    
    # find the contact to update
    if contact_id in yellow_pages['Contact ID']:
        index=yellow_pages['Contact ID'].index(contact_id)
        print(f"Updating contact ID {contact_id}:")
        
        # get new details for the contact
        updated_first_name=input(f"Current First Name: {yellow_pages['First Name'][index]}\nEnter new first name (press Enter to keep current): ")
        if updated_first_name !="":
            yellow_pages['First Name'][index]=updated_first_name
        
        updated_last_name = input(f"Current Last Name: {yellow_pages['Last Name'][index]}\nEnter new last name (press Enter to keep current): ")
        if updated_last_name !="":
            yellow_pages['Last Name'][index]=updated_last_name

        updated_phone_number = input(f"Current Phone Number: {yellow_pages['Phone Number'][index]}\nEnter new phone number (press Enter to keep current): ")
        if updated_phone_number !="":
            yellow_pages['Phone Number'][index]=updated_phone_number
            
        updated_category=input(f"Current Category: {yellow_pages['Category'][index]}\nEnter new category (press Enter to keep current): ")
        if updated_category !="":
            updated_category=updated_category.strip().title()
            if updated_category.isalpha():
                yellow_pages['Category'][index]=updated_category
            else:
                print("Invalid category. Please enter letters only.")
                return  # return the function if invalid category input
        
        print(f"Contact ID {contact_id} has been successfully updated!")
        display_contact_list()
    else:
        print(f"No contact found with ID: {contact_id}\n")
    print()


## MENU 4 DELETE CONTACT
def delete_contact():
    display_contact_list()
    print()
    delete_call_id=int(input('Input the ID you want to delete: '))
    
    # find and delete the contact by ID
    if delete_call_id in yellow_pages['Contact ID']:
        index=yellow_pages['Contact ID'].index(delete_call_id)
        yellow_pages['Contact ID'].pop(index)
        yellow_pages['First Name'].pop(index)
        yellow_pages['Last Name'].pop(index)
        yellow_pages['Phone Number'].pop(index)
        yellow_pages['Category'].pop(index)
        
        print(f"The contact with ID {delete_call_id} has been successfully deleted!\n")
        display_contact_list()
    else:
        print(f"No contact found with ID {delete_call_id}\n")
    print()

## MENU 5 YELLOW BOOK INFO
def display_contact_count():
    print(f"There are {len(yellow_pages['Contact ID'])} contacts in the list.")
    
    category_count={}
    # loop through all contacts and count the occurrences of each category
    for category in yellow_pages['Category']:
        category_count[category]=category_count.get(category, 0) + 1

    # display the count for each category
    print("\nContact count by category:")
    for category, count in category_count.items():
        print(f"{category}: {count} contacts")

# MAIN LOOP
while True:
    print()
    print('--- Welcome to the LinkUp!---')
    print()
    display_menu()
    menu_input=int(input('Enter the program number you want to run: '))
        
    if menu_input==0:
        print()
        search_contact() 
    elif menu_input==1:
        print()
        display_contact_list()
    elif menu_input==2:
        print()
        add_new_contact()
    elif menu_input==3:
        print()
        update_existing_contact()
    elif menu_input==4:
        print()
        delete_contact()
    elif menu_input==5:
        print()
        display_contact_count()
    elif menu_input==6:
        print()
        print('Exiting the program...')
        break
    else:
        print()
        print('Invalid option, please enter a number from 1-5.\n')