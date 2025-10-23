import customtkinter as ctk
import tkinter as tk
import json

# --- Mind Map Tool ---
def mindmap_tool(self):
    # --- Mind Map Notes variables ---
    self.mindmap_notes = []
    self.connections = []
    self._save_after_id_holder = [None]

    # ---  Main Frame ---
    self.main_frame.grid_forget()
    self.main_frame = ctk.CTkFrame(master=self.root, border_width=5, border_color="#1f6aa5")
    self.main_frame.grid(row=1, column=1, sticky="nsew")
    self.main_frame.grid_rowconfigure(1, weight=1)
    self.main_frame.grid_columnconfigure(0, weight=1)

    # --- Mind Map Notes tool bar---
    mindmap_notes_tool_panel = ctk.CTkFrame(
        master=self.main_frame, 
        height=40
    )
    
    mindmap_notes_tool_panel.grid(row=0, column=0, sticky="we", pady=20, padx=20)

    # --- Mind Map Notes Canvas ---
    self.canvas = tk.Canvas(
        master=self.main_frame,
        bg="#323232",
        highlightthickness=0
    )
    
    self.canvas.grid(row=1, column=0, sticky="nsew", pady=20, padx=20)

    # --- Add Mind Map Note button ---
    add_mindmap_note_button = ctk.CTkButton(
        master=mindmap_notes_tool_panel,
        text='Add Note',
        font=("Arial", 20, "bold"),
        command=lambda: Note(self.canvas, self))
    
    add_mindmap_note_button.pack(side='left', padx=10, pady=10)
    
    # --- Loading all saved Mind Map notes ---
    with open(f"{f"projects/{self.current_project}"}/mindmap_notes.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        self.midnmap_notes = {"notes": data.get("notes", []),"connections": data.get("connections", [])}

    for mindmap_note in self.midnmap_notes["notes"]:
        Note(self.canvas, self, **mindmap_note)

    self.root.update_idletasks()
    self.root.after(50,lambda: load_connections(self))
    self.canvas.bind("<Configure>", lambda e: redraw_connections(self.connections))

# --- Loading connections dot - dot ---    
def load_connections(self):
        for connection in self.midnmap_notes["connections"]:
            add_connection(
                self.mindmap_notes[connection["start"]["note_index"]].dots[connection["start"]["side"]],
                self.mindmap_notes[connection["end"]["note_index"]].dots[connection["end"]["side"]],
                self.connections,
                self.canvas,
                lambda: trigger_mindmap_notes_autosave(self.main_frame, lambda: save_data(self.mindmap_notes, self.connections, f"projects/{self.current_project}"), self._save_after_id_holder)
            )
        redraw_connections(self.connections)    

# --- Saves all Mind Map sticky notes data to a JSON file ---
def save_data(mindmap_notes, connections, project_path):
    data = {
        "notes": [note.to_dict() for note in mindmap_notes],
        "connections": [
            {
                "start": {"note_index": mindmap_notes.index(connection[0].owner), "side": connection[0].side},
                "end": {"note_index": mindmap_notes.index(connection[1].owner), "side": connection[1].side}
            }
            for connection in connections if connection[0].owner in mindmap_notes and connection[1].owner in mindmap_notes
        ]
    }
    
    with open(f"{project_path}/mindmap_notes.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# --- Mind Map sticky notes save function with a delay ---
def trigger_mindmap_notes_autosave(main_frame, save_func, after_id_holder):
    if after_id_holder[0]:
        main_frame.after_cancel(after_id_holder[0])
    after_id_holder[0] = main_frame.after(500, save_func)

# --- Creates connection between two dots ---
def add_connection(dot1, dot2, connections, canvas, autosave_func):
    
    # --- Making sure all connections are removed ---
    remove_connection(dot1, connections, canvas, autosave_func)
    
    remove_connection(dot2, connections, canvas, autosave_func)
    
    # --- Creating new connection ---
    if not any((d1 == dot1 and d2 == dot2) or (d1 == dot2 and d2 == dot1) for d1, d2, _ in connections):
        line_id = canvas.create_line(
            *dot1.get_center_coords(),
            *dot2.get_center_coords(),
            fill="red",
            width=2
        )
        
        connections.append((dot1, dot2, line_id))
        
        canvas.tag_bind(
        line_id, "<Button-1>",
        lambda e: remove_connection(line_id, connections, canvas, autosave_func)
        )
        
        autosave_func()

# --- Removes connection between two dots ---
def remove_connection(target, connections, canvas, autosave_func):
    for connection in connections[:]:
        if target in connection or target == connection[2]:
            canvas.delete(connection[2])
            connections.remove(connection)
            autosave_func()

# --- Redraws connection lines ---
def redraw_connections(connections):
    for d1, d2, line_id in connections:
        canvas = d1.owner.owner.canvas
        canvas.coords(line_id, *d1.get_center_coords(), *d2.get_center_coords())

# --- Note Class ---
class Note(ctk.CTkFrame):
    def __init__(self, master, owner, x=100, y=100, title="Title", text="", width=200, height=60):
        super().__init__(master, border_width=1, width=width, height=height)
        self.owner = owner 
        owner.mindmap_notes.append(self)
        self.place(x=x, y=y)

        # --- Mind Map Note Title Field ---
        self.note_title = ctk.CTkEntry(
            master=self, 
            font=('Arial', 20, 'bold')
        )
        
        self.note_title.insert(0, title)
        self.note_title.pack(fill='x', padx=5, pady=(20, 0))
        self.note_title.bind("<KeyRelease>", lambda e: self.autosave())
        
        # --- Mind Map Note Text Box ---
        self.note_textbox = ctk.CTkTextbox(
            master=self, 
            wrap='word',
            font=('Arial', 20, "bold")
        )
        
        self.note_textbox.insert('1.0', text)
        self.note_textbox.pack(fill='both', expand=True, padx=20, pady=10)
        self.note_textbox.bind('<KeyRelease>', lambda e: self.autosave())

        # --- Mind Map Note Delete button ---
        delete_button = ctk.CTkButton(
            master=self, 
            text="Delete", 
            fg_color="red", 
            hover_color="#aa0000",
            font=("Arial", 20, "bold"), 
            command=self.delete
        )
        
        delete_button.pack(pady=(0, 20))

        self.dots = {side: self.Dot(self, side) for side in ("top", "right", "bottom", "left")}
        self.dots["top"].place(relx=0.5, rely=0, anchor='n')
        self.dots["right"].place(relx=1, rely=0.5, anchor='e')
        self.dots["bottom"].place(relx=0.5, rely=1, anchor='s')
        self.dots["left"].place(relx=0, rely=0.5, anchor='w')

        self.bind("<Button-1>", self.start_move)
        self.bind("<B1-Motion>", self.do_move)

    # --- Mind Map Notes auto save function ---
    def autosave(self):
        trigger_mindmap_notes_autosave(
            self.owner.main_frame,
            lambda: save_data(self.owner.mindmap_notes, self.owner.connections, f"projects/{self.owner.current_project}"),
            self.owner._save_after_id_holder
        )

    # --- Class behind red dots located in the middle of each Note's side ---
    class Dot(ctk.CTkFrame):
        def __init__(self, note, side):
            super().__init__(note, width=12, height=12, fg_color="red", corner_radius=6)
            self.side, self.owner = side, note
            
            self.bind("<ButtonPress-1>", self.start_line)
            self.bind("<B1-Motion>", self.draw_line)
            self.bind("<ButtonRelease-1>", self.end_line)
            
            self.drag_line = None

        # --- Creates connection line ---
        def start_line(self, _):
            remove_connection(self, self.owner.owner.connections, self.owner.owner.canvas, self.owner.autosave)
            self.drag_line = self.owner.owner.canvas.create_line(*self.get_center_coords(), *self.get_center_coords(), fill="red", width=2)

        # --- Renders connection line while dragging it ---
        def draw_line(self, _):
            if self.drag_line:
                cx, cy = self.get_center_coords()
                
                mx = self.owner.owner.canvas.winfo_pointerx() - self.owner.owner.canvas.winfo_rootx()
                my = self.owner.owner.canvas.winfo_pointery() - self.owner.owner.canvas.winfo_rooty()
                
                self.owner.owner.canvas.coords(self.drag_line, cx, cy, mx, my)

        # --- Connects line to red dot if it has been dragged to it ---
        def end_line(self, _):
            if not self.drag_line:
                return
            
            mx = self.owner.owner.canvas.winfo_pointerx() - self.owner.owner.canvas.winfo_rootx()
            my = self.owner.owner.canvas.winfo_pointery() - self.owner.owner.canvas.winfo_rooty()
            
            for note in self.owner.owner.mindmap_notes:
                for dot in note.dots.values():
                    if dot != self and ((mx - dot.get_center_coords()[0]) ** 2 + (my - dot.get_center_coords()[1]) ** 2) ** 0.5 < 15:
                        add_connection(self, dot, self.owner.owner.connections, self.owner.owner.canvas, self.owner.autosave)
                        
                        self.owner.owner.canvas.delete(self.drag_line)
                        
                        self.drag_line = None
                        return
            self.owner.owner.canvas.delete(self.drag_line)
            
            self.drag_line = None

        # --- Function used to get middle of the side coords ---
        def get_center_coords(self):
            return (
                self.owner.winfo_x() + self.winfo_x() + self.winfo_width() // 2,
                self.owner.winfo_y() + self.winfo_y() + self.winfo_height() // 2
            )

    # --- Starts the moving process ---
    def start_move(self, e):
        self._start = (e.x, e.y)

    # --- Updates the line upon move ---
    def do_move(self, e):
        dx, dy = e.x - self._start[0], e.y - self._start[1]
        self.place(
            x=max(0, min(self.winfo_x() + dx, self.master.winfo_width() - self.winfo_width())),
            y=max(0, min(self.winfo_y() + dy, self.master.winfo_height() - self.winfo_height()))
        )
        redraw_connections(self.owner.connections)
        self.autosave()

    # --- Function that deletes the dots ---
    def delete(self):
        for dot in self.dots.values():
            remove_connection(dot, self.owner.connections, self.owner.canvas, self.autosave)
        if self in self.owner.mindmap_notes:
            self.owner.mindmap_notes.remove(self)
        self.destroy()
        self.autosave()

    # --- Converts Note's data to dict which can be later saved to json file ---
    def to_dict(self):
        return {
            "x": self.winfo_x(),
            "y": self.winfo_y(),
            "title": self.note_title.get(),
            "text": self.note_textbox.get("1.0", "end-1c"),
            "width": self.winfo_width(),
            "height": self.winfo_height()
        }