import time
from datetime import datetime as dt

# C:\Windows\System32\drivers\etc\hosts
hosts_test = "hosts"
hosts_file = r"C:\Windows\System32\drivers\etc"
web_list = ["facebook.com", "www.facebook.com", "pudelek.pl", "www.pudelek.pl"]
redirect = "127.0.0.1"


while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 12):
        with open(hosts_file, 'r+') as file:
            content = file.read()
            for web in web_list:
                if web in content:
                    pass
                else:
                    file.write(redirect + ' ' + web + '\n')

        print("working hours!")
    else:
        with open(hosts_file, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(web in line for web in web_list):
                    file.write(line)
            file.truncate()

        print("Fun time!")

    time.sleep(10)
