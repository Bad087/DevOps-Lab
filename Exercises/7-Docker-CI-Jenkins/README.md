# Exercise 7 - Introduction to CI and Jenkins Installation

## Objective
Install Jenkins using Docker and create a basic Continuous Integration (CI) pipeline.

## Tools Used
- Docker Desktop
- Jenkins (LTS)
- Git
- GitHub
- PowerShell

## Jenkins Installation
Jenkins was run as a Docker container with persistent storage using the `jenkins_home` Docker volume.

Ports used:
- `8080`: Jenkins web interface
- `50000`: Jenkins agent communication

## CI Pipeline Stages
1. **Checkout:** Retrieve the repository source code.
2. **Validate Exercise Files:** Check that the required Exercise 7 files exist.
3. **CI Verification:** Print a success message when validation completes.

## Project Structure
```text
Exercises/
└── 7-Docker-CI-Jenkins/
    ├── README.md
    ├── Jenkinsfile
    └── screenshots/
```

## Running Jenkins
Open the Jenkins dashboard at:

http://localhost:8080

## Verification
The pipeline should complete successfully after the repository URL, branch, and Jenkinsfile path are configured correctly.

## Screenshots
The `screenshots/` directory contains evidence captured during Jenkins setup and pipeline configuration.
