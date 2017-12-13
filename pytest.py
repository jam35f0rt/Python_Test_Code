'''
import time
import webbrowser
time.sleep(2)
webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
time.sleep(3)
webbrowser.exit()
'''
import os
def rename_file():
    pathworking = os.getcwd()
    file_list = os.listdir(r'C:\Users\James_FORT\Desktop\test')
    os.chdir(r'C:\Users\James_FORT\Desktop\test')
    for file in file_list:
        print('old file name '+ file)
        print('new file name '+ file.translate({ord(n): None for n in '1234567890'}))
        os.rename(file, file.translate({ord(n): None for n in '1234567890'}))
        #os.rename(file, file.translate({ord('b'):'fu' , ord('f'):'Fort' , ord('a'):'James' , ord('1'):None}))
    os.chdir(pathworking)
rename_file()

a='1'
print(ord(a))
