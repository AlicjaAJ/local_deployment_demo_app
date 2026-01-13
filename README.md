<<<<<<< HEAD
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
=======
## Simple local deployment tool
# Description
This is a simple local deployment tool created for educational purposes (I am not a professional. It is not intended to be a ready-to-use product.) This simple tool can be used to check for the presence of both plain and base64 encoded API keys in the local server script.
The API keys used in this project are not real, and they form is only an example of the possible API syntax. To make the syntax suitable for a wider forms of APIs it is enough to update their regax in response.py.
# Setting up crone
The tool is crone-friendly. In case you would like the script to run periodically (idk why you would, but sure buddy) it is enough to edit your local crontap and provide the path to deploy_cron.sh, as follows:
'''
0 23 * * * /path/to/deploy_cron.sh
'''
Everyday at 11 pm the tool will host a server with a host and port specified in your environmental variables (.env) and scan it for API keys. In case if port or host are not specified, server.py choses a random port and local host. By modifying an environmental variable "LOGGING" it is also possible to turn on a silent logging option.
>>>>>>> branch07
