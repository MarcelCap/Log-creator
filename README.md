# Automatic Log Generator with Python and Docker

This repository contains my first practical mission using Docker and Python. 

The goal of this project is to create an automated script that captures the exact execution time and saves it in a `.txt` log file, all running inside an isolated Docker container.

## 🎯 Objectives
* Set up a Python 3.12 environment using Docker.
* Create a robust `docker-compose.yml` file mapping local volumes.
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
3. Run the following command to build the image and start the container:

```bash
docker-compose up --build
```

4. Check your terminal for the `Hello, world!` message.
5. Look inside the project folder. A new file called `log.txt` will automatically appear containing the exact time of the execution.

## 🧠 What I Learned
During this project, I learned how Docker handles virtualization using WSL 2 on Windows, the importance of using volume mapping (`volumes`) to persist files created inside the container to the host machine, and how context managers (`with open(...)`) work in Python to prevent memory leaks and file corruption.

### 🛡️ Best Practices Applied: .dockerignore
Even though this is a small project, I included a `.dockerignore` file. This is a crucial practice for:
1. **Security:** Preventing sensitive data (like `.env` files or `.git` history) from leaking into the Docker image.
2. **Performance:** Ignoring heavy local folders (like virtual environments) to make the image build process faster and the final image lighter.
3. **Consistency:** Ignoring local `log.txt` files ensures the container always starts with a clean slate, generating logs purely through the configured volume.
