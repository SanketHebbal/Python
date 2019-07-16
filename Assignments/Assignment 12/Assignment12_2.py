import sys
import psutil
import argparse


def DisplayProcessInfo(processname):

    try:
        for proc in psutil.process_iter():

            p = proc.as_dict(attrs=['pid','name','username','exe','status'])

            if p['status'] == 'running':
                if processname.lower() in p['name'].lower():
                    print(p)
                    return

        print(processname+" process is not in running state")                       
    except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
        pass

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-d", help = "short description about script" , action="store_true")
    parser.add_argument("processname",help="Name of process of which you want information")

    args = parser.parse_args()

    if args.d:
        print("This script display the information of given process")
            
    try:
        if args.processname:
            DisplayProcessInfo(sys.argv[1])
    except Exception as e:
        print("Error :",e)


    
if __name__ == "__main__":

    main()
