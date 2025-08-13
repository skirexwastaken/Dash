import customtkinter as ctk
import os
import json

# --- Creating Project Menu ---
def create_new_project_screen(self):
    self.new_project_name = ctk.StringVar() #Variable used to track the string value in new_project_name_field

    self.create_project_gui = ctk.CTkFrame(master=self.root)
    self.create_project_gui.pack(fill="both", expand=True)
    self.create_project_gui.place(relx=0.5, rely=0.5, anchor="center")
    
    self.existing_projects = []#List of all existing projects
    
    for project_name in os.listdir("projects"):
        self.existing_projects.append(project_name)
        
    # --- Creating Project Menu  Title ---
    start_label = ctk.CTkLabel(
        master=self.create_project_gui,
        text="Creating a new project",
        font=("Arial", 90, "bold")
    )

    start_label.grid(row=0,columnspan=2,pady=(40,20),padx=40)
        
    # --- Field for a new project name ---
    new_project_name_field = ctk.CTkEntry(
        master=self.create_project_gui,
        width=700,
        placeholder_text="New project name...",
        font=("Arial", 40, "bold"),
        textvariable=self.new_project_name
    )
        
    new_project_name_field.grid(row=1,columnspan=2,pady=20)
        
    self.new_project_name.trace_add("write", lambda *args: on_new_project_name_field_change(self)) #Monitoring changes in the project_name_field entry
        
    # --- Button that creates a new project ---
    self.create_project_button = ctk.CTkButton(
        master=self.create_project_gui,
        text="Create",
        state = "disabled",
        font=("Arial", 40, "bold"),
        command=lambda: (create_new_project(self), forget_create_project_gui(self), self.project_manager_screen(self))
    )

    self.create_project_button.grid(row=2,column=0,sticky="en",pady=20,padx=10)
        
    # --- Button that brings user back to main menu ---
    back_button = ctk.CTkButton(
        master=self.create_project_gui,
        text="Back",
        font=("Arial", 40, "bold"),
        command=lambda: (forget_create_project_gui(self), self.start_screen(self))
    )

    back_button.grid(row=2,column=1,sticky="wn",pady=(20,40),padx=10)

# --- Function that creates a new project folder and brings user to project manager screen ---
def create_new_project(self):

    # --- Creating project folder and json files to keep content of each tool ---
    os.mkdir(f"projects/{self.new_project_name.get()}")
    os.mkdir(f"projects/{self.new_project_name.get()}/text_notes")

    # --- Creating files used for saving data of each tool (except for text notes as these are handled using .txt files) ---
    for file_name in ["to_do_list.json", "calendar.json", "sticky_notes.json", "mindmap_notes.json","check_list.json"]:
        with open(f"projects/{self.new_project_name.get()}/{file_name}","w")as file:
            json.dump({},file,indent=4)

    # --- Setting up default project data configuration ---
    with open(f"projects/{self.new_project_name.get()}/project_data.json", "w") as file:
        default_data = {
                "current_tool":"",
                "current_mindmap_tool":"",
                "current_check_list_tool":"",
                "current_sticky_notes_tool":"",
                "current_text_note_tool":""
        }
        json.dump(default_data,file,indent=4)
        
    # --- Setting current project name ---
    self.current_project = self.new_project_name.get()
    
# --- Upon entering correct text into new_project_name_field, the Create button is enabled ---
def on_new_project_name_field_change(self, *args):
    text = self.new_project_name.get().strip()
    
    # --- Project name is limited to 25 characters and symbols that could break the file creation are disabled ---
    if len(text) > 25 or any(character in text for character in ['/', '\\', ':', '*', '?', '"', '<', '>', '|']):
        if self.create_project_button.cget("state")=="normal":
            self.create_project_button.configure(state="disabled")

    # --- If project name is already and existing project user won't be able to create another one with the same name ---        
    elif text in self.existing_projects and self.create_project_button.cget("state")=="normal":
        self.create_project_button.configure(state="disabled")

    # --- If roject name is valid and the button is disabled it will enabled ---        
    elif text and self.create_project_button.cget("state")=="disabled":
        self.create_project_button.configure(state="normal")
        
    # --- If there's no text in the entry and the button is turned on it will be disabled ---    
    elif not text and self.create_project_button.cget("state")=="normal":
        self.create_project_button.configure(state="disabled")

#  --- GUI forget helper ---
def forget_create_project_gui(self):       
    self.create_project_gui.pack_forget()
    self.create_project_gui.place_forget()          