# initial deployment - MVP
## Tasks
- 1 host all the files in the frontend/ folder under port 8080 with a simple python http server
- 1b set up a silence logging option 
- 2 create a deployment script (bash/python)
- 3 create a test script that tests the functionality of the following page: /help.html
    filter for API keys in the form: API|XXXXXXXX
- 3b some of them will be a BASE64 encoded
- 4 make the script run every day authomatically (cron or scheduler of your choice)
- 5 make the script run at the end of deployment with a 10 second delay
- 6 put all of these in a docker container
- 6b have an alpine base container
## Requirements
- deployment scripts with bash AND python in a single script, both configurable with ENVIRONMENT VARIABLES (port, folder, if its background, logging, ...)
- document at least one flag/feature, add the option to override the above env variables with command line arguments in at least one version (python or bash)
- the B tasks are optional but recommended
- add the printing of the company logo at the start for copyright reasons (logo.txt)
## Tools
python, python HttpServer module, curl, grep, cron, docker basics