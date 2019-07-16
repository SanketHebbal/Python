import sys
import psutil

def DisplayProcess():

    processInfo = list()

    for proc in psutil.process_iter():
        try:
            
           info = proc.as_dict(attrs=['pid','name','username'])
           processInfo.append(info)
           
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    return processInfo

def main():

    try:
        
        processInfo = DisplayProcess()
        for process in processInfo:
            print(process)
            
    except Exception as e:
        print("Error :",e)

if __name__ == "__main__":
    main()
