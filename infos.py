import os

def _name_all(): # return list.
        
    os.chdir("../for_try-selenium")
    return os.listdir(os.curdir)
    
def getter(): # return dict.
    
    dict = {}
    filenames = _name_all()
    for fn in filenames:
        
        if fn[len(fn) - 3:] != 'txt':
            continue
        l = [] # "encoding="utf-8" must be added to avoid UnicodeDecodeError.
        with open(f"../for_try-selenium/{fn}", "r", encoding="utf-8") as file:
            for line in file:
                l.append(line.strip())
        dict[fn[0 : -4]] = l
        
    return dict

