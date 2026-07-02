# Docker will read this file and create the container
# based on the instructions below.

# It will use the following image as the interpreter, so there's no need
# to download instances manually. This sets up the environment.
# I used python 3.12-slim to optimize processing when creating the container.
FROM python:3.12-slim

# Defines the workspace/where the app will be executed.
WORKDIR /app

# What to copy into the container.
# The 1st '.' means the current folder on Windows.
# The 2nd '.' means the /app folder inside the container.
# Syntax: copy source dest
COPY . .

# ENTRYPOINT: The fixed command that doesn't change. 
# Command the container will execute right after it starts.
# The container will always run the Python interpreter in this achive.
# This command capture the flags '--create' and '--delete'
ENTRYPOINT ["python", "-u", "app/main.py"]
