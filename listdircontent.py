import os,argparse
parser=argparse.ArgumentParser(description="python listdircontent.py --depth <depth>\nwhere depth is integer")
parser.add_argument("--depth",type=int,help="depth <int>")
args=parser.parse_args()
depth=args.depth

def lst(name,i):
    print(name)
    data=os.listdir(name)
    for item in data:

        if(os.path.isfile(os.path.join(name,item))):
            print(" "*i+"-"*i+item)
        elif (os.path.isdir(os.path.join(name,item))):
            new=os.path.join(name,item)
            if len(new.split(os.sep))<=depth:
                j=i+1
                lst(new,j)
            else:
                print(new)

if __name__=="__main__":
    dirname=input("Enter the dirname:")
    lst(dirname,1)

            
