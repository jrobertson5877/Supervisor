# SUPERVISOR

Basic python script that will monitor a file for deletion or removal. If the file dissapears than the script will rewrite the file, compile it if needed, and execute it. 

In our test case I simply use a reverse shell backdoor program written in C. The script uses gcc to recompile the copy and execute. 

