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