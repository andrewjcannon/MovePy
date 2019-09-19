# web-sorter

Program that can be used to periodically sort files in a directory into multiple sub-folders based on file type. Web-sorter runs a Flask web server to serve the user interface and settings of the app. All settings are also customizable via a .ini file.

# app.py
app.py can be run to start the web server and run main.py (the sorting script).
The server can be connected to on port 7259 (default).

# main.py
The primary file-sorter script. All settings are loaded from the .ini file, which is also editable via the web interface provided by app.py. The script can, depending on settings, run once or loop continuously at customizable time intervals.
