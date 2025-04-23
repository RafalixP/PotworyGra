from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open ("key.key", "wb") as key_file:
        key_file.write(key)
        
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

load_key()

master_pwd = input('What is the master psswrd? ')
key = load_key() + master_pwd.encode()
fer = Fernet(key)



# Tim 1:30h

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            #print(line.rstrip())
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ", user, "| password: ", str(fer.dencrypt(passw.encode())))

def add():
    name = input('Account name: ')
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
                
while True:
    mode = input('Would you like to add new password or view existing one? (view, add), press Q to quit ').lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print('Invalid mode')