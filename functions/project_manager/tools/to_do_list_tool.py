import customtkinter as ctk
import json

# --- To Do List Tool ---
def to_do_list_tool(self):
    
    self.new_task_name = ctk.StringVar() #Name of a new task in entry
    
    # --- Configuring the Main Frame for Check List tool ---
    self.main_frame.grid_forget()
    self.main_frame = ctk.CTkFrame(
        master=self.root,
        corner_radius=0,
        border_width=5,
        border_color="#1f6aa5"
    )
    self.main_frame.grid(row=1, column=1, sticky="nsew")
    self.main_frame.grid_rowconfigure(1, weight=1)#Developer Note: input bar = row 0, panels = row 1
    self.main_frame.grid_columnconfigure(0, weight=1)

    # --- Saving To Do List tasks ---
    self.todo_tasks = []

    # --- Input Frame for entry name ---
    input_frame = ctk.CTkFrame(master=self.main_frame)
    input_frame.grid(row=0, column=0, sticky="we", padx=20, pady=20)
    input_frame.grid_columnconfigure(0, weight=1)

    # --- Entry for task name ---
    self.task_name = ctk.CTkEntry(
        master=input_frame,
        placeholder_text="New task...",
        textvariable=self.new_task_name,
        font=("Arial", 20,"bold"),
        )
    
    self.task_name.grid(row=0, column=0, sticky="we", padx=(20, 0),pady=10)

    self.new_task_name.trace_add("write", lambda *args: on_new_task_name_field_change(self))
    
    # --- Button that adds task to first column ---
    self.add_task_button = ctk.CTkButton(
        master=input_frame, 
        text="Add Task",
        state="disabled",
        command=lambda: add_task(self),
        font=("Arial", 20,"bold")
        )
    
    self.add_task_button.grid(row=0, column=1,padx=20,pady=10)

    # --- Creating three columns ---
    columns_frame = ctk.CTkFrame(master=self.main_frame)
    columns_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
    columns_frame.grid_columnconfigure((0, 1, 2), weight=1)
    columns_frame.grid_rowconfigure(0, weight=1)

    self.todo_panels = []
    self.todo_lists = []

    column_titles = ["To Do", "In Progress", "Done"]
    for index, title in enumerate(column_titles): #Developer Note: Turns the list into a dict with keys being numbers
        column_frame = ctk.CTkFrame(master=columns_frame)
        column_frame.grid(row=0, column=index, sticky="nsew", padx=20, pady=5)
        column_frame.grid_columnconfigure(0, weight=1)
        column_frame.grid_rowconfigure(1, weight=1)#Developer Note: Makes the scrollable frame expand

        column_title_label = ctk.CTkLabel(
            master=column_frame,
            text=title,
            font=("Arial", 20, "bold"))
        
        column_title_label.grid(row=0, column=0, pady=(5, 2), sticky="ew")

        # --- Frame for stacking tasks ---
        task_frame = ctk.CTkScrollableFrame(master=column_frame)
        task_frame.grid(row=1, column=0, sticky="nsew")
        task_frame.grid_columnconfigure(0, weight=1)

        self.todo_panels.append(column_frame)
        self.todo_lists.append(task_frame)      

        #Developer Note: The reason behind putting the scrollable frame inside of the regular frame is to make the column title on top be static

    # --- Loads all tasks ---
    load_tasks(self)

# --- Function that saves all To Do List tasks ---      
def save_tasks(self):
        data = []
        for task in self.todo_tasks:
            item = {
                'text': task['text'],
                'panel': task['panel']
            }
            data.append(item)
        with open(f"projects/{self.current_project}/to_do_list.json", "w") as f:
            json.dump(data, f, indent=2)

# --- Function that loads all To Do List tasks ---
def load_tasks(self):
    with open(f"projects/{self.current_project}/to_do_list.json", "r") as f:
            data = json.load(f)
            for task in data:
                text = task.get('text')
                panel = task.get('panel')
                if panel in (0, 1, 2) and isinstance(text, str):
                    create_task(self, text, panel)

# --- Function that creates tasks in the scrolable frame ---
def create_task(self, text, panel_index):
    task_frame = ctk.CTkFrame(self.todo_lists[panel_index])
    task_frame.pack(fill="x", pady=2, padx=2)

    # --- Button that moves the task to the column on the left ---
    move_left_button = ctk.CTkButton(
        master=task_frame, 
        text="<", 
        width=30,
        command=lambda f=task_frame, idx=panel_index: move_task(self,f, idx, -1),
        font=("Arial", 20,"bold")
    )

    move_left_button.grid(row=0, column=0, padx=2, pady=2)

    # --- If the task reaches the last column on the left, the move_left_button is disabled ---
    if panel_index == 0:
        move_left_button.configure(state="disabled")

    # --- Task Name Label ---
    task_name_label = ctk.CTkLabel(
         master=task_frame,
         text=text,
         anchor="w",
         font=("Arial", 20,"bold")
    )
    task_name_label .grid(row=0, column=1, sticky="we", padx=5)
    task_frame.grid_columnconfigure(1, weight=1)

    # --- Button that moves the task to the column on the right ---
    move_right_button = ctk.CTkButton(
        task_frame, 
        text=">", 
        width=30,
        command=lambda f=task_frame, idx=panel_index: move_task(self,f, idx, 1),
        font=("Arial", 20,"bold")
    )
    move_right_button.grid(row=0, column=2, padx=2, pady=2)

    # --- If the task reaches the last column on the right, the move_right_button is disabled ---
    if panel_index == 2:
        move_right_button.configure(state="disabled")

    # --- Button that deleted the task ---
    delete_button = ctk.CTkButton(
        master=task_frame, 
        text="X", 
        width=30, 
        fg_color="red", 
        hover_color="darkred",
        command=lambda f=task_frame: delete_task(self,f),
        font=("Arial", 20,"bold")
    )
    delete_button.grid(row=0, column=3, padx=2, pady=2)

    self.todo_tasks.append({'text': text, 'panel': panel_index, 'widget': task_frame})

# --- Removes task from any column ---
def delete_task(self,task_frame):
    for task in self.todo_tasks:
        if task['widget'] == task_frame:
            self.todo_tasks.remove(task)
            break
    task_frame.destroy()
    save_tasks(self)         
                    
# --- Adds task to first column ---
def add_task(self):
        text = self.task_name.get().strip()
        create_task(self,text, panel_index=0)
        self.task_name.delete(0, ctk.END)
        save_tasks(self)
                    
# --- Moves tasks between columns ---
def move_task(self,task_frame, current_index, direction):
    new_index = current_index + direction
    if new_index < 0 or new_index > 2:
        return
    task_data = next((t for t in self.todo_tasks if t['widget'] == task_frame), None)
    if not task_data:
            return
    # --- Get the text from the label widget ---
    text_widget = next((w for w in task_frame.winfo_children() if isinstance(w, ctk.CTkLabel)), None)
    if text_widget:
        text = text_widget.cget("text")
    else:
        return
        
    # --- Destroy the old task frame and remove data ---
    task_frame.destroy()
    self.todo_tasks.remove(task_data)
        
    # --- Create a new task in the new panel ---
    create_task(self,text, new_index)
    save_tasks(self)

# --- Upon entering correct text into new_task_name the add button is enabled ---
def on_new_task_name_field_change(self, *args):
    text = self.new_task_name.get().strip()
    
    if len(text) > 25:#Task name length is limited to 25 characters including spaces
        if self.add_task_button.cget("state")=="normal":
            self.add_task_button.configure(state="disabled")
              
    elif text and self.add_task_button.cget("state")=="disabled":
        self.add_task_button.configure(state="normal")
        
    elif not text and self.add_task_button.cget("state")=="normal":
        self.add_task_button.configure(state="disabled")                   