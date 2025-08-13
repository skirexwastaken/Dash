import customtkinter as ctk
 
# --- Settings Menu ---
def settings_screen(self):
    self.settings_gui = ctk.CTkFrame(master=self.root)
    self.settings_gui.pack(fill="both", expand=True)
    self.settings_gui.place(relx=0.5, rely=0.5, anchor="center")
        
    # --- Settings  Title ---
    settings_label = ctk.CTkLabel(
        master=self.settings_gui,
        text="Settings",
        font=("Arial", 90, "bold")
    )

    settings_label.pack(pady=(40,20),padx=40)
    
    # --- Button that brings user to Appearance Menu ---
    appearance_button = ctk.CTkButton(
        master=self.settings_gui,
        text="Appearance",
        font=("Arial", 40, "bold"),
        command=lambda: (forget_settings_gui(self), self.appearance_screen(self))
    )

    appearance_button.pack(pady=20)
    
    # --- Button that brings user to Themes Menu ---
    themes_button = ctk.CTkButton(
        master=self.settings_gui,
        text="Themes",
        font=("Arial", 40, "bold"),
        command=lambda: (forget_settings_gui(self), self.themes_screen(self))
    )

    themes_button.pack(pady=20)
    
    # --- Button that brings user to Toggle Tools Menu ---
    toggle_tools_button = ctk.CTkButton(
        master=self.settings_gui,
        text="Tools",
        font=("Arial", 40, "bold"),
        command=lambda: (forget_settings_gui(self), self.toggle_tools_screen(self))
    )

    toggle_tools_button.pack(pady=20)
    
    # --- Button that brings user to Key Binds Menu ---
    key_binds_button = ctk.CTkButton(
        master=self.settings_gui,
        text="Key Binds",
        font=("Arial", 40, "bold"),
        command=lambda: (forget_settings_gui(self), self.key_binds_screen(self))
    )

    key_binds_button.pack(pady=20)
        
    # --- Button that brings user back to Main Menu ---
    back_button = ctk.CTkButton(
        master=self.settings_gui,
        text="Back",
        font=("Arial", 40, "bold"),
        command=lambda: (forget_settings_gui(self), self.start_screen(self))
    )
    
    back_button.pack(pady=(20,40))
    
#  --- GUI forget helper ---    
def forget_settings_gui(self):
    self.settings_gui.pack_forget()
    self.settings_gui.place_forget()    