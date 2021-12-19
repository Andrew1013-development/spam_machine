# spammer_lol.py / spammer_lol_beta.py
- The source code for a spamming script, using pyautogui, written in Python 3.10.0rc2
- Current versions statistics :
  - Stable version : Version 2.5
  - Released version : Version 3.0 beta 7
  - Near Deprecation version : Version 2.0
  - Deprecated version : Version 1.0

## some notices :
- The author (Andrew1013) is busy with his endterm tests and school things so the release of Version 3.0 beta 7.1 will be delayed.
- I'll still try to work on Version 3.0 beta 7.1 and beta 8 while doing my tests if i have time, but expect some delay.
- I expect to wrap up the testing phase of Version 3 betas in January of 2022 (currently working on beta 7.1), but it is subjected to change.
- The Version 2.x lineage will end with Version 2.7, moving to the more stable Version 3.0 releases when the Version 3.0 beta phase end.
- If you have any issues, post it on the Issues tab in the GitHub page or contact me at Discord via DMs (read "contact me" section for more details)
- If you want to participate in this project, contact me at Discord via DMs or via my emails (read "contact me" section for more details)

## contact me
- Discord : Andrew 1013#3953 / Andrew 1214#3480
- Gmail : viethuytran147@gmail.com / viethuytran123@gmail.com
- GitHub : Issues tab on the repository page
- Facebook : Mark Hay / Huy Thứ Hai
- YouTube (though not coding channels yet) : RYL Andrew / RYL Andrew 2

## changelog (in order from newest to oldest)
Version 3.0 beta 7.1 (coming soon) :
1. Bug fixes for some functions of Version 3.0 beta 7

Version 3.0 beta 7 (newest version)
1. Added functionality for labeling string during spam operation
2. Added functionality for changing the order of spamming (fixed or randomized)

Version 3.0 beta 6 :
1. Bug fixes for self-install functions (introduced in version 3.0 beta 5 and version 2.4)
2. Statistics report as txt file? (work in progress)
3. Revamp to the cpu check to get timeout mechanic
 
Version 2.5 (newest stable version):
1. Bug fixes for self-installing modules function 
   - this function was introduced first in Version 3.0 beta 5 and Version 2.4)

Version 2.4 :
1. added the ability to self-install the modules if it's missing (from Version 3.0 beta 4)

Version 3.0 beta 5 (the newest version) :
1. Added functionality to generate 2 strings of random letters
   - Either on-demand or fixed (generate once before the spamming)
2. Added functionality for second string spamming
3. A slight change to timing (timing code integrated into the functions instead of the driver code)

Version 3.0 beta 4 (the newest version) :
1. added the ability to self-install the modules if it's missing

Version 3.0 beta 3 :
1. added more functionality for spamming 2 different messages, still in order (from string1 to string2) only
2. added Command Line Interface (CLI) test for 2 strings functionality

Version 3.0 beta 2 :
1. added basic functionality for spamming 2 different messages in order (from string1 to string2) only
   - full functionailty will come in version 3.0 beta 4 or beta 5 (read "some notices" for more details)

Version 3.0 beta 1 (the first beta of Version 3.x):
1. rewrite code to
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

Version 1.0.x to 1.2 :
- Changelog lost (version 1.0 in GitHub was version 3 of the project in motion offline)

Version 1.0 :
- Initial release
