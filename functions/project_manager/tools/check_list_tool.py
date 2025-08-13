import customtkinter as ctk
import json

# --- Check List Tool ---
def check_list_tool(self):
    
    self.new_task_name = ctk.StringVar()
    
    # --- Configuring the Main Frame for Check List tool ---
    self.main_frame.grid_forget()
    self.main_frame = ctk.CTkFrame(
        master=self.root,
        corner_radius=0,
        border_width=5,
        border_color="#1f6aa5"
    )

    self.main_frame.grid(row=1, column=1, sticky="nsew")
    self.main_frame.grid_rowconfigure(1, weight=1)
    self.main_frame.grid_columnconfigure(0, weight=1)

    # --- Saving Check List tasks ---
    self.checklist_tasks = []

    # --- Input Frame for entry name ---
    input_frame = ctk.CTkFrame(master=self.main_frame)
    input_frame.grid(row=0, column=0, sticky="we", padx=20, pady=20)
    input_frame.grid_columnconfigure(0, weight=1)

    # --- Entry for task name ---
    self.task_name = ctk.CTkEntry(
        master=input_frame,
        placeholder_text="New task...",
        textvariable=self.new_task_name,
        font=("Arial", 20, "bold"),
    )
    
    self.task_name .grid(row=0, column=0, sticky="we", padx=(20, 0), pady=10)
    
    self.new_task_name.trace_add("write", lambda *args: on_new_task_name_field_change(self))

    # --- Button that adds task to first column ---
    self.add_task_button = ctk.CTkButton(
        master=input_frame,
        text="Add Task",
        command=lambda: add_task(self),
        state="disabled",
        font=("Arial", 20, "bold")
    )
    self.add_task_button.grid(row=0, column=1, padx=20, pady=10)

    # --- Creating two columns ---
    columns_frame = ctk.CTkFrame(master=self.main_frame)
    columns_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
    columns_frame.grid_columnconfigure((0, 1), weight=1)
    columns_frame.grid_rowconfigure(0, weight=1)

    column_titles = ["Unfinished", "Finished"]
    
    self.check_columns = []
    
    for index, title in enumerate(column_titles):
        column_frame = ctk.CTkFrame(columns_frame)
        column_frame.grid(row=0, column=index, sticky="nsew", padx=20, pady=5)
        column_frame.grid_columnconfigure(0, weight=1)
        column_frame.grid_rowconfigure(1, weight=1)

        column_title_label = ctk.CTkLabel(
            master=column_frame, 
            text=title, 
            font=("Arial", 20, "bold")
        )
        column_title_label.grid(row=0, column=0, pady=(5, 2), sticky="ew")

        # --- Frame for stacking tasks ---
        task_frame = ctk.CTkScrollableFrame(column_frame)
        task_frame.grid(row=1, column=0, sticky="nsew")
        task_frame.grid_columnconfigure(0, weight=1)

        self.check_columns.append(task_frame)
        
    load_tasks(self)
    
# --- Function that saves all Check List tasks ---    
def save_tasks(self):
        data = []
        for task in self.checklist_tasks:
            item = {
                'text': task['text'],
                'finished': task['finished']
            }
            data.append(item)

        with open(f"projects/{self.current_project}/check_list.json", "w") as f:
            json.dump(data, f, indent=2)

# --- Function that loads all Check List tasks ---
def load_tasks(self):
    with open(f"projects/{self.current_project}/check_list.json", "r") as f:
        data = json.load(f)
        
    for task in data:
        text = task.get('text')
        finished = task.get('finished', False)
        create_task(self, text, finished)  # self passed here  

# --- Function that creates tasks in the scrolable frame ---
def create_task(self, text, finished=False):
    column_index = 1 if finished else 0
    item_frame = ctk.CTkFrame(self.check_columns[column_index])
    item_frame.pack(fill="x", pady=2, padx=2)

    # --- Task Label ---
    task_label = ctk.CTkLabel(
        item_frame,
        text=text,
        anchor="w",
        font=("Arial", 20, "bold")
    )

    task_label.grid(row=0, column=0, sticky="we", padx=5)
    item_frame.grid_columnconfigure(0, weight=1)

    # --- Move button ---
    move_button = ctk.CTkButton(
        item_frame,
        text=">" if not finished else "<",
        width=40,
        command=lambda: move_task(self, item_frame),
        font=("Arial", 20, "bold")
    )

    move_button.grid(row=0, column=1, padx=2, pady=2)

    # --- Delete button ---
    delete_button = ctk.CTkButton(
        item_frame,
        text="X",
        width=40,
        fg_color="red",
        hover_color="darkred",
        command=lambda: delete_item(self, item_frame),
        font=("Arial", 20, "bold")
    )
    delete_button.grid(row=0, column=2, padx=2, pady=2)

    self.checklist_tasks.append(
        {
        'text': text,
        'finished': finished,
        'widget': item_frame
        }
    )

# --- Removes task from either column ---
def delete_item(self, item_frame):
    for task in self.checklist_tasks:
        if task['widget'] == item_frame:
            self.checklist_tasks.remove(task)
            break

    item_frame.destroy()
    save_tasks(self)

# --- Adds task to first column ---
def add_task(self):
        text = self.task_name .get().strip()
        if not text:
            return
        create_task(self,text, finished=False)
        self.task_name .delete(0, ctk.END)
        save_tasks(self)  

# --- Moves tasks between columns ---
def move_task(self, item_frame):
    for task in self.checklist_tasks:
        if task['widget'] == item_frame:
            item_data = task
            break

    if not item_data:
        return
    
    text = item_data['text']
    finished = not item_data['finished']

    # --- Removes task from old column ---
    item_frame.destroy()
    self.checklist_tasks.remove(item_data)

    # --- Adds task to new column ---
    create_task(self, text, finished)
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