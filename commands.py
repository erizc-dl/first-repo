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

list_of_commands = (
    "Top Git Commands:\n"
    "1. git init\n"
    "2. git clone\n"
    "3. git add\n"
    "4. git commit\n"
    "5. git status\n"
    "6. git branch\n"
    "7. git merge\n"
    "8. git pull\n"
    "9. git push\n"
)

print(list_of_commands)

# Asks the user for a command
command = input("Enter your command (1-9): ")

# Validate user's input
while not command.isdigit() or not (1 <= int(command) <= 9):
    command = input("Invalid input. Enter a number between 1 and 9: ")

# Transform input to index
index = int(command) - 1

# Return final command
selected_command = commands[index]
print(f"You've selected {selected_command}.")
