import getpass
import os
import json
import pathlib
USER_NAME = getpass.getuser()


def change_config(key,value):
    #get config-datas
    try:
        with open('config.json') as f:
            data = json.load(f)
        f.close()
    
        #change config-datas
        print(f"{data[key]} to")
        data[key]=value
        f = open('config.json','w')
        json.dump(data,f)
        print(data[key])
        

    except:
        print("Error reading json File")

def change_path():
    path = input("\nPlease Input your Path:")
    if os.path.exists(path):
        change_config("path",path)
    else:
        print("Could not find Path")

def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'''cd "%s"
        python -c "from wallee import*; generatePicture()"''' % file_path)
    change_config("autostart",True)
    change_config("walleepath",file_path)


def delete_from_startup():
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\open.bat' % USER_NAME
    if os.path.exists(bat_path):
        os.remove(bat_path)
    change_config("autostart",False)
    change_config("walleepath","")


def openConfig():
    while True:
        print ("""
        1.Change Path
        2.Change max Pictures
        3.Change Autostart
        4.Exit/Quit
        """)
        ans=input("What would you like to do?") 
        if ans=="1": 
            change_path()
                

        elif ans=="2":
            answer = input("\nPlease input max Pictures:")
            if (int(answer)>0):
                change_config("maximage",int(answer))
                print("Changed max Pictures")

            else:
                print("Input is not integer")

        elif ans=="3":
            answer = input("Should the Script be in Autostart? [y/n]:")
            if answer == "y":
                wpath = f"{pathlib.Path(__file__).parent.absolute()}"
                add_to_startup(wpath)
                print("Added to autostart")
            elif answer == "n":
                print("Deleted from Autostart")
                delete_from_startup()
        
        elif ans=="4":
            break

        elif ans !="":
            print("\n Not Valid Choice Try again") 


#delete_from_startup()