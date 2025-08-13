import customtkinter as ctk
import tkinter as tk
import json

# --- Sticky Notes Tool ---
def sticky_notes_tool(self):
    # --- Sticky notes variables ---
    self.sticky_notes = []
    self.save_after_id = None
    
    # ---  Main Frame ---
    self.main_frame.grid_forget()
    self.main_frame = ctk.CTkFrame(
        master=self.root,
        border_width=5,
        border_color="#1f6aa5"
    )
    
    self.main_frame.grid(row=1, column=1, sticky="nsew")
    self.main_frame.grid_rowconfigure(1, weight=1)
    self.main_frame.grid_columnconfigure(0, weight=1)

    # --- Sticky Notes tool panel ---
    sticky_notes_tools_panel = ctk.CTkFrame(master=self.main_frame, height=40)
    sticky_notes_tools_panel.grid(row=0, column=0, sticky="we", padx=20, pady=20)
    sticky_notes_tools_panel.grid_columnconfigure((0, 1, 2), weight=0)

    # --- Add Note button ---
    add_sticky_note_button = ctk.CTkButton(
        master=sticky_notes_tools_panel,
        text='Add Note',
        font=("Arial", 20,"bold"),
        command=lambda: (add_note_ui(self), trigger_sticky_notes_autosave(self))
    )
    add_sticky_note_button.pack(side='left', padx=10, pady=10)

    # --- Sticky Notes Canvas ---
    self.canvas = tk.Canvas(
        master=self.main_frame, 
        highlightthickness=0, 
        bg="#323232"
    )
    self.canvas.grid(row=1, column=0, sticky="nsew", pady=20, padx=20)
    
    # --- Loading sticky notes ---
    with open(f"projects/{self.current_project}/sticky_notes.json", 'r', encoding="utf-8") as f:
        data = json.load(f)
        for note_data in data:
            add_note_ui(self, **note_data)
    
    # --- Start auto save ---
    trigger_sticky_notes_autosave(self)

# --- Sticky Notes Helper Functions ---
def add_note_ui(self, x=100, y=100, title="Title", text="", width=200, height=60):
    Note(self.canvas, self, x=x, y=y, title=title, text=text, width=width, height=height)

# --- Saves all sticky notes data to a JSON file ---
def save_sticky_notes(self):
    with open(f"projects/{self.current_project}/sticky_notes.json", "w", encoding="utf-8") as f:
        json.dump([note.to_dict() for note in self.sticky_notes], f, indent=2, ensure_ascii=False)

# --- Sticky notes save function with a delay -> Auto Save is triggered every 0.5 seconds ---
def trigger_sticky_notes_autosave(self):
    if self.save_after_id:
        try:
            self.main_frame.after_cancel(self.save_after_id)
        except Exception:
            pass
    self.save_after_id = self.main_frame.after(500, lambda: save_sticky_notes(self))

# --- Note Class ---
class Note(ctk.CTkFrame):
    def __init__(self, master, owner, x=50, y=50, title="Title", text="", width=200, height=60, **kwargs):
        super().__init__(master, border_width=1)
        self.place(x=x, y=y)
        self.owner = owner
        self.owner.sticky_notes.append(self)
        self.configure(width=width, height=height)

        # --- Sticky Note Title Field ---
        self.note_title = ctk.CTkEntry(
            master=self, 
            font=('Arial', 20, 'bold')
        )
        
        self.note_title.insert(0, title)
        self.note_title.pack(fill='x', padx=5, pady=(20, 0))
        self.note_title.bind("<KeyRelease>", lambda event: trigger_sticky_notes_autosave(self.owner))

        # --- Sticky Note Text Box ---
        self.note_textbox = ctk.CTkTextbox(master=self, wrap='word', font=('Arial', 20, "bold"))
        self.note_textbox.insert('1.0', text)
        self.note_textbox.pack(fill='both', expand=True, padx=20, pady=10)
        self.note_textbox.bind('<KeyRelease>', lambda event: trigger_sticky_notes_autosave(self.owner))

        # --- Delete Button ---
        self.delete_button = ctk.CTkButton(
            master=self, 
            text="Delete", 
            command=self.delete, 
            fg_color="red", 
            hover_color="#aa0000",
            font=("Arial", 20,"bold")
        )
        
        self.delete_button.pack(pady=(0, 20))

        self.bind_events()

    # --- Binds mouse events for dragging the note ---
    def bind_events(self):
        self.bind('<Button-1>', self.start_move)
        self.bind('<B1-Motion>', self.do_move)

    # --- Saves the starting coordinates for dragging ---
    def start_move(self, event):
        self._drag_start_x = event.x
        self._drag_start_y = event.y

    # --- Moves the widget based on the mouse drag ---
    def do_move(self, event):
        dx = event.x - self._drag_start_x
        dy = event.y - self._drag_start_y

        canvas_width = self.master.winfo_width()
        canvas_height = self.master.winfo_height()

        new_x = self.winfo_x() + dx
        new_y = self.winfo_y() + dy

        x = max(0, min(new_x, canvas_width - self.winfo_width()))
        y = max(0, min(new_y, canvas_height - self.winfo_height()))

        self.place(x=x, y=y)
        trigger_sticky_notes_autosave(self.owner)

    # --- Deletes the note and triggers an autosave ---
    def delete(self):
        if self in self.owner.sticky_notes:
            self.owner.sticky_notes.remove(self)
        self.destroy()
        trigger_sticky_notes_autosave(self.owner)

    # --- Converts note data to a dictionary for saving ---
    def to_dict(self):
        return {
            "x": self.winfo_x(),
            "y": self.winfo_y(),
            "title": self.note_title.get(),
            "text": self.note_textbox.get("1.0", "end-1c"),
            "width": self.winfo_width(),
            "height": self.winfo_height()
        }