#port by Uhalm and Jashu0
#import libraries
import os;
import platform;
import time;


#system variables
clear = 'Tux';
opsys = 'Tux';


#software variables
softVer = 'pre-Alpha 0.0.0 b ~ 0'

#game variables


#function that checks if user is running Windows or Unix
def osCheck():
	#call the global variables
	global clear;
	global opsys;

	#get the operating system
	opsys = platform.system();

	#check if the OS is Windows or Linux
	#if Linux
	if opsys.lower() == 'linux' or opsys.lower() == 'linux1' or opsys.lower() == 'linux2':
		#set clear to the linux clear command 'clear'
		clear = 'clear';
		#clear the screen
		os.system('clear');
		#print a alert on the stability on Linux
		print('ALERT!');
		print('Some functions will only work on Windows devices.');
		print('Software may be unstable on Linux devices.')

		#sleep for 8 seconds
		time.sleep(8);
		#clear the screen
		os.system('clear');
		#run the startup function
		startup();

	#if Windows
	elif opsys.lower() == 'win' or opsys.lower() == 'win32' or opsys.lower() == 'windows':
		#set clear to Windows clear command 'cls'
		clear = 'cls'
		#set the window title to Project 741 - re:Coded
		os.system('title Project 741 - re:Coded');
		#sets the background black '0'  and the text green 'a'
		os.system('color 0a');
		#set the size of the window 160 coloumes and 62 lines
		os.system('mode con cols=160 lines=62');

		#clear the screen
		os.system('cls');
		#run the startup function
		startup();


	#print what to do if not windows or linux
	else:
		#print the error
		print('Please use a Linux or Windows Operating System.');
		print("This software will not work on other OS's");
		#sleep for 1 minute
		print('Software will exit in 1 minute');
		time.sleep(60);



#the startup function
def startup():
	#clear screen
	os.system(clear);
	#print the Game name and version (splash screen)
	print('Project 741');
	print('Realm of the Fallen v1.7_08  -  re:Coded');
	print('Version:', softVer);

	#sleep for 10 seconds
	time.sleep(10);
	#run the startMenu function
	startMenu();



#menu to be displayed to login create acount etc
def startMenu():
	#clear the screen
	os.system(clear);

	#test line
	print(clear, opsys, softVer);
	startMenu();


osCheck();
