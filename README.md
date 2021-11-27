# spam_machine
The source code for a spamming script, using pyautogui, written in Python 3.10.0rc2

Version 3.0 beta 1 (coming soon):
1. rewrite code to shorten code complexity and reduce memory consumption
   - Shorten code complexity / source code file size
   - Reduce CPU / memory consumption
   - Easier to run on weaker machines
2. remove time_between_message manual input, instead relying on CPU usage to determine time_between_message
3. added time for execution measurement (available in developer mode) (used for both version 2.3 and 3.0 beta 1)

Version 2.3 :
1. added execution time measurement (available in development mode)

Version 2.2:
1. Fixed error : name "sus" not defined, when running version 2.1 script (observed on Python 3.10.0rc2)
2. Added "emergency stops" when CPU usage is too high to continue for 10 times

Version 2.1:
1. Added functionality to end the program in a quick manner by pressing Ctrl + C to raise up KeyboardInterrupt exception instead of pressing E, which doesn't even work well anyways
2. Added functionality to execute the spamming function in the command line interface (CLI) to preview the spam messages before moving to the main wave.

Version 2:
- Added "developer mode", which can be triggered by typing "elando" into the command line interface (CLI) while executing the .py source code file.
