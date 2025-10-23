import customtkinter as ctk
import os

# --- Loading Project Menu ---
def load_project_screen(self):
    project_names=[]#List of all current projects

    # --- Loading all projects to project_names ---
    for project_name in os.listdir("projects"):
        file_path = os.path.join("projects", project_name)
        if os.path.isdir(file_path):
            project_names.append(project_name)
        
    self.load_project_gui = ctk.CTkFrame(master=self.root,)      

    # --- Creating Project Menu  Title ---
    load_project_label = ctk.CTkLabel(
        master=self.load_project_gui,
        text="Loading a project",
        font=("Arial", 90, "bold")
    )

    load_project_label.grid(columnspan=2,row=0,pady=(40,20),padx=40)
    
    # --- Label That shows currently selected project ---
    self.current_project_label = ctk.CTkLabel(
        master=self.load_project_gui,
        text="None",
        font=("Arial", 40, "bold")
    )

    self.current_project_label.grid(columnspan=2,row=1,pady=20)
        
    # --- Creating scroll frame for project names ---
    self.project_name_scroll_frame = ctk.CTkScrollableFrame(
        master=self.load_project_gui,
        height=50
    )
    
    self.project_name_scroll_frame.grid(columnspan=2,row=2,sticky="we",pady=20,padx=80)
     
    # --- Adds all project names to the scroll frame ---               
    for project_name in project_names:
        project_name_button = ctk.CTkButton(
            master=self.project_name_scroll_frame,
            text=project_name,
            font=("Arial", 20, "bold"),
            command=lambda name=project_name: (on_load_project_name_selected(self,name), ),
            corner_radius=5
        )

        project_name_button.pack(fill="x", pady=5,padx=10)
        
    # --- Button that loads a project ---
    self.load_project_button = ctk.CTkButton(
        master=self.load_project_gui,
        text="Load",
        state = "disabled",
        font=("Arial", 40, "bold"),
        command=lambda: (forget_load_project_gui(self), self.project_manager_screen(self))
        )
    
    self.load_project_button.grid(column=0,sticky="en",row=3,pady=20,padx=10)
         
    # --- Button that brings user back to main menu ---
    back_button = ctk.CTkButton(
        master=self.load_project_gui,
        text="Back",
        font=("Arial", 40, "bold"),
        command=lambda: (forget_load_project_gui(self), self.start_screen(self))
    )

    back_button.grid(column=1,sticky="wn",row=3,pady=(20,40),padx=10)

    # --- Displaying the UI (packing and placing at the end avoids render lag) ---
    self.load_project_gui.pack(fill="both", expand=True)
    self.load_project_gui.place(relx=0.5, rely=0.5, anchor="center")
    
# --- Upon clicking on one of the project names in the scroll frame, it is set to current project that is to be loaded ---
def on_load_project_name_selected(self, name):

    # --- Changing name of the lable indicating the currently selected project and updating the current_project name variable ---
    self.current_project_label.configure(text=name)
    self.current_project=name

    # --- Upon selecting a project the load button is enabled ---
    if self.load_project_button.cget("state")=="disabled":
        self.load_project_button.configure(state="normal")   
        
#  --- GUI forget helper ---
def forget_load_project_gui(self):         
    self.load_project_gui.pack_forget()
    self.load_project_gui.place_forget()