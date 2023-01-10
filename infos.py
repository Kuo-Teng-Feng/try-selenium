import os

def _name_all(): # return list.
        
    os.chdir("../for_try-selenium")
    return os.listdir(os.curdir)
    
def getter(): # return dict.
    
    dict = {}
    filenames = _name_all()
    for fn in filenames:
        
        l = []
        with open(f"../for_try-selenium/{fn}", "r") as file:
            for line in file:
                l.append(line)
        dict[fn[0 : -4]] = l
        
    return dict