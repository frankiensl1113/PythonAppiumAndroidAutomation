# PythonAppiumAndroidAutomation

# Installation Guide

This guide will walk you through the installation process for Python 3, Appium Server, Android Studio, Android SDK, Java JDK, as well as starting the Appium Server and running Python in PyCharm.

## Python 3

1. Visit the official Python website: https://www.python.org/downloads/
2. Download the latest version of Python 3 for your operating system.
3. Run the installer and follow the installation instructions.
4. Make sure to add Python to your system's PATH during the installation process.

or install through Brew

Install Brew
Homebrew installs the stuff you need. Homebrew is a package manager for Mac OS

1. Launch Terminal.
2. Launchpad – Other – Terminal
3. Install HomeBrew
4. /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
5. brew install python3

## Appium Server

1. Install Node.js from https://nodejs.org/en/download/
2. Open a terminal or command prompt.
3. Run the following command to install Appium globally:

or simply call "npm install -g appium"

## Android Studio and Android SDK
Download and install Android Studio from the official website: https://developer.android.com/studio
Follow the installation wizard to complete the installation.
Start Android Studio and open the SDK Manager.
Also, install the following:
1. Android SDK Build-Tools 34
2. Andoroid Emulator
3. Google Web Driver
4. Android SDK Command-Line tools
5. Source for android 32
6. Android SDK Platform-Tools

Install the required Android SDK packages for your target devices 
For target device, Please use pixel 7and API level 32.


## Java JDK
Download the latest Java JDK from the Oracle website: https://www.oracle.com/java/technologies/javase-jdk11-downloads.html
Select the appropriate JDK version for your operating system and download the installer.
Run the installer and follow the installation instructions.


## Setup the environment path for appium, pycharm and andriod stuido/ virtual device
Add the following path to the ~/.bash_profile 

export ANDROID_HOME=~/Library/Android/sdk/
export PATH=$PATH:$ANDROID_HOME/platform-tools
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/tools/bin
export PATH=$PATH:$ANDROID_HOME/emulator
export JAVA_HOME=$(/usr/libexec/java_home)

Then, dont forget to "source ~/.bash_profile" 

## Importing and Running Python in PyCharm
Download and install PyCharm from the official website: https://www.jetbrains.com/pycharm/
Start PyCharm and Click import, select "PythonAppiumAndroidAutomation"
In the project settings, configure the Python interpreter to use the installed Python 3 version.
Import the project into the pyCharm and select python3.
To run the Python code, right-click on the file and select "Run <TodoistAutoTest.py>".

## To run the automation test
1. Turn on the virtual device, install the Todoist.apk and leave it ON.
2. In your console, get the connect virtual device by calling: 
	"adb devices" and copy the name
2. In your console, start the appium server by calling: appium
3. Open the project in pycharm and update the virtual device name in line 20 and 28
4. Make sure the appium server started listening and android virtual device is started
5. Choose the TodistAutoTest.py and click run. The virtual device will be moving as the auto script in the py file. The test result will be shown in the console.The assertion is purely done by comparing the api response and the actual app UI in this project. 
It can be integrated with other testing framework to enhace the have more testing, assertion.



