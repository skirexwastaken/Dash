# Dash: Simple and light weight project manager
Dash is a simple and light weight project manager written in Python.

It uses the customTkinter library for all of its GUI.

## Settup Guide
First things first, you will need to install python together with pip, the newest versions of both.

After installing pip you need to run the following command using a terminal in the application folder to install all needed libraries: pip install -r requirements.txt

Now you should be able to run Dash.py using a terminal in the application folder

## Use Guide

### Main Menu
Upon opening Dash, you will end up in a main menu, there will be 4 buttons:

1. New Project -> Here you can create a new project

2. Load Project -> Here you can load your existing projects

3. Settings -> Here you can find Dash settings: Appearance, Themes, Tools and Key Binds:

4. Exit -> This button turns off the application

### Different Settings
Dash offers different settings that allow you to customize the app to your liking:

1. Appearance -> You can switch on/off fullscreen mode there and switch between light/dark mode

2. Themes -> You can switch between blue, dark blue and green color themes

3. Tools -> You can disabled certain tools that you don't need, these will no longer display in Project Manager

4. Key Binds -> You can set different key binds to each tool here

### Workspace
After creating or loading a project, you will end up in the Workspace menu, you will find the following tools there:

1. To Do List -> This tool allows you to manage your tasks easily: You can create a task there and move it between To Do, In Progress and Done

2. Calendar -> This tool allows you to add notes to specific days in a month, such as deadlines or what needs to be done on that day

3. Mind map -> This tool allows you to to add sticky notes on a white board and connect them with red lines. This can be used to connect logical parts together

4. Check List -> This tool is similar to To Do List, however added tasks can be directly marked as finished

5. Sticky Notes -> This tool is similar to mindmap, but the notes can't be connected with red lines

6. Text Note -> This tool is esentially a light weight text editor that allows you to write text notes, save them and load them

## Developer Note: 
As of right now, the application is mainly optimized to run in 1920x1080 resolution, support for more resolutions will be available in future releases.

The main library behind the GUI, customtkinter, seems to currently be not fully supported on linux. Possible linux/windows theme might be added in the future.
