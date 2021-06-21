import os

def walk_dir(dir):
    for Path,dirs,filename in os.walk(dir):
        file = []
        a = []
        
        dirr = dirs
        print(Path)
        for Path,dirs,filename in os.walk(dir):
            if dirr == dirs :
                for f in filename:
                    a.append(os.path.splitext(f))
                    for b in a:
                        file.append(b)
            dirr = dirs
    _dir = dict(zip(dirs,file))
    return _dir

dir = input("please input the path:")
non = walk_dir(dir)
print (non)
