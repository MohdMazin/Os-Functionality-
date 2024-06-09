import os

# Printing the current working directory
print("Current Working Directory:", os.getcwd())

# Function to create a folder
def crfol():
    ask1 = input("Want to make a folder? (Y/N): ").upper()
    if ask1 == "Y":
        global namfol_1
        namfol_1 = input("Enter the name of the folder you want: ")
        try:
            os.mkdir(namfol_1)
            print(f"Folder '{namfol_1}' has been created successfully!")
        except FileExistsError:
            print(f"Folder '{namfol_1}' already exists.")

# Function to delete a folder
def delfol():
    ask2 = input("Enter the name of the folder you want to delete: ")
    if os.path.exists(ask2) and os.path.isdir(ask2):
        os.rmdir(ask2)
        print(f"Folder '{ask2}' has been deleted successfully!")
    else:
        print("Invalid input. Please try again later!")

# Ask the user for the function they want to perform
print("TELL THE FUNCTION YOU WANT TO PERFORM")
print("CREATE, DELETE")

mainask = input("Enter the function you want to perform: ").upper()
if mainask == "CREATE":
    crfol()
elif mainask == "DELETE":
    delfol()
else:
    print("Invalid function selected!")

# Finding the path of the folder
def pathask():
    ask3 = input("Enter the name of the folder you made: ")
    if 'namfol_1' in globals() and ask3 == namfol_1:
        full_path = os.path.join(os.getcwd(), namfol_1)
        print(f"The path of the folder '{namfol_1}' is: {full_path}")
    else:
        print("No such folder was created.")

# Optionally call pathask() to find the path of the created folder
try:
    askpath = input("Want to find the location of the folder or not? (Y/N): ").upper()
    if askpath == "Y":
        pathask()
except Exception as e:
    print("An error occurred: ", e)




    



    
    
        


