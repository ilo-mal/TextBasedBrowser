import sys
import os
from collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import Fore

args = sys.argv
user_entry = args[1]   # please provide folder name

path = os.path.join(user_entry)
if not os.path.exists(path):  # create folder and checks if it's doesn't exist already
    os.makedirs(path)
options = input("Put URL address:")
my_stack = []


def input_strip(opt):
    to_strip = ['https://', 'https://www.', 'http://', 'http://www.', 'www.']
    for x in to_strip:
        if opt.startswith(x):
            opt = opt.replace(x, '')
    return opt


options = input_strip(options)


def my_serch(url):
    url_all = 'http://' + url
    headers = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url_all)           # r = requests.get(url, headers=headers)
    styled = BeautifulSoup(r.content, 'html.parser')
    attr = styled.find_all(['h1', 'h2', 'a', 'p'])
    out = ''
    for at in attr:
        out += at.text + '\n'
    return out


def file_write():
    path_file = options.partition('.')[0]
    with open(os.path.join(path, path_file), 'w+') as any_web:
        kol = my_serch(options)
        print(Fore.BLUE + kol)
        for _chunk in my_serch(options):
            return any_web.write(my_serch(options))


def file_open():
    with os.scandir(path) as dirs:  # checks if file in directory
        for x in dirs:
            if x.name == options:
                print(open(os.path.join(path, options), 'r').read())


def go_back():
    if len(my_stack) > 0:
        my_stack.pop()
        if len(my_stack) > 0:
            print(open(os.path.join(path, my_stack[-1]), 'r').read())


def my_help():
    print('''
    1. You can put url address as example: "yahoo.com"
    2. To go back to previous page please write "back"
    3. Each time you will go to website it content will be saved in file named after 
        website e.g. "yahoo"
    4. To read downloaded page file please write file name as per example: "yahoo"
    ''')


while options != 'exit':
    if '.' in options:
        my_stack.append(options.partition('.')[0])
        file_write()
    elif options == 'back':
        go_back()
    elif options == 'help':
        my_help()
    elif os.path.isfile(os.path.join(path, options)):
        file_open()
    elif not os.path.isfile(os.path.join(path, options)):
        print("There is some error in your URL, please try again:")

    options = input("Put URL address:")
