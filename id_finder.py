inp = input("element copy: ")
print(inp[inp.index('id="') + 4 : inp.index('"', inp.index('id="') + 5)])
