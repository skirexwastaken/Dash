import customtkinter as ctk
import json

# --- Key Binds Menu ---
def key_binds_screen(self):

    # --- Loading app data ---
    with open("app_data.json","r") as file:
        app_data = json.load(file)

    # --- Variables for tracking entry of every key bind --- #Developer Note: Yes, I don't like this part either but to my knowledge there doesn't seem to be more efficient solution
    self.to_do_list_tool_key_bind = ctk.StringVar(value=app_data["key_binds"]["to_do_list_tool"])
    self.calendar_tool_key_bind = ctk.StringVar(value=app_data["key_binds"]["calendar_tool"])
    self.mindmap_tool_key_bind = ctk.StringVar(value=app_data["key_binds"]["mindmap_tool"])
    self.check_list_tool_key_bind = ctk.StringVar(value=app_data["key_binds"]["check_list_tool"])
    self.sticky_notes_tool_key_bind = ctk.StringVar(value=app_data["key_binds"]["sticky_notes_tool"])
    self.text_note_tool_key_bind = ctk.StringVar(value=app_data["key_binds"]["text_note_tool"])
    
    self.key_binds_gui = ctk.CTkFrame(master=self.root)
    self.key_binds_gui.pack(fill="both", expand=True)
    self.key_binds_gui.place(relx=0.5, rely=0.5, anchor="center")

    # --- Key Binds Title ---  
    appearance_label = ctk.CTkLabel(
        master=self.key_binds_gui,
        text="Key Binds",
        font=("Arial", 90, "bold")
    )

    appearance_label.grid(columnspan=2,row=0,pady=(40,20),padx=40)

    # --- To Do List Key Binds Change ---   
    to_do_list_tool_key_bind_label = ctk.CTkLabel(
        master=self.key_binds_gui,
        text="To Do List",
        font=("Arial", 40, "bold"),
    )

    to_do_list_tool_key_bind_label.grid(column=0,row=1,pady=20)
    
    self.to_do_list_tool_key_bind_entry = ctk.CTkEntry(
        master=self.key_binds_gui,
        textvariable=self.to_do_list_tool_key_bind,
        justify="center",
        font=("Arial", 40, "bold")
    )

    self.to_do_list_tool_key_bind_entry.grid(column=1,row=1,pady=20)
    self.to_do_list_tool_key_bind.trace_add("write", lambda *args: on_new_key_binds_name_field_change(self))

    # --- Calendar Key Binds Change ---  
    calendar_tool_key_bind_label = ctk.CTkLabel(
        master=self.key_binds_gui,
        text="Calendar",
        font=("Arial", 40, "bold"),
    )

    calendar_tool_key_bind_label.grid(column=0,row=2,pady=20)
    
    
    self.calendar_tool_key_bind_entry = ctk.CTkEntry(
        master=self.key_binds_gui,
        textvariable=self.calendar_tool_key_bind,
        justify="center",
        font=("Arial", 40, "bold")
    )

    self.calendar_tool_key_bind_entry.grid(column=1,row=2,pady=20)
    self.calendar_tool_key_bind.trace_add("write", lambda *args: on_new_key_binds_name_field_change(self))

    # --- Mindmap Key Binds Change ---  
    mindmap_tool_key_bind_label = ctk.CTkLabel(
        master=self.key_binds_gui,
        text="Mindmap",
        font=("Arial", 40, "bold"),
    )

    mindmap_tool_key_bind_label.grid(column=0,row=3,pady=20)
    
    
    self.mindmap_tool_key_bind_entry = ctk.CTkEntry(
        master=self.key_binds_gui,
        justify="center",
        textvariable=self.mindmap_tool_key_bind,
        font=("Arial", 40, "bold")
    )

    self.mindmap_tool_key_bind_entry.grid(column=1,row=3,pady=20)
    self.mindmap_tool_key_bind.trace_add("write", lambda *args: on_new_key_binds_name_field_change(self))

    # --- Check List Key Binds Change ---  
    check_list_tool_key_bind_label = ctk.CTkLabel(
        master=self.key_binds_gui,
        text="Check List",
        font=("Arial", 40, "bold"),
    )

    check_list_tool_key_bind_label.grid(column=0,row=4,pady=20)
    
    self.check_list_tool_key_bind_entry = ctk.CTkEntry(
        master=self.key_binds_gui,
        justify="center",
        textvariable=self.check_list_tool_key_bind,
        font=("Arial", 40, "bold"),
    )

    self.check_list_tool_key_bind_entry.grid(column=1,row=4,pady=20)
    self.check_list_tool_key_bind.trace_add("write", lambda *args: on_new_key_binds_name_field_change(self))

    # --- Sticky Notes Key Binds Change --
    sticky_notes_tool_key_bind_label = ctk.CTkLabel(
        master=self.key_binds_gui,
        text="Sticky Notes",
        font=("Arial", 40, "bold")
    )

    sticky_notes_tool_key_bind_label.grid(column=0,row=5,pady=20)
    
    self.sticky_notes_tool_key_bind_entry = ctk.CTkEntry(
        master=self.key_binds_gui,
        justify="center",
        textvariable=self.sticky_notes_tool_key_bind,
        font=("Arial", 40, "bold")
    )

    self.sticky_notes_tool_key_bind_entry.grid(column=1,row=5,pady=20)
    self.sticky_notes_tool_key_bind.trace_add("write", lambda *args: on_new_key_binds_name_field_change(self))

    # --- Text Note Key Binds Change --
    text_note_tool_key_bind_label = ctk.CTkLabel(
        master=self.key_binds_gui,
        text="Text Note",
        font=("Arial", 40, "bold")
    )  

    text_note_tool_key_bind_label.grid(column=0,row=6,pady=20) 
    
    self.text_note_tool_key_bind_entry = ctk.CTkEntry(
        master=self.key_binds_gui,
        justify="center",
        textvariable=self.text_note_tool_key_bind,
        font=("Arial", 40, "bold")
    ) 
     
    self.text_note_tool_key_bind_entry.grid(column=1,row=6,pady=20)
    self.text_note_tool_key_bind.trace_add("write", lambda *args: on_new_key_binds_name_field_change(self))

    # --- Button that saves the new key binds configuration ---
    self.save_button = ctk.CTkButton(
        master=self.key_binds_gui,
        text="Save",
        state="normal",
        font=("Arial", 40, "bold"),
        command=lambda: (forget_key_binds_gui(self),save_key_binds(self,app_data), self.settings_screen(self))
    )

    self.save_button.grid(column=0,row=7,pady=(20,40))
          
    # --- Button that brings user back to settings menu ---
    back_button = ctk.CTkButton(
        master=self.key_binds_gui,
        text="Back",
        font=("Arial", 40, "bold"),
        command=lambda: (forget_key_binds_gui(self), self.settings_screen(self))
    )

    back_button.grid(column=1,row=7,pady=(20,40))
    
# --- Function that saves the changed keybinds to app data ---
def save_key_binds(self,app_data):
    all_texts =  {
        "to_do_list_tool":self.to_do_list_tool_key_bind.get().rstrip(),
        "calendar_tool":self.calendar_tool_key_bind.get().rstrip(),
        "mindmap_tool":self.mindmap_tool_key_bind.get().rstrip(),
        "check_list_tool":self.check_list_tool_key_bind.get().rstrip(),
        "sticky_notes_tool":self.sticky_notes_tool_key_bind.get().rstrip(),
        "text_note_tool":self.text_note_tool_key_bind.get().rstrip()
    }
    for text in all_texts:
        app_data["key_binds"][text]=all_texts[text]
        
    with open("app_data.json","w") as file:
        json.dump(app_data,file,indent=4)

# --- Checks if all new key binds are in correct format ---        
def on_new_key_binds_name_field_change(self, *args):
    all_texts = [
        self.to_do_list_tool_key_bind.get().rstrip(),
        self.calendar_tool_key_bind.get().rstrip(),
        self.mindmap_tool_key_bind.get().rstrip(),
        self.check_list_tool_key_bind.get().rstrip(),
        self.sticky_notes_tool_key_bind.get().rstrip(),
        self.text_note_tool_key_bind.get().rstrip()
    ]
    
    all_valid = True

    for text in all_texts:
        if not (len(text) == 1 or text in ["<F1>","<F2>","<F3>","<F4>","<F5>","<F6>"]):
            all_valid = False
            break

    if all_valid:
        self.save_button.configure(state="normal")
    else:
        self.save_button.configure(state="disabled")
        
#  --- GUI forget helper ---   
def forget_key_binds_gui(self):      
    self.key_binds_gui.pack_forget()
    self.key_binds_gui.place_forget()