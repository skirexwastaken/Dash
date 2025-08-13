import customtkinter as ctk
import json

# --- Function that updates the current_tool in project data ---
def update_current_tool(self,tool,arg):
    self.project_data[tool]=arg
    with open(f"projects/{self.current_project}/project_data.json","w") as file:
        json.dump(self.project_data,file,indent=4)

# --- Project Manager Menu ---
def project_manager_screen(self):
    self.root.grid_rowconfigure(1, weight=1)
    self.root.grid_columnconfigure(1, weight=1)

    # --- Loading app data ---
    with open("app_data.json","r") as file:
        self.app_data = json.load(file)

    # --- Loading project data ---     
    with open(f"projects/{self.current_project}/project_data.json","r") as file:
            self.project_data = json.load(file)         
        
    self.project_manager_gui = ctk.CTkFrame(master=self.root)

    # --- Main Frame ---
    self.main_frame = ctk.CTkFrame(
        master=self.root,
        corner_radius=0,
        border_width=5,
        border_color="#1f6aa5"
        )
    self.main_frame.grid(row=1, column=1, sticky="nsew")
    self.main_frame.grid_rowconfigure(0, weight=1)
    self.main_frame.grid_columnconfigure(0, weight=1)

    # --- Default tool option when no tool is selected after creating a new project
    main_frame_label = ctk.CTkLabel(
        master=self.main_frame,
        text="No selected tool",
        font=("Arial", 20)
    )

    main_frame_label.grid(row=0, column=0, padx=20, pady=20)
    
    # --- Top Panel Frame ---
    
    self.top_panel = ctk.CTkFrame(
        master=self.root,
        corner_radius=0,
        border_width=5,
        border_color="#1f6aa5"
    )
    
    self.top_panel.grid(row=0, column=0, columnspan=2, sticky="nsew")
    
    # --- Top Panel Title --
    project_title = ctk.CTkLabel(
        master=self.top_panel,
        text=self.current_project,
        font=("Arial", 90,"bold")
    )

    project_title.pack(pady=20,padx=25)
    
    # --- Tool Panel Title ---
    
    self.tool_panel = ctk.CTkFrame(
        master=self.root,
        corner_radius=0,
        border_width=5,
        border_color="#1f6aa5"
    )
    
    self.tool_panel.grid(row=1, column=0, sticky="nswe")

    # --- Project Manager tool part label ---     
    tool_panel_label = ctk.CTkLabel(
        master=self.tool_panel,
        text="Tools",
        font=("Arial", 75, "bold")
    )

    tool_panel_label.pack(pady=15)
    
    # --- To Do List tool button ---
    if self.app_data["enabled_tools"]["to_do_list_tool"]:
        
        to_do_list_button = ctk.CTkButton(
            master=self.tool_panel, 
            text="To Do List",
            font=("Arial", 40,"bold"),
            command=lambda: ((self.to_do_list_tool(self) if not self.project_data["current_tool"]=="to_do_list_tool" else None),update_current_tool(self,"current_tool","to_do_list_tool"))
        )
        
        to_do_list_button.pack(pady=15, fill="x", padx=10)
        
        # -- Adding key bind from app data ---
        self.root.bind(f"{self.app_data["key_binds"]["to_do_list_tool"]}",lambda event: (self.to_do_list_tool(self)))

    # --- Calendar tool button ---
    if self.app_data["enabled_tools"]["calendar_tool"]:
        
        calendar_button = ctk.CTkButton(
            master=self.tool_panel, 
            text="Calendar",
            font=("Arial", 40,"bold"),
            command=lambda: ((self.calendar_tool(self) if not self.project_data["current_tool"]=="calendar_tool" else None),update_current_tool(self,"current_tool","calendar_tool"))
        )
        
        calendar_button.pack(pady=15, fill="x", padx=10)
        
        # -- Adding key bind from app data ---
        self.root.bind(f"{self.app_data["key_binds"]["calendar_tool"]}",lambda event: (self.calendar_tool(self)))

    # --- Mind Map tool button ---
    if self.app_data["enabled_tools"]["mindmap_tool"]:
        
        mindmap_button = ctk.CTkButton(
            master=self.tool_panel, 
            text="Mind Map",
            font=("Arial", 40,"bold"),
            command=lambda: ((self.mindmap_tool(self) if not self.project_data["current_tool"]=="mindmap_tool" else None),update_current_tool(self,"current_tool","mindmap_tool"))
        )
        
        mindmap_button.pack(pady=15, fill="x", padx=10)
        
        # -- Adding key bind from app data ---
        self.root.bind(f"{self.app_data["key_binds"]["mindmap_tool"]}",lambda event: (self.mindmap_tool(self)))

    # --- Check List tool button ---
    if self.app_data["enabled_tools"]["check_list_tool"]:
        
        check_list_button = ctk.CTkButton(
            master=self.tool_panel, 
            text="Check List",
            font=("Arial", 40,"bold"),
            command=lambda: ((self.check_list_tool(self) if not self.project_data["current_tool"]=="check_list_tool" else None),update_current_tool(self,"current_tool","check_list_tool"))
        )
        
        check_list_button.pack(pady=20, fill="x", padx=10)
        
        # -- Adding key bind from app data ---
        self.root.bind(f"{self.app_data["key_binds"]["check_list_tool"]}",lambda event: (self.check_list_tool(self)))
    
    # ---Sticky Notes tool button ---
    if self.app_data["enabled_tools"]["sticky_notes_tool"]:
        
        sticky_notes_button = ctk.CTkButton(
            master=self.tool_panel, 
            text="Sticky Notes",
            font=("Arial", 40,"bold"),
            command=lambda: ((self.sticky_notes_tool(self) if not self.project_data["current_tool"]=="sticky_notes_tool" else None),update_current_tool(self,"current_tool","sticky_notes_tool"))
        )
        
        sticky_notes_button.pack(pady=15, fill="x", padx=10)
        
        # -- Adding key bind from app data ---
        self.root.bind(f"{self.app_data["key_binds"]["sticky_notes_tool"]}",lambda event: (self.sticky_notes_tool(self)))
    
    # --- Text Note tool button ---
    if self.app_data["enabled_tools"]["text_note_tool"]:
        
        text_note_button = ctk.CTkButton(
            master=self.tool_panel, 
            text="Text Note",
            font=("Arial", 40,"bold"),
            command=lambda: ((self.text_note_tool(self) if not self.project_data["current_tool"]=="text_note_tool" else None),update_current_tool(self,"current_tool","text_note_tool"))
        )
        
        text_note_button.pack(pady=15, fill="x", padx=10)
        
        # -- Adding key bind from app data ---
        self.root.bind(f"{self.app_data["key_binds"]["text_note_tool"]}",lambda event: (self.text_note_tool(self)))

    # --- Spacing between Project Manager tools and general tools
    space_label = ctk.CTkLabel(
        master=self.tool_panel,
        text="- - - - -",
        font=("Arial", 30, "bold")
    )
    space_label.pack(pady=15)

    # --- Delete project button
    delete_project_button = ctk.CTkButton(
        master=self.tool_panel, 
        text="Delete Project",
        font=("Arial", 40,"bold"),
        command=lambda: (forget_project_manager_gui(self), self.root.grid_rowconfigure(0), self.root.grid_columnconfigure(0), self.delete_project_tool(self))
    )
    
    delete_project_button.pack(pady=15, fill="x", padx=10)
    
    # --- Button that brings user back to main menu ---
    main_menu_button = ctk.CTkButton(
        master=self.tool_panel, 
        text="Main Menu",
        font=("Arial", 40,"bold"),
        command=lambda: (forget_project_manager_gui(self), self.root.grid_rowconfigure(0), self.root.grid_columnconfigure(0), self.unbind_key_binds_tool(self), self.start_screen(self))
    )
    
    main_menu_button.pack(pady=15, fill="x", padx=10)
    
    # --- Checking for current_tool -> the last tool used before closing the app will be restored considering it's enabled in self.app_data ---
    match self.project_data["current_tool"]:
    
        case "to_do_list_tool":
            if self.app_data["enabled_tools"]["to_do_list_tool"]: 
                self.to_do_list_tool(self)
            else:
                self.project_data["current_tool"]=""    
                
        case "calendar_tool":
            if self.app_data["enabled_tools"]["calendar_tool"]: 
                self.calendar_tool(self) 
            else:
                self.project_data["current_tool"]="" 
                
        case "mindmap_tool":
            if self.app_data["enabled_tools"]["mindmap_tool"]: 
                self.mindmap_tool(self) 
            else:
                self.project_data["current_tool"]=""     
            
        case "check_list_tool":
            if self.app_data["enabled_tools"]["check_list_tool"]: 
                self.check_list_tool(self) 
            else:
                self.project_data["current_tool"]="" 
                
        case "sticky_notes_tool":
            if self.app_data["enabled_tools"]["sticky_notes_tool"]: 
                self.sticky_notes_tool(self) 
            else:
                self.project_data["current_tool"]="" 
            
        case "text_note_tool":
            if self.app_data["enabled_tools"]["text_note_tool"]: 
                self.text_note_tool(self)        
            else:
                self.project_data["current_tool"]=""
                
#  --- GUI forget helper ---
def forget_project_manager_gui(self):
    self.tool_panel.grid_forget()
    self.top_panel.grid_forget()
    self.main_frame.grid_forget()                