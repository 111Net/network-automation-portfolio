import os

aliases = """

# Custom Aliases
alias gs='git status'
alias gp='git pull'
alias ll='ls -lah'
alias py='python3'
alias venv='python3 -m venv venv'

"""

bashrc_path = os.path.expanduser("~/.bashrc")

with open(bashrc_path, "a") as file:
    file.write(aliases)

print("Aliases added successfully!")

os.system("source ~/.bashrc")
