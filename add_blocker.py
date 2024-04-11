import time 
import random
from nextdnsapi.api import *

login = input("Email: ")
passwrd = input("Passwrd: ") 

header = account.login(login, passwrd)
print(account.list(header))
config = input("id: ")

file_name = input("database: ")
with open(file_name, 'r') as saved_domains:

    for i in saved_domains:
        print("adding:", str(i))
        timer = random.randint(1,4)
        time.sleep(int(timer))
        a = denylist.blockdomain(i.strip(), config, header)
        print(a)