#port by Uhalm and Jashu0
#import libraries
import os;
import platform;
import time;


##system variables
#clear command
clear = 'Tux';
#operating system user is using
opsys = 'Tux';


##software variables
#version of the software
softVer = 'pre-Alpha 0.0.0 b ~ 2'
#credits for the re:Code
credits = """re:Code Project head:
Uhalm

re:Code Developers:
Jashu0
Uhalm

Original Code: 
Adam [REDACTED]

Testers:
Uhalm
Jashu0


In memorry of Adam [REDACTED]


"""


##user variables
#users username
username1 = 'Tux';
#users password
password1 = 'Tux';
#users input prompt !!re:Code OPTIONS ONLY!!
prompt = ''; #defult is the original '' no prompt version

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
	#print the UI
	print("""What would you like to do?

1) Create  Account
2) Login
99) Exit


100)re:Code menu


Current Version: v1.7_08""");


	#try doing this
	try:
		#get the user input
		userIn = int(input());



		#TEST BLOCK
#		print(userIn); #PRINT THE USER INPUT
#		time.sleep(5); #SLEEP5 SECODNS
		#END TEST BLOCK

		#if user selects 1
		if userIn == 1:
			#run create user function
			createUser();

		#if user selects 2
		elif userIn == 2:
			#run login function
			login();

		#if user selects 99
		elif userIn == 99:
			#clear the screen
			os.system(clear);
			#exit
			exit();


		#if user wants to accsess the re:Code spisific menu
		elif userIn == 100:
			reMenu();

		#if user input is invalod
		else:
			#rerun the function
			startMenu();



	except ValueError:
		print('ValueError');
		startMenu();

	except TypeError:
		print('TypeError');
		startMenu();



#create a new user
def createUser():
	#call the globals
	global username1;
	#clear the screen
	os.system(clear);
	#print the UI
	print('What would you like your username to be?');
	#get the users input
	username1 = input();
	#run the function to check for spaces
	checkForSpaces();


def checkForSpaces():
	print('UNFINISHED');
	time.sleep(1.526);
	startMenu();


#login to a existing account
def login():
	print('UNFINISHED')
	time.sleep(1.526);
	startMenu();


#the new re:Code only menu
def reMenu():
	#clear the screen
	os.system(clear);
	#print the UI
	print("Realm of the Fallen - re:Code")
	print("Version:", softVer);
	print("|--------------------------------------------|");
	print("|1) Login                                    |");
	print("|2) Create Account                           |");
	print("|3) Exit                                     |");
	print("|4) Settings                                 |");
	print("|5) Credits                                  |")
	print("|6) Original Menu                            |")
	print("|--------------------------------------------|");

	#get the user input
	userIn = input(prompt);
	#print the user input
	print(userIn);
	time.sleep(1.89523);
	#goto the main menu
	startMenu();







osCheck();
