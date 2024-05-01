# File System Navigation:
  
1. List files and directories:
  ```
    ls
  ```
2. Change directory:

```
cd directory_name
```

3. Print working directory:
```
pwd
```

4. Make directory:
```
mkdir new_directory
```

5. Remove directory:
```
 rmdir directory_name
```
6. File Operations:

    **Create an empty file:**
```
touch new_file.txt
```

7. Display file content:
```
cat file.txt
```
8. Copy files and directories:

```
cp source_file destination_directory
```
9. Move or rename files and directories:
```
mv old_name new_name
```

10. Remove files and directories:
```
    rm file.txt
```
11. File Permission:

    **Change file permissions:**
```
chmod permissions file_name
```
12. Change file owner and group:
```
chown user:group file_name
```
13. Change group ownership:
```
    chgrp group_name file_name
```
14. Text Processing:

    **Search text patterns in files:**
```

grep pattern file.txt
```
15. Stream editor for text manipulation:
```
sed 's/old_text/new_text/' file.txt
```

16. Pattern scanning and text processing tool:

```
    awk '/pattern/ {print}' file.txt
```
17. System Information:

    **Print system information:**
```
uname -a
```
18. Display disk space usage:

```
df -h
```
19. Display Linux processes:

```
top
```
20. Display amount of free and used memory:

```
    free -m
```
21. Package Management:

    **Package management tools for installing, updating, and removing software packages:**
```
apt-get install package_name
```


22. Networking:

    **Display network interface information:**
```

ifconfig
```

23. Check network connectivity:

```
ping google.com
```
24. Secure Shell for remote access:

```
ssh username@hostname
```
25. Securely copy files between hosts:

```
    scp source_file username@hostname:/destination_directory
```
26. Process Management:

    **Display information about running processes:**

```
ps aux
```

27. Terminate processes by ID or name:

```
kill process_id
```
28. List processes based on name:

```
pgrep process_name
```

Shell Scripting:

  **Make a shell script executable:**
```
chmod +x script.sh
```
29. Execute a shell script:

```

./script.sh

