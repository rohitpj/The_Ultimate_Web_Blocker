import time
import requests
from datetime import datetime as dt

hosts_path = "/etc/hosts"  # for cringe linux and mac nerds
hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"

# IP address for localhost
redirect = "127.0.0.1"

# the banes of my future career
website_list = ["google.com"]

# replace with ur username
leetcode_api_url = "https://faisal-leetcode-api.cyclic.app/swrlit"

def get_number_of_solved_problems(api_url):
    response = requests.get(api_url)
    data = response.json()
    return data['totalSolved']

# Initially set the current_number_of_solved_problems
current_number_of_solved_problems = get_number_of_solved_problems(leetcode_api_url)

while True:
    # Time period during which to block websites
    #if dt(dt.now().year, dt.now().month, dt.now().day, 3.5) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 3.6):
      
    if dt(dt.now().year, dt.now().month, dt.now().day, 13) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 14):
        print("Blocking websites...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print("Time to unblock, but you must solve a LeetCode problem first...")
        new_number_of_solved_problems = get_number_of_solved_problems(leetcode_api_url)
        
        
        #if new_number_of_solved_problems > current_number_of_solved_problems:
        if new_number_of_solved_problems > current_number_of_solved_problems:
            print("Unblocking websites...")
            with open(hosts_path, 'r+') as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)
                file.truncate()
        else:
            print("Solve a LeetCode problem to unblock websites.")
    
    # Check every 5 minutes
    time.sleep(60)
