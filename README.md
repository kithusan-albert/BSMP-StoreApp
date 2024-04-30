## Steps to download and setup local environment in VS Code
1. Clone the repository to a local folder using github desktop
2. In VS Code, open the repository, then open the Command Palette (View > Command Palette or (Ctrl+Shift+P)). Then select the Python: Create Environment command to create a virtual environment in your workspace. Select venv and then the Python environment you want to use to create it.
3. In the terminal within CS code run the following commands:
..1. python -m pip install flask
..2. venv\Scripts\Activate.ps1
..3. pip install -r requirements.txt
4. In the root folder create a connect.py file with your local database connection details. This should be in the same folder as the run.py file.
5. Now you can run the following line(s) to launch the webapp:

   Press the play button on Run.py

OR
 
   flask --app run.py run
   flask --app run.py run --debug  (this line will auto run flask everytime you hit save, saves some time)


