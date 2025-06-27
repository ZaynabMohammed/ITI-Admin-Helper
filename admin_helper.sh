#!/bin/bash

# Administrative helper - take an option from user and perform a task.

select choice in "Add a new user" "Delete user account" "Modify user account" "Disable user account" "Enable user account" "Change user password" "Delete user account with home directory" "Delete user account without home directory" "Add a new group" "Modify an existing group" "List groups" "Delete group" "Add user to group" "Exit"; do
    case $REPLY in
        1)
            read -p "Enter username for new user: " username
            useradd "$username"
            echo "User $username added successfully."
            ;;
        2)
            read -p "Enter username to delete: " username
            userdel "$username"
            echo "User $username deleted successfully."
            ;;
        3)
            read -p "Enter username to modify: " username
            read -p "Enter new username: " new_username
            usermod -l "$new_username" -d "/home/$new_username" -m "$username"
            echo "User $username modified to $new_username successfully."
            ;;
        4)
            read -p "Enter username to disable: " username
            usermod -L "$username"
            echo "User $username disabled successfully."
            ;;
        5)
            read -p "Enter username to enable: " username
            usermod -U "$username"
            echo "User $username enabled successfully."
            ;;
        6)
            read -p "Enter username to change password: " username
            read -s -p "Enter new password: " password
            echo "$password" | passwd --stdin "$username"
            echo "Password for user $username changed successfully."
            ;;
        7)
            read -p "Enter username to delete with home directory: " username
            userdel -r "$username"
            echo "User $username and home directory deleted successfully."
            ;;
        8)
            read -p "Enter username to delete without home directory: " username
            userdel "$username"
            echo "User $username deleted successfully."
            ;;
        9)
            read -p "Enter group name to add: " groupname
            groupadd "$groupname"
            echo "Group $groupname added successfully."
            ;;
        10)
            read -p "Enter group name to modify: " groupname
            read -p "Enter new group name: " new_groupname
            groupmod -n "$new_groupname" "$groupname"
            echo "Group $groupname modified to $new_groupname successfully."
            ;;
        11)
            echo "List of groups:"
            cut -d: -f1 /etc/group
            ;;
        12)
            read -p "Enter group name to delete: " groupname
            groupdel "$groupname"
            echo "Group $groupname deleted successfully."
            ;;
        13)
            read -p "Enter username to add to group: " username
            read -p "Enter group name: " groupname
            usermod -aG "$groupname" "$username"
            echo "User $username added to group $groupname successfully."
            ;;
        14)
            echo "Exiting the Administrative Helper..."
            exit 0
            ;;
        *)
            echo "Invalid option. Please try again."
            ;;
    esac
done