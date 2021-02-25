# Canvas Auto-Grader
This program uses PyAutoGui to automatically grade the "To Do" queue in Canvas.

## Assumptions
This program is designed to run under several conditions.
* Windows 10
* 1920 x 1080 monitor resolution
* Firefox browser
* Bookmarks toolbar showing (this matters because of the clicking coordinates the program uses)
* Canvas assignments are all Complete/Incomplete grading types OR quizzes. This program will not grade quizzes, but it will leave a comment on the quiz which allows you to easily enter scores later.

The code can be adjusted to work for different settings, but this is how it's currently set up.

## Installing Python
Python needs to be installed on your computer for this to work. Download and install the latest version [here](https://www.python.org/downloads/). When installing, make sure you check the "Add Python 3.X to PATH" on the setup wizard.

Once Python has been installed, open Command Prompt and run the following command:

`pip install --user pyautogui`


## Instructions
1. Open `autograder.py` and put the URL of your Canvas account into the `CANVAS_URL` variable on line 11.

  Line 11 should look like this when you're finished with this step:

  ```CANVAS_URL = "https://my-institution.instructure.com"```

2.  Open Canvas in a Firefox window and log in. You'll keep this tab open since it avoids any login issues with the program.

3. Run `autograder.py`. It will open your Canvas URL in a new window and begin the grading process

## Additional Details
* **IMPORTANT**: If you need to terminate the program early this is done by dragging your mouse to the top left corner of the screen. This may take several seconds to work, so make sure to keep dragging the mouse to the top left corner.

* The functionality of this program may vary depending on individual computer settings.

##
