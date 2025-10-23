# --- Importing needed libraries ---
import customtkinter as ctk
import json

# --- Importing all functions that make up the application ---
from functions.import_files import import_files

# --- Dash Class ---
class Dash:
    def __init__(self):
        with open("app_data.json","r") as app_data:
            app_data=json.load(app_data)
            
        # --- Configuring ctk + Defining and configuring root ---
        ctk.set_appearance_mode(app_data["appearance"])
        ctk.set_default_color_theme(app_data["theme"])
        self.root = ctk.CTk()
        self.root.attributes("-fullscreen",app_data["fullscreen"])
        self.root.title("Dash")
        self.root.geometry("1920x1080")
        self.root.resizable(True,True)
        
        # --- Importing files from definitions ---
        
        import_files(self)
            
        # --- Main Menu screen is displayed upon app start ---
        self.start_screen(self)
        
        # --- Starts the main loop of the app ---    
        self.root.mainloop()
            
#--- Starts the app ---       
app = Dash()   