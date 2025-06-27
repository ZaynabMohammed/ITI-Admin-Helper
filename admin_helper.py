import subprocess

def execute_command(command):
    """Executes a shell command and returns the output."""
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.decode('utf-8').strip()}"

def admin_helper():
    while True:
        print("\nSelect an option:")
        print("1. Add a new user")
        print("2. Delete user account")
        print("3. Modify user account")
        print("4. Disable user account")
        print("5. Enable user account")
        print("6. Change user password")
        print("7. Delete user account with home directory")
        print("8. Delete user account without home directory")
        print("9. Add a new group")
        print("10. Modify an existing group")
        print("11. List groups")
        print("12. Delete group")
        print("13. Add user to group")
        print("14. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username for new user: ")
            result = execute_command(f"useradd {username}")
            print(f"User {username} added successfully.")
        
        elif choice == '2':
            username = input("Enter username to delete: ")
            result = execute_command(f"userdel {username}")
            print(f"User {username} deleted successfully.")
        
        elif choice == '3':
            username = input("Enter username to modify: ")
            new_username = input("Enter new username: ")
            result = execute_command(f"usermod -l {new_username} -d /home/{new_username} -m {username}")
            print(f"User {username} modified to {new_username} successfully.")
        
        elif choice == '4':
            username = input("Enter username to disable: ")
            result = execute_command(f"usermod -L {username}")
            print(f"User {username} disabled successfully.")
        
        elif choice == '5':
            username = input("Enter username to enable: ")
            result = execute_command(f"usermod -U {username}")
            print(f"User {username} enabled successfully.")
        
        elif choice == '6':
            username = input("Enter username to change password: ")
            password = input("Enter new password: ")
            result = execute_command(f"echo {password} | passwd --stdin {username}")
            print(f"Password for user {username} changed successfully.")
        
        elif choice == '7':
            username = input("Enter username to delete with home directory: ")
            result = execute_command(f"userdel -r {username}")
            print(f"User {username} and home directory deleted successfully.")
        
        elif choice == '8':
            username = input("Enter username to delete without home directory: ")
            result = execute_command(f"userdel {username}")
            print(f"User {username} deleted successfully.")
        
        elif choice == '9':
            groupname = input("Enter group name to add: ")
            result = execute_command(f"groupadd {groupname}")
            print(f"Group {groupname} added successfully.")
        
        elif choice == '10':
            groupname = input("Enter group name to modify: ")
            new_groupname = input("Enter new group name: ")
            result = execute_command(f"groupmod -n {new_groupname} {groupname}")
            print(f"Group {groupname} modified to {new_groupname} successfully.")
        
        elif choice == '11':
            print("List of groups:")
            result = execute_command("cut -d: -f1 /etc/group")
            print(result)
        
        elif choice == '12':
            groupname = input("Enter group name to delete: ")
            result = execute_command(f"groupdel {groupname}")
            print(f"Group {groupname} deleted successfully.")
        
        elif choice == '13':
            username = input("Enter username to add to group: ")
            groupname = input("Enter group name: ")
            result = execute_command(f"usermod -aG {groupname} {username}")
            print(f"User {username} added to group {groupname} successfully.")
        
        elif choice == '14':
            print("Exiting the Administrative Helper...")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    admin_helper()
