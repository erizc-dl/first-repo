"""Top commands in Git classified in a list."""

commands = [
    "git init", 
    "git clone", 
    "git add", 
    "git commit", 
    "git status", 
    "git branch", 
    "git merge", 
    "git pull", 
    "git push"]

list_of_commands = "Top Git Commands: \n1. git init \n2. git clone \n3. git add \n4. git commit \n5. git status \n6. git branch \n7. git merge \n8. git pull \n9. git push \n"
print(list_of_commands)

command = input("Enter your command (1-9): ")

if command in commands:
    print("Valid command")
else:
    while command not in commands:
        print("Invalid command")
        input("Enter your command: ")
    print("Valid command")
