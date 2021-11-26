# spam_machine
the code for a spamming script, written in Python 3.10.0rc2


Version 2.2:
	1.Fixed error : name "sus" not defined, when running version 2.1 script (observed on Python 3.10.0rc2)
	2.Added "emergency stops" when CPU usage is too high to continue for 10 times

Version 2.1:
	1.Added functionality to end the program in a quick manner by pressing Ctrl + C to raise up KeyboardInterrupt exception instead of pressing E, which doesn't even work well anyways
	2.Added functionality to execute the spamming function in the command line interface (CLI) to preview the spam messages before moving to the main wave.

Version 2:
	Added "developer mode", which can be triggered by typing "elando" into the command line interface (CLI) while executing the .py source code file.
