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
    "git push",
    "git config"]

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
    "10. git config"
)

command_purpose = [
    "git init: initializes a brand new Git repository and begins tracking an existing directory. It adds a hidden subfolder within the existing directory that houses the internal data structure required for version control.",
    "git clone: creates a local copy of a project that already exists remotely. The clone includes all the project's files, history, and branches.",
    "git add: stages a change. Git tracks changes to a developer's codebase, but it's necessary to stage and take a snapshot of the changes to include them in the project's history. This command performs staging, the first part of that two-step process. Any changes that are staged will become a part of the next snapshot and a part of the project's history. Staging and committing separately gives developers complete control over the history of their project without changing how they code and work.",
    "git commit: saves the snapshot to the project history and completes the change-tracking process. In short, a commit functions like taking a photo. Anything that's been staged with git add will become a part of the snapshot with git commit.",
    "git status: shows the status of changes as untracked, modified, or staged.",
    "git branch: shows the branches being worked on locally.",
    "git merge: merges lines of development together. This command is typically used to combine changes made on two distinct branches. For example, a developer would merge when they want to combine changes from a feature branch into the main branch for deployment.",
    "git pull: updates the local line of development with updates from its remote counterpart. Developers use this command if a teammate has made commits to a branch on a remote, and they would like to reflect those changes in their local environment.",
    "git push: pdates the remote repository with any commits made locally to a branch.",
    "git config: creates an alias for contributor and commands."
]
print(list_of_commands)

# Asks the user for a command
command = input("Enter your command (1-10): ")

# Validate user's input
while not command.isdigit() or not (1 <= int(command) <= 10):
    command = input("Invalid input. Enter a number between 1 and 10: ")

# Transform input to index
index = int(command) - 1

# Return final command
selected_command = commands[index]
print(f"You have selected {selected_command}.")

# Print out the description of commands
print(command_purpose[index])