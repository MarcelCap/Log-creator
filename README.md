# Automatic Log Generator with Python and Docker

This repository contains my first practical mission using Docker and Python. 

The goal of this project is to create an automated script that captures the exact execution time and saves it in a `.txt` log file, all running inside an isolated Docker container.

The application now features a Command-Line Interface (CLI) allowing users to dynamically choose between creating/updating logs and deleting the log file.

## 🎯 Objectives
* Set up a Python 3.12 environment using Docker.
* Create a robust `docker-compose.yml` file mapping local volumes.
* Utilize `ENTRYPOINT` and argument parsing (`sys.argv`) for interactive execution.
* Apply PEP 8 formatting standards to the Python code.
* Use the **Rubber Ducking** technique to comment and explain the *why* behind every block of code.

## 🛠️ Technologies Used
* **Python 3.12** (Slim version for lighter containerization)
* **Docker**
* **Docker Compose**

## 🚀 How to Run the Project

### Prerequisites
Make sure you have [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running on your machine.

### Step-by-Step

1. Clone this repository to your local machine.
2. Open your terminal and navigate to the project folder.
3. Build the image first by running:

```bash
docker-compose build
```

4. **To Create or Append a Log:**
Run the container passing the `--create` flag. A new `log.txt` file will automatically appear (or update) in your local folder:

```bash
docker-compose run my_python_app --create
```

5. **To Delete the Log File:**
Run the container passing the `--delete` flag. The `log.txt` file will be safely removed from your local folder:

```bash
docker-compose run my_python_app --delete
```

*Note: If you run the container without any flags, it will print a helpful menu showing the available commands.*

## 🧠 What I Learned
During this project, I learned how Docker handles virtualization using WSL 2 on Windows, the importance of using volume mapping (`volumes`) to persist files created inside the container to the host machine, and how context managers (`with open(...)`) work in Python to prevent memory leaks. I also explored how `ENTRYPOINT` differs from `CMD` in Dockerfiles, allowing the container to act as a command-line executable.

### 🛡️ Best Practices Applied: .dockerignore
Even though this is a small project, I included a `.dockerignore` file. This is a crucial practice for:
1. **Security:** Preventing sensitive data (like `.git` history) from leaking into the Docker image.
2. **Performance:** Ignoring heavy local folders to make the image build process faster and the final image lighter.
3. **Consistency:** Ignoring local `log.txt` files ensures the container always starts with a clean slate, generating logs purely through the configured volume.
