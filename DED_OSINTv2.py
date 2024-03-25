import os
import time

# Function to create the folder and text files
def create_files():
    folder_path = os.path.join(os.path.expanduser('~'), 'Documents', 'DED_OSINT')
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Create Data.txt for logging valid commands
    with open(os.path.join(folder_path, 'Data.txt'), 'a') as f:
        f.write("Valid Commands Log:\n")
    
    # Create Errors.txt for logging invalid commands
    with open(os.path.join(folder_path, 'Errors.txt'), 'a') as f:
        f.write("Invalid Commands Log:\n")

def log_command(command):
    folder_path = os.path.join(os.path.expanduser('~'), 'Documents', 'DED_OSINT')
    with open(os.path.join(folder_path, 'Data.txt'), 'a') as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}: {command}\n")

def log_error(command):
    folder_path = os.path.join(os.path.expanduser('~'), 'Documents', 'DED_OSINT')
    with open(os.path.join(folder_path, 'Errors.txt'), 'a') as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}: {command}\n")

def print_menu():
    print("________  ___________________         ________    _________.___ __________________")
    print("\______ \ \_   _____/\______ \        \_____  \  /   _____/|   |\      \__    ___/")
    print(" |    |  \ |    __)_  |    |  \        /   |   \ \_____  \ |   |/   |   \|    |   ")
    print(" |    `   \|        \ |    `   \      /    |    \/        \|   /    |    \    |   ")
    print("/_______  /_______  //_______  /      \_______  /_______  /|___\____|__  /____|   ")
    print("        \/        \/         \/               \/        \/             \/         ")
    print("                                                                 Version: 1.0.0.2 ")
    print("                                                                                  ")
    print("                                                                                  ")
    print("[1] Attack IP                                                                     ")
    print("[2] Attack URL                                                                    ")
    print("[3] Botnet Startup                                                                ")
    print("[4] Check Vulnerabilities                                                         ")
    print("[5] Check IP                                                                      ")
    print("[6] Discord Lookup                                                                ")
    print("[7] Emulate Bluetooth                                                             ")
    print("[8] Find Data                                                                     ")
    print("[9] Find URL IP                                                                   ")
    print("[10] Find Discord Key [COMING SOON]                                               ")
    print("[12] Flipper Zero App Download                                                    ")
    print("[13] Get URL IP                                                                   ")
    print("[14] Get Short URL Origin                                                         ")
    print("[15] Hash Cracker                                                                 ")
    print("[16] Hash Generator                                                               ")
    print("[17] Join The Discord                                                             ")
    print("[18] Kill Task                                                                    ")
    print("[19] Manage Logs                                                                  ")
    print("[20] Ping Test                                                                   ")

def main():
    create_files()
    print_menu()
    command_number = input("Type Command Number: ")

    valid_commands = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    if command_number in valid_commands:
        log_command(command_number)
        print("Valid command entered. Logged in Data.txt.")
    else:
        log_error(command_number)
        print("Invalid command entered. Logged in Errors.txt.")
        
        commando = ('1')
        commandt = ('2')
        commandth = ('3')
        commandf = ('4')
        commandfi = ('5')
        commands = ('6')
        commandse = ('7')
        commande = ('8')
        commandn = ('9')
        commandt = ('10')
        commandel = ('11')
        commandtw = ('12')
        commandthi = ('13')
        commandfou = ('14')
        commandfif = ('15')
        commandsix = ('16')
        commandsev = ('17')
        commandeih = ('18')
        commandnin = ('19')
        commandtwen = ('20')
        
        if command_number in commando:
            

if __name__ == "__main__":
    main()
