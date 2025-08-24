# Dash: Simple and light weight project manager

Designed and developed by Daniel

## Developer Note: 

> As of right now, the application is mainly optimized to run in 1920x1080 resolution, support for more resolutions will be available in future releases.
> The main library behind the GUI, customtkinter, seems to be currently not fully supported on linux. 
> Due to time constrains I was not able to design separate GUI for linux but it would be the first thing I would do if I had more time.
> However you can still find pictures of how the GUI is supposed to look like in screenshots folder.

## Settup Guide

> First things first, you will need to install python together with pip, the newest versions of both.

> After installing pip you need to run the following command using a terminal in the application folder to install all needed libraries: pip install -r requirements.txt

> Now you should be able to run Dash.py using a terminal in the application folder

## Use Guide

### Upon opening Dash, you will end up in a main menu, there will be 4 buttons:

> New Project -> Here you can create a new project

> Load Project -> Here you can load your existing projects

> Settings -> Here you can find Dash settings: Appearance, Themes, Tools and Key Binds:

> Exit -> This button turns off the application

### Different Settings

> Appearance -> You can switch on/off fullscreen mode there and switch between light/dark mode

> Themes -> You can switch between blue, dark blue and green color themes

> Tools -> You can disabled certain tools that you don't need, these will no longer display in Project Manager

> Key Binds -> You can set different key binds to each tool here

### Project manager is the main menu you will get to after creating or loading a project, you will find the following tools there:

> To Do List -> This tool allows you to manage your tasks easily: You can create a task there and move it between To Do, In Progress and Done

> Calendar -> This tool allows you to add notes to specific days in a month, such as deadlines or what needs to be done on that day
 
> Mind map -> This tool allows you to to add sticky notes on a white board and connect them with red lines. This can be used to connect logical parts together

> Check List -> This tool is similar to To Do List, however added tasks can be directly marked as finished

> Sticky Notes -> This tool is similar to mindmap, but the notes can't be connected with red lines

> Text Note -> This tool is esentially a light weight text editor that allows you to write text notes, save them and load them
