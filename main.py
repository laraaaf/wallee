import os
from menu import *
from wallee import *

print ("\nWelcome to wallee :)\n\n")

while True:
    print ()
    ans=input("""
    Commands:
    wallee --firstsetup         if this is your first time with wallee
    wallee --generate           generate new wallpaper
    wallee --config             Change configuration of wallee
    wallee --exit               exit wallee
    """) 
    if ans=="wallee --firstsetup": 
        change_path()
                        

    elif ans=="wallee --generate":
        generatePicture()


    elif ans=="wallee --config":
        openConfig()

    elif ans=="wallee --exit":
        print ("Goodbye")
        break

    elif ans !="":
        print("\n Not Valid Choice Try again") 



