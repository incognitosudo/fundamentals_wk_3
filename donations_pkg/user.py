#defin function login
def login(database, username , password):
    if username in database:
        if database[username] == password:
            print(f"Welcome {username} !")
            return username
        else:
            print(f"You have inputted incorrect password {username}")
            return ""
    else:
        print(f"{username} not found...")
        return ""

    print(database, username, password)

def register(database, username, password):
    if username in database:
        print("Username already registered.")
        return ""
    
    else:
        database[username] = password
        print(f"Username {username} registered!")
        return username