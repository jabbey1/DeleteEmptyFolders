import os
import send2trash
import pathlib

def find_empty_directories(dir_path) -> list:
    empty = [root for root, dirs, files, in os.walk(dir_path) 
                   if not len(dirs) and not len(files)]
    return empty

def get_path():
    current_directory = os.getcwd()
    return current_directory

def delete_dirs(empty):
    for dir in empty:
        os.remove(dir)
    

def send_dirs_to_trash(empty):
    for dir in empty:
        send2trash.send2trash(dir)



current_directory = get_path()
empty = find_empty_directories(current_directory)
print(f'Found {len(empty)} empty directories:')
print(empty)
while True:
    answer = input('Would you like to send empty directories to the recycle bin? y/n')
    if answer == 'n':
        while True:
            answer = input('Would you like to permanently delete empty directories? y/n')
            if answer == 'n':
                break
            if answer == 'y':
                delete_dirs(empty)
                break
            else:
                print('Invalid response. Please answer "y" or "n"')
        break
    if answer == 'y':
        send_dirs_to_trash(empty)
        break
    else:
        print('Invalid response. Please answer "y" or "n"')

print('Finished. May need to run again if some directories only contained another empty directory.')