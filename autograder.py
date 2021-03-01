"""Assists in grading Canvas assignments."""

import random
import time
import webbrowser
import tkinter as tk
import pyautogui as py

ROOT = tk.Tk()

CANVAS_URL = 'YOUR CANVAS URL HERE'

ACCEPT = (1730, 180)
CHECK = (1100, 100, 400, 400)
COPY_NAME = (1670, 140)
GRADE = (1400, 300, 500, 500)
MORE = (1000, 500, 500, 400)
NO_SUB = (300, 180, 1000, 100)
OLD_COMMENT = (1700, 400, 600, 200)
SELECT = (1910, 600)
SKIP = (1630, 180)
STATUS = (1600, 100, 100, 50)
SUBMITTED = (1400, 150, 500, 300)
TODO = (1100, 100, 200, 200)
TOP_PAGE = (1800, 130)
USERNAME_BOX = (900, 300)

py.FAILSAFE = True
py.PAUSE = .1

def main():
    """Open Canvas and grades everything"""
    open_browser()
    num = num_assignments()
    py.click(TOP_PAGE)
    print("Assignments left: " + str(num))
    py.press('tab')
    py.hotkey('ctrl', 'enter')
    check_load()
    grade_assignment()
    py.hotkey('ctrl', 'w')
    time.sleep(1)
    for i in range(num):
        if (num - i) == 0:
            print("No more assignments to grade.")
            break
        else:
            print("Assignments left: " + str(num - i))
            py.press('tab')
            py.press('tab')
            py.hotkey('ctrl', 'enter')
            check_load()
            grade_assignment()
            py.hotkey('ctrl', 'w')
            time.sleep(1)

def num_assignments():
    """Finds number of assignments"""
    time.sleep(2)
    more = False
    while not more:
        if py.locateOnScreen('images/more.png', region=MORE, confidence=0.7):
            print("Found 'more' for number of assignments!")
            more = True
        else:
            print("Cannot find 'more' to get number of assignments")
            time.sleep(1)
    get_ass = py.locateCenterOnScreen('images/more.png', region=MORE, confidence=0.7)
    original_ass = get_ass
    ass_x = get_ass[0] - 25
    ass_y = get_ass[1] + 25
    py.doubleClick(ass_x, ass_y)
    py.hotkey('ctrl', 'c')
    py.click(original_ass)
    ass = ROOT.clipboard_get()
    ass = int(ass)
    ass += 4
    print("There are " + str(ass) + " assignments to grade.")
    return ass

def check_load():
    """Check if next assignment is loaded"""
    loaded = False
    while not loaded:
        if py.locateOnScreen('images/submitted.png', region=(SUBMITTED),
                             confidence=0.9):
            print('Loaded!')
            loaded = True
        else:
            time.sleep(2)
            print("Loading...")
    return True

def open_browser():
    """Open Canvas in browser and waits until loaded"""
    webbrowser.open(CANVAS_URL)
    loaded = False
    while not loaded:
        if py.locateOnScreen('images/to_do.png', region=(TODO)):
            loaded = True
            print("Loaded!")
        else:
            print("Loading Canvas...")
            time.sleep(1)

def grade_assignment():
    """Identifies grade type and gives full points"""
    while True:
        if (py.locateOnScreen('images/check.png', region=(STATUS), confidence=0.9)
                or py.locateOnScreen('images/no_submission.png', region=(NO_SUB), confidence=0.9)):
            print("Nothing to grade")
            break

        elif py.locateOnScreen('images/quiz.png', region=(GRADE)):
            print('Found quiz')
            py.doubleClick(COPY_NAME)
            py.hotkey("ctrl", "c")
            py.press("c")
            leave_comment()
            for _ in range(3):
                py.press("tab")
            py.press("enter")
            py.click(TOP_PAGE)
            py.press("n")
            time.sleep(1)
        else:
            comment_grade()
            time.sleep(.5)
            py.press("n")
            time.sleep(1)

def comment_grade():
    """Grades dropbox and leaves comment"""
    py.click(SELECT)
    py.press("g")
    py.press("up")
    py.press("down")
    py.doubleClick(COPY_NAME)
    py.hotkey("ctrl", "c")
    py.press("c")
    leave_comment()
    for _ in range(3):
        py.press("tab")
    py.press("enter")
    time.sleep(2)

def leave_comment():
    """Leaves comment in Canvas Speedgrader."""
    num = random.randint(0, 11)
    if num == 0:
        py.typewrite("Great, thanks ")
        paste_name()
        py.typewrite("!")
    elif num == 1:
        py.typewrite("Awesome, thanks for sharing ")
        paste_name()
        py.typewrite("!")
    elif num == 2:
        py.typewrite("Nice job, ")
        paste_name()
        py.typewrite("! Hope you're having fun!")
    elif num == 3:
        py.typewrite("Great job, ")
        paste_name()
        py.typewrite("!")
    elif num == 4:
        py.typewrite("This is great! Thanks ")
        paste_name()
        py.typewrite("!")
    elif num == 5:
        py.typewrite("Perfect, thanks ")
        paste_name()
        py.typewrite("!")
    elif num == 6:
        py.typewrite("Well done! Thanks ")
        paste_name()
        py.typewrite("!")
    elif num == 7:
        py.typewrite("This is awesome! Nice job ")
        paste_name()
        py.typewrite("!")
    elif num == 8:
        py.typewrite("Nicely done! Thanks ")
        paste_name()
        py.typewrite("!")
    elif num == 9:
        py.typewrite("This is great work! Nice job ")
        paste_name()
        py.typewrite(".")
    elif num == 10:
        py.typewrite("This looks really good, ")
        paste_name()
        py.typewrite("! Well done.")
    elif num == 11:
        py.typewrite("Thanks, ")
        paste_name()
        py.typewrite("! You did really well on this assignment.")

def paste_name():
    """Pastes student's first name into comment"""
    py.hotkey("ctrl", "v")
    py.press("backspace")

if __name__ == '__main__':
    main()
