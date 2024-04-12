import win32gui

def rename_window(new_name, old_name):
    try:
        handle = win32gui.FindWindow(None, old_name) # Get the window
        win32gui.SetWindowText(handle, new_name) # Set the window title

    except Exception as e:
        print(f"An error occured, {e}")
try:
    file = open("new_name.cum", "r")
    file_2 = open("old_name.cum", "r")

    new_name = file.read().strip()
    old_name = file_2.read().strip()

    file.close()
    file_2.close()

except:
    print("Missing settings file, creating a new one")
    file = open("new_name.cum", "w")
    file_2 = open("old_name.cum", "w")

    print("To bring this setup up, just delete the name.cum file \n")

    old_name = input("What is the name of the window you want to rename? ")
    new_name = input("What should the window be renamed to? ")

    file.write(new_name)
    file_2.write(old_name)

    file.close()
    file_2.close()

rename_window(new_name, old_name)