import customtkinter as ctk

# --- Appearance Menu ---
def appearance_screen(self):
    self.appearance_gui = ctk.CTkFrame(master=self.root)
    self.appearance_gui.pack(fill="both", expand=True)
    self.appearance_gui.place(relx=0.5, rely=0.5, anchor="center")

    # --- Appearance Title ---   
    appearance_label = ctk.CTkLabel(
        master=self.appearance_gui,
        text="Appearance",
        font=("Arial", 90, "bold")
    )

    appearance_label.pack(pady=(40,20),padx=40)
    
    # --- Full Screen button ---
    full_screen_button = ctk.CTkButton(
        master=self.appearance_gui,
        text="Fullscreen",
        font=("Arial", 40, "bold"),
        command=lambda: (self.root.attributes("-fullscreen", not self.root.attributes("-fullscreen")),self.settings_change("fullscreen", self.root.attributes("-fullscreen")))
    )

    full_screen_button.pack(pady=20)
    
    # --- Light Mode button ---
    light_button = ctk.CTkButton(
        master=self.appearance_gui,
        text="Light",
        font=("Arial", 40, "bold"),
        command=lambda: (ctk.set_appearance_mode("light"), self.settings_change("appearance","light"))
    )

    light_button.pack(pady=20)
    
    # --- Dark Mode button ---
    dark_button = ctk.CTkButton(
        master=self.appearance_gui,
        text="Dark",
        font=("Arial", 40, "bold"),
        command=lambda: (ctk.set_appearance_mode("dark"), self.settings_change("appearance","dark"))
    )

    dark_button.pack(pady=20)
    
        
    # --- Button that brings user back to settings menu ---
    back_button = ctk.CTkButton(
        master=self.appearance_gui,
        text="Back",
        font=("Arial", 40, "bold"),
        command=lambda: (self.appearance_gui.pack_forget(), self.appearance_gui.place_forget(), self.settings_screen(self))
    )
    
    back_button.pack(pady=(20,40))