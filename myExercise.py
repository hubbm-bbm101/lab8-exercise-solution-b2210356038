import sys
names=sys.argv[2]
with open(sys.argv[1],"r") as file:
    lines=file.readlines()
records={}
nameslist=names.split(",")
for line in lines:
    linelist=line.strip().split(":")
    name=linelist[0]
    info=linelist[1]
    records[name]=info
for n in nameslist:
    try:
        print("Name: "+n+", "+"University: "+records[n]+" ")
    except KeyError:
        print("No record of '{}' was found! ".format(n))    
    