import threading
import time
def input_function():
    print("Your string is:  ",string)
def reverse_function():
    print("reverse string:  ",string[::-1])
def capitalize_function():
    print("capitalize  string:  ",string.capitalize())
def shift_function():
    data=[]
    for i in string:
        if i.strip() and i in strs:
            data.append(strs[(strs.index(i) + 2) % 26])
        elif i.strip() and i in STRS:
            data.append(STRS[(STRS.index(i) + 2) % 26])
        else:
            data.append(i)
    output=''.join(data)
    print("shifting character:  ",output)


string=input("enter the string:   ")
strs='abcdefghijklmnopqrstuvwxyz'
STRS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
input_function()
reverse_function()
capitalize_function()
shift_function()
t1 = threading.Thread(target=input_function, name='t1')
t2 = threading.Thread(target=reverse_function, name='t2')
t3 = threading.Thread(target=capitalize_function, name='t3')
t4 = threading.Thread(target=shift_function, name='t4')

