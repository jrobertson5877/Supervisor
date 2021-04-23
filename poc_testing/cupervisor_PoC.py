#/usr/bin/python


import time
import os
import subprocess
from subprocess import call

def main():
    
    startTime = time.time()
    
    childPath = "/root/Documents/0x80/red/case_studies/supervisor/test_env/config"    #"/home/fungi/.vim/install"
    childPathParent = childPath.rpartition('/')[0]
    while True:
        print ("[!] Checking to see if child still exists at {} [!]".format(childPath))
        
        time.sleep(10.0 - ((time.time() - startTime) % 10.0))
        
        if os.path.exists(childPath):
            print ("[!] Child at {} exists [!]".format(childPath))
        else:
            print ("[!] Child at {} does not exist [!]".format(childPath))
            if not os.path.exists(childPathParent):
                print ("[!] Parent directory of child at {} not found, creating... [!]".format(childPathParent))
                os.makedirs(childPathParent)
            print ("[!] Writing c program to config.c at {} [!]".format(childPath))
            with open ('config.c', 'w') as child:
                child.write('''\
                #include <stdio.h>
                #include <stdlib.h>
                
                int main() {
                    printf("Hello! Im the c script executing!");
                    exit(0);
                }
                ''')
            print("[!] compiling config.c to config [!]")
            call(["gcc", "-o", "config", "config.c"])
            print("[!] removing config.c [!]")
            call(["rm", "-f", "config.c"])
            print("[!] moving config to {} [!]".format(childPathParent))
            call(["mv", "config", childPathParent])
            print("[!] calling ./config [!]")
            call([childPath])           


if __name__ == "__main__":
    main()
