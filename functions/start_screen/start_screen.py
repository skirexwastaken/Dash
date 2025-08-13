import os
import customtkinter as ctk

# --- Main Menu ---  
def start_screen(self):
    self.start_gui = ctk.CTkFrame(master=self.root)
    self.start_gui.pack(fill="both", expand=True)
    self.start_gui.place(relx=0.5, rely=0.5, anchor="center")
        
    # --- Main Menu Title ---
    start_screen_label = ctk.CTkLabel(
        master=self.start_gui,
        text="Welcome to Dash",
        font=("Arial", 90, "bold")
    )

    start_screen_label.pack(pady=(40,20),padx=40)

    # --- Button that brings user to project creation menu ---
    new_project_button = ctk.CTkButton(
        master=self.start_gui,
        text="New Project",
        font=("Arial", 40, "bold"),
        command=lambda: (forget_start_gui(self), self.create_new_project_screen(self))
    )

    new_project_button.pack(pady=20)
        
    # --- Button that brings user to project loading menu ---
    load_project_button = ctk.CTkButton(
        master=self.start_gui,
        text="Load Project",
        font=("Arial", 40, "bold"),
        command=lambda: (forget_start_gui(self), self.load_project_screen(self))
    )

    # --- If there are no projects in projects folder, the load button is disabled ---
    if not os.listdir("projects"):
        load_project_button.configure(state="disabled")

    load_project_button.pack(pady=20)
        
    # --- Button that brings user to Dash settings ---
    settings_button = ctk.CTkButton(
        master=self.start_gui,
        text="Settings",
        font=("Arial", 40, "bold"),
        command=lambda:(forget_start_gui(self),self.settings_screen(self))
    )

    settings_button.pack(pady=20)    
        
    # --- Button that turns off the app ---
    exit_button = ctk.CTkButton(
        master=self.start_gui,
        text="Exit",
        font=("Arial", 40, "bold"),
        command=lambda: (self.root.destroy())
    )
    
    exit_button.pack(pady=(20,40))
    
#  --- GUI forget helper ---
def forget_start_gui(self):
    self.start_gui.pack_forget()
    self.start_gui.place_forget()    