import time
import requests
from datetime import datetime as dt
from cryptography.fernet import Fernet
import os

#hosts_path = "/etc/hosts" for linux/mac
hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"
leetcode = False
fileEncryption = False
file_locations=[]
key_locations=[]

# localhost
redirect = "127.0.0.1"

# the banes of my future career
website_list = ["google.com"]

# replace with your username
leetcode_api_url = "https://faisal-leetcode-api.cyclic.app/swrlit"

def get_number_of_solved_problems(api_url):
    response = requests.get(api_url)
    data = response.json()
    return data['totalSolved']

def encrypt_file(file_location):
    encryption_key = Fernet.generate_key()
    cipher_suite = Fernet(encryption_key)
    with open(file_location, 'rb') as file:
        file_data = file.read()

    encrypted_data = cipher_suite.encrypt(file_data)

    encrypted_file_location = file_location + '.encrypted'
    with open(encrypted_file_location, 'wb') as file:
        file.write(encrypted_data)
    
    # Save the key to a file
    key_file_location = file_location + '.key'
    with open(key_file_location, 'wb') as file:
        file.write(encryption_key)
    
    # Append the encrypted file location and key location to the lists
    file_locations.append(encrypted_file_location)
    key_locations.append(key_file_location)

    print(f'File encrypted and saved as {encrypted_file_location}')
    print(f'Encryption key saved as {key_file_location}')

    #FILE IS DELETED HERE commented for safety uncomment if ur the same as above

    #os.remove(file_location)
    #print(f'Original file {file_location} has been deleted.')

def decrypt_file(encrypted_file_location, key_location):
    with open(key_location, 'rb') as file:
        encryption_key = file.read()
    
    cipher_suite = Fernet(encryption_key)
    
    with open(encrypted_file_location, 'rb') as file:
        encrypted_data = file.read()

    decrypted_data = cipher_suite.decrypt(encrypted_data)
    
    # Remove the '.encrypted' extension from the encrypted_file_location
    original_file_location = encrypted_file_location.rsplit('.encrypted', 1)[0]

    # Save the decrypted data back to the original location
    with open(original_file_location, 'wb') as file:
        file.write(decrypted_data)
    
    os.remove(encrypted_file_location)
    print(f'Encrypted file {encrypted_file_location} has been deleted.')
    
    # Delete the key file
    os.remove(key_location)
    print(f'Key file {key_location} has been deleted.')

    print(f'File decrypted and saved as {original_file_location} encrypted file and key has been deleted.')


def decrypt_all_files(file_locations, key_locations):
    print("Your files are at ", file_locations)
    print("Your keys are at ", key_locations)
    if len(file_locations) != len(key_locations):
        print("Error: The number of file locations and key locations must be the same.")
        return
    
    for file_location, key_location in zip(file_locations, key_locations):
        decrypt_file(file_location, key_location)

# Initially set the current_number_of_solved_problems
current_number_of_solved_problems = get_number_of_solved_problems(leetcode_api_url)

blockingTime = int(input("How many hours do you want to block websites? Whole hours only sry :( "))

if input("Add Leetcode puzzle? type YES if so") == "YES":
    leetcode = True

if input("Do you want to put up some files as a guarantee? type YES is so\nWARNING DO NOT DO THIS IF YOU DO NOT TRUST THIS CODE OR ME OR IF THE DOCUMENTS ARE VALUABLE I'LL FEEL VERY BAD IF YOU LOSE THEM :(") == "YES":
    fileEncryption = True

if fileEncryption:
    done = False
    while not done:
        file_location = input("Where is the file location? Type DONE when finished. ")
        if file_location != "DONE":
            encrypt_file(file_location)
        else:
            done = True

end_time = (dt.now().hour + blockingTime) % 24
while True:
    #if dt(dt.now().year, dt.now().month, dt.now().day, dt.now().hour) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, end_time):
    if 1==2:
        print("Blocking websites...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        if leetcode:
            print("Time to unblock, but you must solve a LeetCode problem first...")
            new_number_of_solved_problems = get_number_of_solved_problems(leetcode_api_url)
            if new_number_of_solved_problems > current_number_of_solved_problems:
                print("Unblocking websites...")
                with open(hosts_path, 'r+') as file:
                    content = file.readlines()
                    file.seek(0)
                    for line in content:
                        if not any(website in line for website in website_list):
                            file.write(line)
                    file.truncate()
            if fileEncryption:
                decrypt_all_files(file_locations, key_locations)
            else:
                print("Solve a LeetCode problem to unblock websites.")

        elif fileEncryption:
            decrypt_all_files(file_locations, key_locations)
            
        else:
            print("Unblocking websites...")
            with open(hosts_path, 'r+') as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)
                file.truncate()

    # Check every 5 minutes
    time.sleep(60)
