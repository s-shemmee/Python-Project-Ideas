# Desktop Notifier App in Python

A desktop notifier is a simple Python application that displays a desktop pop-up message as a notification. The user receives a notification whenever a particular app is launched.

## How we can use it?

- Daily reminder to take your medication.
- Ask a question
- Hourly reminder to drink water.
- Notify about updates
- Birthday reminder
- Gym reminder
- Promote a limited-time deal
- Collect feedback
- Daily tracker for COVID stats in your country

and many more, it’s completely up to you how to use this application.

## What we need ?

### Plyer

*Plyer is an open source library to access features commonly found in various platforms via python.*

## Installing required python packages

*we need to download two important packages for this application.*

*Open your terminal and run the following command.*

- **1.requests** :

in case you want to fetch data from the web

```terminal
 pip install requests
```

- **2. plyer** :

For creating notifications on your PC

```terminal
pip install plyer
```

*Now that we have the packages, we are ready to import it in our python script.*

```py
from plyer import notification
```

## Coding Timuu

- Now let's specify the parameters.

```py
from plyer import notification

title = 'Hi, Hello and Hi !'

message= 'If u reading this ~I LOVE U TO THE MOON AND BACK !!'

notification.notify(title= title,
                    message= message,
                    app_icon = "heart.ico",
                    timeout= 15,
                    toast= False)

time.sleep(60*60)
```

- Let's look at what the parameters mean:

```markdown
Syntax: notify(title=”, message=”, app_name=”, app_icon=”, timeout=10, ticker=”, toast=False)
```

Parameters:

- `title (str`) : Title of the notification
- `message (str)` : Message of the notification
- `app_name (str)` : Name of the app launching this notification
- `app_icon (str)` : Icon to be displayed along with the message
- `timeout (int)` : time to display the message for, defaults to 10
- `time.sleep` : After displaying a notification, we will make it sleep for 1 hour or 60 minutes. You can choose a different interval.
- `ticker (str)` : text to display on status bar as the notification arrives
- `toast (bool)` : simple Android message instead of full notification

## Here is how you see your notification after running your application

![notification after running](Capture.PNG)

## How to make a python application to run in the background?

*Just follow this simple command to make your application run in the background, note you need to type this command in command prompt in case you are using Windows and terminal in case you are using Linux.*

> Note: replace the `<your-file-name-here>` with your file name

```terminal
pythonw.exe .\<your-file-name-here>
example 
pythonw.exe .\Desktop_Notifier_App.py
```

*That's it your application now starts running in the background.*

## How do you confirm that your application is running in the background?

*open task manager in your pc and you can see that in background process you can see python is running.*

![script running in the backgroung](Capture2.PNG)

## How to stop getting notifications?

*That’s simple, in the task manager kill the process named python. If you feel any difficulty in stoping the notification please feel free to post your difficulty in the Discussion section of this Documentation.*
