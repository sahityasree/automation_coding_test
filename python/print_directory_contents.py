import os

def print_directory_contents(path):
    #dir= "C:\\Users\\Admin\\Desktop\\sahitya\\projects"
    print(path)
    
    files = os.listdir(path)
    print(files)
    for name in files:
        print("the name of file/dir is :")
        print(name) 
        full_path = os.path.join(path, name)
        if(os.path.isdir(full_path)):
            print("it is a directory");
            inn=os.listdir(full_path)
            print("inner paths are")
            for name in inn:
                print(name)
                inner_path = os.path.join(path,full_path, name)
                print("the path of inner file is")
                print(inner_path);
        else:
            print("the path of the file is :")
            
            print(full_path);
            
dir= "C:\\Users\\Admin\\Desktop\\sahitya\\projects"
print_directory_contents(dir)