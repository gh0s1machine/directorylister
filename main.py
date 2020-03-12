from datetime import date
import os
import getpass


# Works on macos
# This is by no means advanced in anyway
# It's meant for coding practice


def todays_date():
    d = date.today()
    td = f"{d.month}/{d.day}/{d.year}"
    return td


# simple input function
def get_dir_name():
    d = input('Enter Directory Name: ')
    return d


dir_name = get_dir_name()

current_user = getpass.getuser() # gets the current user's name
root_path = f'/Users/{current_user}' # path for current user home directory

whole_path = f'{root_path}/{dir_name}'



# creates directory to change to from root path directory you entered
#def dir_to_change_to(base_path, dir_name):
#    whole_path = f'{base_path}/{dir_name}'
#    return whole_path


#my_path = dir_to_change_to(root_path, get_dir_name()) # holds the directory to change to in a new variable
current_dir = os.chdir(whole_path) # changes to the directory
dir_items = os.listdir() # lists items in that directory



# cleans up the look in the terminal
print('\n')
print("Today's date is: " + todays_date())
print("-------------------------------------------- \n")
print(f"You are in: {os.getcwd()}")
print("-------------------------------------------- \n")
print(f"You have: {len(dir_items)} items in this directory")
print("-------------------------------------------- \n")
print("This directory contains...")
print("-------------------------------------------- \n")


# for loop to list each item in the directory on a new line
for item in dir_items:
    print(f"{item} \n")

print("-------------------------------------------- \n")



