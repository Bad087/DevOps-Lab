# Exercise 8 - Hello World Jenkins Job

## Objective
Create a shell script, upload it to GitHub using Git, and execute it using a Jenkins Freestyle job.

## Prerequisites
- Git installed
- Docker Desktop running
- Jenkins running and accessible at http://localhost:8080
- A GitHub repository

## Script
The `hello-world.sh` script contains:

```bash
#!/bin/bash
echo "Hello, Jenkins!"
```

## GitHub Repository
https://github.com/Bad087/DevOps-Lab

## Jenkins Configuration
1. Open Jenkins.
2. Click New Item.
3. Name the job HelloWorld.
4. Select Freestyle project.
5. Configure Git source control with the DevOps-Lab repository URL.
6. Set the branch to */main.
7. Add an Execute shell build step with:

```bash
cd Exercises/8-Hello-World-Jenkins-Job
sh hello-world.sh
```

8. Save the job and click Build Now.

## Expected Output
```text
Hello, Jenkins!
Finished: SUCCESS
```
