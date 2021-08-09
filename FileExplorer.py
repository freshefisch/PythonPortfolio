import os

#set start variables
start_folderPATH = r"C:\\"
current_folderPATH = r""
new_folderPATH = r""
loop = True

#______________________________________________________________
#MAIN LOOP
while loop:

    #reset current files/folders
    list_of_files = []    

    #get folder contents
    if current_folderPATH == "":
        current_folderPATH = start_folderPATH
        for i in os.listdir(start_folderPATH):
            list_of_files.append(i)

    else:
        current_folderPATH = new_folderPATH
        for i in os.listdir(current_folderPATH):
            list_of_files.append(i)       


    #show folder contents
    print("\n0 ... (up one folder)")
    for i in range(0,len(list_of_files)):
        if i in range(0,9):
            print("  "+(str(i+1))+" -",list_of_files[i])
        elif i in range(9,99):
            print(" "+(str(i+1))+" -",list_of_files[i])
        elif i in range(99,999):
            print((str(i+1))+" -",list_of_files[i])

    #choose folder/file
    input_filenumber = int(input("\nEnter folder/file number: "))


    while not input_filenumber in range(0,(len(list_of_files)+1)):
        print("\nPlease enter a correct number.")
        input_filenumber = int(input("\nEnter folder/file number: "))
    
    #GO BACK
    if input_filenumber == 0:
        print("Chose to go back one folder")
        sep = "\\"
        new_folderPATH = current_folderPATH.rsplit(sep, 1)[0]

    #GO FOREWARD
    else:
        #SET NEW FOLDER
        chosen_file_folder = list_of_files[(input_filenumber-1)]

        #if folder: CHANGE PATH TO CHOSEN FOLDER  
        if not "." in chosen_file_folder:

            print(f"\nYou chose the folder | {chosen_file_folder} |\n")
            
            #set chosen folder to folder for next loop
            new_folderPATH = current_folderPATH + "\\" + chosen_file_folder
            
        #if file: OPEN FILE AND STAY IN CURRENT FOLDER
        else: 
            print("This is a file")
            loop = False
    