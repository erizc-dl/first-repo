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

command = input("Enter your command: ")

if command in commands:
    print("Valid command")
else:
    while command not in commands:
        print("Invalid command")
        input("Enter your command: ")
    print("Valid command")
