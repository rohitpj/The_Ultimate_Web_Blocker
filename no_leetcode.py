import time
from datetime import datetime as dt

# Hosts file path
hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts" 

# IP address for localhost
redirect = "127.0.0.1"

# List of websites to block
website_list = ["https://www.bbc.co.uk/news/business-66019291","random_test.com","google.com"]

while True:
    # Time period during which to block websites
    if dt(dt.now().year, dt.now().month, dt.now().day, 4) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 5):
        print("Blocking websites...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print("Unblocking websites...")
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

    # Check every 5 seconds
    time.sleep(30)
