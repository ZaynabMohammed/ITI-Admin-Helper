# Administrative Helper

This project contains two versions of a command-line tool to manage Linux user and group accounts:

- A **Bash script** using a `select` menu
- A **Python script** using `subprocess` for command execution

## Features

Both scripts support the following administrative tasks:

1. Add a new user  
2. Delete user account  
3. Modify user account  
4. Disable user account  
5. Enable user account  
6. Change user password  
7. Delete user account with home directory  
8. Delete user account without home directory  
9. Add a new group  
10. Modify an existing group  
11. List all groups  
12. Delete a group  
13. Add user to a group  
14. Exit  

---

## 🖥 Bash Version

### File
`admin_helper.sh`

### Usage
```bash
chmod +x admin_helper.sh
sudo ./admin_helper.sh
