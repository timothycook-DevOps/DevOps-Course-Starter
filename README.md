# DevOps Apprenticeship: Project Exercise

## Getting started

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from a bash shell terminal:

### On macOS and Linux

```bash
$ source setup.sh
```

### On Windows (Using PowerShell)

```powershell
$ .\setup.ps1
```

### On Windows (Using Git Bash)

```bash
$ source setup.sh --windows
```

Once the setup script has completed and all packages have been installed, start the Flask app by running:

```bash
$ flask run
```

### Initial Setup for Checklist Appplication

Add the following to the .env file.

Add your Trello api details.

1. TRELLOAPIKEY = 'yourAPIkey'
2. TRELLOSERVERTOKEN = 'yourAPIkey'

Add the following values to the ApiAccess.py folder.

  TODOLISTURL = 'https://api.trello.com/1/lists/YOURTODOLISTID/cards/'
  DOINGLISTURL = 'https://api.trello.com/1/lists/YOURDOINGLISTID/cards/'
  DONELISTURL = 'https://api.trello.com/1/lists/YOURDONELISTID/cards/'

  CARDSURL = 'https://api.trello.com/1/cards/'
  LISTURL = 'https://api.trello.com/1/lists/'
  TODOLISTID = 'YOURTODOLISTID'
  DOINGLISTID = 'YOURDOINGLISTID'
  DONELISTID = 'YOURDONELISTID'

Replacing the capitalised URL values with your own trello values.

###

You should see output similar to the following:

```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```

Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

### Notes

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like developement mode (which also enables features like hot reloading when you make a file change).

- There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

When running `setup.sh`, the `.env.template` file will be copied to `.env` if the latter does not exist.
