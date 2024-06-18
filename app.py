from donations_pkg import homepage, user  # imports functions

# let's declare some variables
database = {"admin": "1234"}  # dictionary
donations = []  # empty list
authorized_user = ""

# show the homepage initially
homepage.show_homepage()
while True:
    print("You must be logged in to donate")
    option = input("Choose an option: ")

    if option == "1":
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        authorized_user = user.login(database, username, password)
        homepage.show_homepage()
        if authorized_user != "":
            print(f"Logged in as: {username}")

    elif option == "2":
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        authorized_user = user.register(database, username, password)
        if authorized_user != "":
            database[username] = password
            print(f"Registered successfully and logged in as: {username}")
        homepage.show_homepage()

    elif option == "3":
        if authorized_user == "":
            print("You are not logged in")
        else:
            donation_string = homepage.donate(authorized_user)
            donations.append(donation_string)
        homepage.show_homepage()

    elif option == "4":
        homepage.show_donations(donations)
        homepage.show_homepage()

    elif option == "5":
        print("Leaving DonateMe... ")
        break

    else:
        print("Invalid option, please try again.")
