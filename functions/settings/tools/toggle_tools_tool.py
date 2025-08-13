import customtkinter as ctk
import json

# --- Toogle Tools Menu ---
def toggle_tools_screen(self):
    self.toggle_tools_gui = ctk.CTkFrame(master=self.root)
    self.toggle_tools_gui.pack(fill="both", expand=True)
    self.toggle_tools_gui.place(relx=0.5, rely=0.5, anchor="center")
    
    # --- Loading app data ---
    with open("app_data.json","r") as file:
        app_data = json.load(file)

    # --- Status Title ---  
    appearance_label = ctk.CTkLabel(
        master=self.toggle_tools_gui,
        text="Toggle Tools",
        font=("Arial", 90, "bold")
    )

    appearance_label.grid(columnspan=2,row=0,pady=(40,20),padx=40)

    # --- To Do List Status Change ---   
    to_do_list_tool_toggle_label = ctk.CTkLabel(
        master=self.toggle_tools_gui,
        text="To Do List",
        font=("Arial", 40, "bold"),
    )

    to_do_list_tool_toggle_label.grid(column=0,row=1,pady=20)
    self.to_do_list_variable = ctk.BooleanVar(value=app_data["enabled_tools"]["to_do_list_tool"])
    
    self.to_do_list_tool_toggle_checkbox = ctk.CTkCheckBox(
        master=self.toggle_tools_gui,
        text="",
        variable=self.to_do_list_variable,
        font=("Arial", 40, "bold")
    )

    self.to_do_list_tool_toggle_checkbox.grid(column=1,row=1,pady=20)
    
    # --- Calendar Status Change ---  
    calendar_tool_toggle_label = ctk.CTkLabel(
        master=self.toggle_tools_gui,
        text="Calendar",
        font=("Arial", 40, "bold"),
    )

    calendar_tool_toggle_label.grid(column=0,row=2,pady=20)
    self.calendar_variable = ctk.BooleanVar(value=app_data["enabled_tools"]["calendar_tool"])
    
    self.calendar_tool_toggle_checkbox = ctk.CTkCheckBox(
        master=self.toggle_tools_gui,
        text="",
        variable=self.calendar_variable,
        font=("Arial", 40, "bold")
    )
    self.calendar_tool_toggle_checkbox.grid(column=1,row=2,pady=20)
    
    # --- Mindmap Status Change ---  
    mindmap_tool_toggle_label = ctk.CTkLabel(
        master=self.toggle_tools_gui,
        text="Mindmap",
        font=("Arial", 40, "bold"),
    )

    mindmap_tool_toggle_label.grid(column=0,row=3,pady=20)
    self.mindmap_variable = ctk.BooleanVar(value=app_data["enabled_tools"]["mindmap_tool"])
    
    self.mindmap_tool_toggle_checkbox = ctk.CTkCheckBox(
        master=self.toggle_tools_gui,
        text="",
        variable=self.mindmap_variable,
        font=("Arial", 40, "bold")
    )

    self.mindmap_tool_toggle_checkbox.grid(column=1,row=3,pady=20)
    
    # --- Check List Status Change ---  
    check_list_tool_toggle_label = ctk.CTkLabel(
        master=self.toggle_tools_gui,
        text="Check List",
        font=("Arial", 40, "bold"),
    )

    check_list_tool_toggle_label.grid(column=0,row=4,pady=20)
    self.check_list_variable = ctk.BooleanVar(value=app_data["enabled_tools"]["check_list_tool"])
    
    self.check_list_tool_toggle_checkbox = ctk.CTkCheckBox(
        master=self.toggle_tools_gui,
        text="",
        variable=self.check_list_variable,
        font=("Arial", 40, "bold"),
    )
    
    self.check_list_tool_toggle_checkbox.grid(column=1,row=4,pady=20)
    
    # --- Sticky Notes Status Change --
    sticky_notes_tool_toggle_label = ctk.CTkLabel(
        master=self.toggle_tools_gui,
        text="Sticky Notes",
        font=("Arial", 40, "bold")
    )

    sticky_notes_tool_toggle_label.grid(column=0,row=5,pady=20)
    self.sticky_notes_variable = ctk.BooleanVar(value=app_data["enabled_tools"]["sticky_notes_tool"])
    
    self.sticky_notes_tool_toggle_checkbox = ctk.CTkCheckBox(
        master=self.toggle_tools_gui,
        text="",
        variable=self.sticky_notes_variable,
        font=("Arial", 40, "bold")
    )

    self.sticky_notes_tool_toggle_checkbox.grid(column=1,row=5,pady=20)
    
    # --- Text Note Status Change --
    text_note_tool_toggle_label = ctk.CTkLabel(
        master=self.toggle_tools_gui,
        text="Text Note",
        font=("Arial", 40, "bold")
    )  

    text_note_tool_toggle_label.grid(column=0,row=6,pady=20) 
    self.text_note_variable = ctk.BooleanVar(value=app_data["enabled_tools"]["text_note_tool"])
    
    self.text_note_tool_toggle_checkbox = ctk.CTkCheckBox(
        master=self.toggle_tools_gui,
        text="",
        variable=self.text_note_variable,
        font=("Arial", 40, "bold")
    )

    self.text_note_tool_toggle_checkbox.grid(column=1,row=6,pady=20)
    
    # --- Button that saves the new tool status configuration ---
    save_button= ctk.CTkButton(
        master=self.toggle_tools_gui,
        text="Save",
        font=("Arial", 40, "bold"),
        command=lambda: (forget_toggle_tools_gui(self), self.settings_screen(self),save_tools_status(self,app_data))
    )

    save_button.grid(column=0,row=7,pady=(20,40))
          
    # --- Button that brings user back to settings menu ---
    back_button = ctk.CTkButton(
        master=self.toggle_tools_gui,
        text="Back",
        font=("Arial", 40, "bold"),
        command=lambda: (forget_toggle_tools_gui(self), self.settings_screen(self))
    )

    back_button.grid(column=1,row=7,pady=(20,40))
    
    # --- Function that saves the changed keybinds to app data ---
    def save_tools_status(self,app_data):#Developer Note: This could be probably shortened but it's still only 6 lines
        app_data["enabled_tools"]["to_do_list_tool"]=self.to_do_list_variable.get()
        
        app_data["enabled_tools"]["calendar_tool"]=self.calendar_variable.get()
            
        app_data["enabled_tools"]["mindmap_tool"]=self.mindmap_variable.get()
            
        app_data["enabled_tools"]["check_list_tool"]=self.check_list_variable.get()
            
        app_data["enabled_tools"]["sticky_notes_tool"]=self.sticky_notes_variable.get()
            
        app_data["enabled_tools"]["text_note_tool"]=self.text_note_variable.get()      

        # --- Saves the updated app data to json file ---            
        with open("app_data.json","w") as file:
            json.dump(app_data,file,indent=4)
            
#  --- GUI forget helper --- 
def forget_toggle_tools_gui(self):
    self.toggle_tools_gui.pack_forget()
    self.toggle_tools_gui.place_forget()             