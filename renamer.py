import os

def rename_files():
    #Setup file paths (Script should be in the same path of the folders)
    folder=input("What is the name of the folder you want to rename: ")
    file_list = os.listdir("C:/Users/cfmor/Desktop/work/Test/banknotes/"+ str(folder))
    print(file_list)
    path = os.getcwd()
    print("Images Directory: " + path)
    os.chdir("C:/Users/cfmor/Desktop/work/Test/banknotes/"+ str(folder))
    
    #Rename files
    n=0
    for file_name in file_list:
        os.rename(file_name, str(folder)+"_"+str(n)+".jpg")
        n += 1
    
if __name__ == '__main__':
    rename_files()
    print("Done")