# Exercise 9: Jenkins Multi-Stage Pipeline

## Objective
Build, test, check code quality, deploy, and verify a Python Flask application using Jenkins.

## Technologies
- Jenkins Pipeline
- Python 3
- Flask
- unittest
- flake8
- Docker

## Pipeline stages
1. **Build:** Create a Python virtual environment and install dependencies.
2. **Test:** Run unit tests using unittest.
3. **Code Quality:** Check Python files using flake8.
4. **Deploy:** Copy the application into a deployment directory.
5. **Test Deployed Application:** Start the application and verify its HTTP response.

## Files
- `Jenkinsfile` - Pipeline definition
- `app.py` - Flask web application
- `test_app.py` - Unit tests
- `requirements.txt` - Python dependencies
- `Dockerfile` - Container build instructions
- `.dockerignore` - Files excluded from the Docker build
- `screenshots/` - Evidence of the completed exercise

## Jenkins configuration
- Job type: Pipeline
- Definition: Pipeline script from SCM
- SCM: Git
- Repository: https://github.com/Bad087/DevOps-Lab.git
- Branch: `*/main`
- Credentials: `- none -` for a public repository
- Script Path: `Exercises/9-Python-MultiStage-Pipeline/Jenkinsfile`

## Expected result
All five stages should pass, including the HTTP response verification.

Expected response:
`Hello, Jenkins Multi-Stage Pipeline!`

## Deployment note
The Jenkins pipeline performs a workspace-based demonstration deployment and HTTP check. The Dockerfile is provided for a separate container deployment.
