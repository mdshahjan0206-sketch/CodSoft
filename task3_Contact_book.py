# Create an empty dictionary to store contacts
contacts = {}

while True:
    # Display menu
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Contact
    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")

        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }

        print("Contact Added Successfully!")

    # View Contacts
    elif choice == "2":
        if contacts:
            print("\nContact List:")
            for name, details in contacts.items():
                print(f"\nName: {name}")
                print("Phone:", details["Phone"])
                print("Email:", details["Email"])
                print("Address:", details["Address"])
        else:
            print("No Contacts Found!")

    # Search Contact
    elif choice == "3":
        name = input("Enter Name to Search: ")

        if name in contacts:
            print("\nContact Found!")
            print("Phone:", contacts[name]["Phone"])
            print("Email:", contacts[name]["Email"])
            print("Address:", contacts[name]["Address"])
        else:
            print("Contact Not Found!")

    # Update Contact
    elif choice == "4":
        name = input("Enter Name to Update: ")

        if name in contacts:
            contacts[name]["Phone"] = input("New Phone: ")
            contacts[name]["Email"] = input("New Email: ")
            contacts[name]["Address"] = input("New Address: ")

            print("Contact Updated Successfully!")
        else:
            print("Contact Not Found!")

    # Delete Contact
    elif choice == "5":
        name = input("Enter Name to Delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact Deleted Successfully!")
        else:
            print("Contact Not Found!")

    # Exit Program
    elif choice == "6":
        print("Thank You for Using Contact Book!")
        break

    else:
        print("Invalid Choice! Try Again.")
