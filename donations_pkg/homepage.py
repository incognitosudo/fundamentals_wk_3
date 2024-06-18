#task 2 show homepage and initialize app data
def show_homepage():
    print("")
    print("          === DonateMe Homepage ===          ")
    #print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Login       | 2.  Register       |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Donate      | 4.  Show Donations |")
    print("------------------------------------------")
    print("| 5.           Exit                      |")
    print("------------------------------------------")


#< ---- task 6 --->
def donate(username):
        donation_amnt = input("Enter amount to donate: ")
        donation_string = f"{username} donated ${donation_amnt}"
        print("Thank you for your donation!", donation_string)
        return donation_string

def show_donations(donations):
    print("\n--- All Donations ---")
    if not donations:
        print("Currently, there are no donations.")
    else:
        for donation in donations:
            print(donation)