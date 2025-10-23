import customtkinter as ctk
import os
import json

# --- Text Note Tool ---
def text_note_tool(self):
    self.main_frame.grid_forget()
    self.main_frame = ctk.CTkFrame(
        master=self.root,
        corner_radius=0,
        border_width=5,
        border_color="#1f6aa5"
        )
    
    # --- Loads project data ---
    with open(f"projects/{self.current_project}/project_data.json","r") as file:
            self.project_data = json.load(file)
    
    # --- Sets Main Frame parameters ---        
    self.main_frame.grid(row=1, column=1, sticky="nsew")
    self.main_frame.grid_columnconfigure(0, weight=1)
    self.main_frame.grid_rowconfigure(1, weight=1)
    
    # --- Text Note tool panel ---
    text_note_tools_panel = ctk.CTkFrame(master=self.main_frame)
    text_note_tools_panel.grid(column=0, row=0, sticky = "we", padx=20, pady=20)
    
    # --- Save Text Note button ---
    save_button = ctk.CTkButton(
        master=text_note_tools_panel,
        text="Save",
        font=("Arial", 20,"bold"),
        command=lambda: (save_load_helper_function(self), save_text_note_screen(self))
    )

    save_button.grid(column=0, row=0, pady=15, padx=10)
    
    # --- Load Text Note button ---
    load_button = ctk.CTkButton(
        master=text_note_tools_panel,
        text="Load",
        font=("Arial", 20,"bold"),
        command=lambda: (save_load_helper_function(self), load_text_note_screen(self))
    )

    load_button.grid(column=1, row=0, pady=15, padx=10)
    
    # --- Main Text Box ---
    self.text_note_area = ctk.CTkTextbox(
        master=self.main_frame,
        font=("Arial", 20,"bold")
    )

    self.text_note_area.grid(columnspan=3, row=1, sticky="nswe", padx=20, pady=20)
    
    # --- Clean Text Note button ---
    clean_button = ctk.CTkButton(
        master=text_note_tools_panel,
        text="Clean",
        font=("Arial", 20,"bold"),
        command=lambda: (self.text_note_area.delete("1.0", "end"),update_current_tool(self,"current_text_note_tool",""))
    )

    clean_button.grid(column=2, row=0, pady=15, padx=10)
    
    # --- If current text note is not none -> the last text note is loaded ---
    if self.project_data["current_text_note_tool"] != "":
        with open(f"projects/{self.current_project}/text_notes/{self.project_data["current_text_note_tool"]}","r") as file:
            note_text = file.readlines()
        self.text_note_area.delete("1.0", "end") #Cleans the field
        self.text_note_area.insert("1.0", "".join(note_text)) #Inserts the text note into the field
    
# --- Save Text Note Menu ---
def save_text_note_screen(self):
    self.save_text_note_name = ctk.StringVar()
    self.save_text_note_gui = ctk.CTkFrame(master=self.root)
    self.save_text_note_gui.pack(fill="both", expand=True)
    self.save_text_note_gui.place(relx=0.5, rely=0.5, anchor="center")
    
    self.existing_text_notes = []
    for text_note_name in os.listdir(f"projects/{self.current_project}/text_notes"): 
             if text_note_name.endswith('.txt'):
                self.existing_text_notes.append(text_note_name)       
        
    # --- Save Text Note Title ---
    save_text_note_label = ctk.CTkLabel(
        master=self.save_text_note_gui,
        text="Saving a text note",
        font=("Arial", 90, "bold")
    )

    save_text_note_label.grid(columnspan=2,row=0,pady=(40,20),padx=40)
        
    # --- Field for Text Note name ---
    save_text_note_label_name_field = ctk.CTkEntry(
        master=self.save_text_note_gui,
        width=700,
        placeholder_text="New project name...",
        font=("Arial", 40, "bold"),
        textvariable=self.save_text_note_name
    )
        
    save_text_note_label_name_field.grid(columnspan=2,row=1,pady=20)
        
    self.save_text_note_name.trace_add("write", lambda *args: on_save_text_note_label_name_field_change(self)) #Monitoring for changes in the project_name_field entry
        
    # --- Button that seves the Text Note ---
    self.save_text_note_button = ctk.CTkButton(
        master=self.save_text_note_gui,
        text="Save",
        state = "disabled",
        font=("Arial", 40, "bold"),
        command=lambda: (save_text_note(self),self.save_text_note_gui.pack_forget(), self.save_text_note_gui.place_forget(), self.project_manager_screen(self))
    )
    self.save_text_note_button.grid(column=0,row=2,sticky="ne",pady=20,padx=10)
        
    # --- Button that brings user back Project Manager ---
    back_button = ctk.CTkButton(
        master=self.save_text_note_gui,
        text="Back",
        font=("Arial", 40, "bold"),
        command=lambda: (self.save_text_note_gui.pack_forget(), self.save_text_note_gui.place_forget(), self.project_manager_screen(self))
    )

    back_button.grid(column=1,row=2,sticky="nw",pady=(20,40),padx=10)

# --- Upon entering text into save_text_note_label_name_field, the Save button is enabled ---
def on_save_text_note_label_name_field_change(self, *args):
    text = self.save_text_note_name.get().strip()
    
    if len(text) > 25 or any(character in text for character in ['/', '\\', ':', '*', '?', '"', '<', '>', '|']):#Text Note name length is limited to 25 characters including spaces
        if self.save_text_note_button.cget("state")=="normal":
            self.save_text_note_button.configure(state="disabled")

    elif f"{text}.txt" in self.existing_text_notes and self.save_text_note_button.cget("state")=="normal":
        self.save_text_note_button.configure(state="disabled")
            
    elif text and self.save_text_note_button.cget("state")=="disabled":
        self.save_text_note_button.configure(state="normal")
        
    elif not text and self.save_text_note_button.cget("state")=="normal":
        self.save_text_note_button.configure(state="disabled")

# --- Function that saves the content of a text note into a .txt file ---        
def save_text_note(self):
    with open(f"projects/{self.current_project}/text_notes/{self.save_text_note_name.get()}.txt","w") as file:
        file.writelines(self.text_note_area.get("1.0", "end-1c"))
    update_current_tool(self,"current_text_note_tool",f"{self.save_text_note_name.get().strip()}.txt")    

# --- Function that updates the current tool on project data ---       
def update_current_tool(self,tool,arg):
        self.project_data[tool]=arg
        with open(f"projects/{self.current_project}/project_data.json","w") as file:
            json.dump(self.project_data,file,indent=4)
                 
# --- Loading Text Note Menu ---
def load_text_note_screen(self):
    
    # --- Loading all Text Note names in current project folder ---
    text_note_names=[]
    for text_note_name in os.listdir(f"projects/{self.current_project}/text_notes"): 
            if text_note_name.endswith('.txt'):
                text_note_names.append(text_note_name)
                 
    # --- Load Text Note Panel ---    
    self.load_text_note_gui = ctk.CTkFrame(master=self.root)      

    # --- Loading Text Note Title ---
    load_text_note_label = ctk.CTkLabel(
        master=self.load_text_note_gui,
        text="Loading a text note",
        font=("Arial", 90, "bold")
    )

    load_text_note_label.grid(columnspan=2,row=0,pady=(40,20),padx=40)
    
    # --- Currently selected Text Note ---
    self.current_text_note_label = ctk.CTkLabel(
        master=self.load_text_note_gui,
        text="None",
        font=("Arial", 40, "bold")
    )

    self.current_text_note_label.grid(columnspan=2,row=1,pady=20)
        
    # --- Creating scroll frame for Text Note names ---
    self.text_note_scroll_frame = ctk.CTkScrollableFrame(
        master=self.load_text_note_gui,
        height=50
    )

    self.text_note_scroll_frame.grid(columnspan=2,row=2,sticky="we",pady=20,padx=80)
     
    # --- Adding all text notes to the scrollable frame ---            
    for text_note in text_note_names:
        text_note_button = ctk.CTkButton(
            master=self.text_note_scroll_frame,
            text=text_note,
            font=("Arial", 15, "bold"),
            command=lambda name=text_note: (on_text_note_name_selected(self,name), ),
            corner_radius=5
        )

        text_note_button.pack(fill="x", pady=5,padx=10)
        
    # --- Button that loads a Text Note ---
    self.load_text_note_button = ctk.CTkButton(
        master=self.load_text_note_gui,
        text="Load",
        state = "disabled",
        font=("Arial", 40, "bold"),
        command=lambda: (self.load_text_note_gui.pack_forget(), self.load_text_note_gui.place_forget(),update_current_tool(self,"current_text_note_tool",self.current_text_note), self.project_manager_screen(self))
    )
    
    self.load_text_note_button.grid(sticky="en",column=0,row=3,pady=20,padx=10)
         
    # --- Button that brings user back to Project Manager ---
    back_button = ctk.CTkButton(
        master=self.load_text_note_gui,
        text="Back",
        font=("Arial", 40, "bold"),
        command=lambda: (self.load_text_note_gui.pack_forget(), self.load_text_note_gui.place_forget(), self.project_manager_screen(self))
    )
    back_button.grid(sticky="wn",column=1,row=3,pady=(20,40),padx=10)
    self.load_text_note_gui.pack(fill="both", expand=True)
    self.load_text_note_gui.place(relx=0.5, rely=0.5, anchor="center")
    
# --- Upon clicking on one of the Text Note names in the scroll frame, it is set to current Text Note selected ---
def on_text_note_name_selected(self, name):
    self.current_text_note_label.configure(text=name)
    self.current_text_note=name
    if self.load_text_note_button.cget("state")=="disabled":
        self.load_text_note_button.configure(state="normal")                

# --- Helper functions that shortens the code in save/load button command part ---
def save_load_helper_function(self):
    self.tool_panel.grid_forget()
    self.top_panel.grid_forget(),
    self.main_frame.grid_forget(),
    self.root.grid_rowconfigure(0)
    self.root.grid_columnconfigure(0)                                