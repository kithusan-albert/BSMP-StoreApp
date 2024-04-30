# COMP639S1_Group_AEv

### References
All images used for this application have been downloaded from https://pixabay.com/ and are free for use under the Pixabay Content License: https://pixabay.com/service/license-summary/

## Steps to pull the latest updates from GitHub to PythonAnywhere and check if all works as expected
1. Go to Consoles tab on PythonAnywhere.
2. If there is a Bash console open, you can use it. If there isn't any, please start a new Bash console.
3. In the Bash console type cd COMP639S1_Group_AE to change the directory to what we need.
4. Type git pull and provide your personal GitHub username or email address and our shared token (group_project_shared_token.odt file from our SharePoint folder. This is an MS Word file type).
5. Check whether there is a MySQL console open. If positive - open it, if negative - go to the Databases tab and click on anglers$fishing database. The MySQL console will open.
6. Type source /home/anglers/COMP639S1_Group_AE/create_fishing_schema_pa.sql to run the database file and
   source /home/anglers/COMP639S1_Group_AE/insert_fishing_data.sql to populate the tables with data.
8. Go to Web tab, press the green Reload button and open the application.


## Steps to download and setup local environment in VS Code
1. Clone the repository to a local folder using github desktop
2. In VS Code, open the repository, then open the Command Palette (View > Command Palette or (Ctrl+Shift+P)). Then select the Python: Create Environment command to create a virtual environment in your workspace. Select venv and then the Python environment you want to use to create it.
3. In the terminal within CS code run the following commands:
..1. python -m pip install flask
..2. venv\Scripts\Activate.ps1
..3. pip install -r requirements.txt
4. In the root folder create a connect.py file with your local database connection details. This should be in the same folder as the run.py file.
5. Now you can run the following line(s) to launch the webapp:
 
   flask --app run.py run

   flask --app run.py run --debug  (this line will auto run flask everytime you hit save, saves some time)




## References
### Images:
https://www.freepik.com/free-vector/nature-underwater-blue-clear-water-background_39207975.htm#query=sea%20water%20cartoon&position=0&from_view=keyword&track=ais&uuid=71853842-e81f-49e7-bef7-ce4a6d259690

https://iconduck.com/emojis/96945/fishing-pole-and-fish

### PythonAnywhere account created for this group project:
username: anglers

password: Ang_L1Rs_@_PAre

separate mailbox set up for PythonAnywhere account:

John McBrown <johnmcbrown@mailfence.com>

J0Hn_@_14032024Br0wn

## Pre-populated users
There are several pre-populated users, fishing guides and managers pre-defined to showcase the functionality of the website for users of varying permission levels.
 Username | Password | Role |
| --- | --- | --- |
| arnold | P@55w0rd | Manager |
| kira | P@55w0rd | Manager |
| veronika | P@55w0rd | Manager |
| andrew | P@55w0rd | Manager |
| jackdaniel | P@55w0rd | Fishing Guide |
| cantor | P@55w0rd | Fishing Guide |
| mark | P@55w0rd | Fishing Guide |
| serg | P@55w0rd | Fishing Guide |
| robert | P@55w0rd | Fishing Guide |
| iriya | P@55w0rd | Fishing Guide |
| maria | P@55w0rd | Fishing Guide |
| jackfrost | P@55w0rd | Fishing Guide |
| bob | P@55w0rd | Member |
| aria | P@55w0rd | Member |
| johnconnor | P@55w0rd | Member |
| patrick | P@55w0rd | Member |
| elsa | P@55w0rd | Member |
| max | P@55w0rd | Member |
| april | P@55w0rd | Member |
| luna | P@55w0rd | Member |
| petracolins | P@55w0rd | Member |
| abigail | P@55w0rd | Member |
| aleenacoo | P@55w0rd | Member |
| helga | P@55w0rd | Member |
| miriam | P@55w0rd | Member |
| ruthreiner | P@55w0rd | Member |
| moonpie | P@55w0rd | Member |
| franndr | P@55w0rd | Member |
| keithshi | P@55w0rd | Member |
| oruaans | P@55w0rd | Member |
| mattrilke | P@55w0rd | Member |
| werter | P@55w0rd | Member |
| thomasmann | P@55w0rd | Member |

