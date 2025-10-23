import customtkinter as ctk

# --- Themes Menu ---
def themes_screen(self):
    self.themes_gui = ctk.CTkFrame(master=self.root)
    self.themes_gui.pack(fill="both", expand=True)
    self.themes_gui.place(relx=0.5, rely=0.5, anchor="center")

    # --- Themes Title ---
    appearance_label = ctk.CTkLabel(
        master=self.themes_gui,
        text="Themes",
        font=("Arial", 90, "bold")
    )

    appearance_label.pack(pady=(40,20),padx=40)
    
    # --- Blue theme button---
    blue_button = ctk.CTkButton(
        master=self.themes_gui,
        text="Blue",
        font=("Arial", 40, "bold"),
        command=lambda: (themes_change_helper(self,"blue"))
    )

    blue_button.pack(pady=20)
    
    # --- Dark Blue theme button ---
    dark_blue_button = ctk.CTkButton(
        master=self.themes_gui,
        text="Dark Blue",
        font=("Arial", 40, "bold"),
        command=lambda: (themes_change_helper(self,"dark-blue"))
    )

    dark_blue_button.pack(pady=20)
    
    # --- Green theme button ---
    green_button = ctk.CTkButton(
        master=self.themes_gui,
        text="Green",
        font=("Arial", 40, "bold"),
        command=lambda: (themes_change_helper(self,"green"))
    )

    green_button.pack(pady=20)
    
    # --- Button that brings user back to Settings Menu ---
    back_button = ctk.CTkButton(
        master=self.themes_gui,
        text="Back",
        font=("Arial", 40, "bold"),
        command=lambda: (self.themes_gui.pack_forget(), self.themes_gui.place_forget(), self.settings_screen(self))
    )
    
    back_button.pack(pady=(20,40))
    
# --- Helper function that helps making the code more clean + executes the theme change ---
def themes_change_helper(self,colour):
    ctk.set_default_color_theme(colour)

    self.settings_change("theme",colour)

    self.themes_gui.pack_forget()
    self.themes_gui.place_forget()

    self.themes_screen(self)