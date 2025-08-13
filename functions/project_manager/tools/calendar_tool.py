import customtkinter as ctk
import calendar
from datetime import datetime
import json

# --- Calendar Tool ---
def calendar_tool(self):

    # --- Loading calendar data ---
    with open(f"projects/{self.current_project}/calendar.json", "r", encoding="utf-8") as f:
        self.calendar_data = json.load(f)

    # --- Used as a middle ground between days entries and json file -> So saving into json is not triggered after every letter change ---
    self.save_after_ids = {}

    # --- Main Frame ---
    self.main_frame.grid_forget()
    self.main_frame = ctk.CTkFrame(
        master=self.root,
        corner_radius=0,
        border_width=5,
        border_color="#1f6aa5"
    )
    self.main_frame.grid(row=1, column=1, sticky="nsew")
    
    # --- Configuring Main Panel for calendar need ---
    self.main_frame.grid_columnconfigure(0, weight=1)
    self.main_frame.grid_rowconfigure(1, weight=1)  # calendar area expands

    # --- Year/Month/Day tracking ---
    self.current_year = getattr(self, "current_year", datetime.now().year)
    self.current_month = getattr(self, "current_month", datetime.now().month)
    self.current_day = getattr(self, "current_day", datetime.now().day)

    # --- Top Panel ---
    top_panel = ctk.CTkFrame(master=self.main_frame)
    top_panel.grid(row=0, column=0, pady=20,padx=20, sticky="we")
    top_panel.grid_columnconfigure((0, 2), weight=1)
    top_panel.grid_columnconfigure(1, weight=2)

    # --- Previous Month button ---
    previous_month_button = ctk.CTkButton(
        master=top_panel,
        text="<", 
        width=50,
        font=("Arial", 20,"bold"),
        command=lambda: change_month(self, -1)
    )
    
    previous_month_button.grid(row=0, column=0, sticky="w", padx=10)

    # --- Current Month label ---
    self.month_label = ctk.CTkLabel(
        master=top_panel,
        text="",
        font=("Arial", 40, "bold")
    )

    self.month_label.grid(row=0, column=1)

    # --- Next Month button ---
    next_month_button = ctk.CTkButton(
        master=top_panel,
        text=">",
        width=50,
        font=("Arial", 20,"bold"),
        command=lambda: change_month(self, 1)
    )

    next_month_button .grid(row=0, column=2, sticky="e", padx=10)

    # --- Calendar Frame ---
    self.calendar_frame = ctk.CTkFrame(master=self.main_frame)
    self.calendar_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

    # --- Columns expand evenly to fill the whole Main Frame ---
    for column in range(7):
        self.calendar_frame.grid_columnconfigure(column, weight=1)

    # --- First row (week day lables) doesn't have to expand
    self.calendar_frame.grid_rowconfigure(0, weight=0)
    
    # --- rows expand evenly to fill the whole Main Frame ---
    for row in range(1, 7):
        self.calendar_frame.grid_rowconfigure(row, weight=1)

    self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # --- Render upon starting the calendar tool ---
    render_calendar(self)

# --- Function that renders the calendar ---
def render_calendar(self):
    # --- Clears whole calendar frame ---
    for window in self.calendar_frame.winfo_children():
        window.destroy()

    # --- Configures the calendar title with selected month and year ---
    self.month_label.configure(text=f"{calendar.month_name[self.current_month]} {self.current_year}")

    # --- Renders week day labels ---
    for index, day_name in enumerate(self.days): #Developer Note: Enumerate will turn the list into a dictionary in this format {0:"Mon",...}
        day_label = ctk.CTkLabel(
            master=self.calendar_frame, 
            text=day_name, font=("Arial", 20, "bold")
        )
        day_label.grid(row=0, column=index, padx=4, pady=(4, 8))

    # --- Gets month weeks (list of weeks -> each week is 7 integers) ---
    cal = calendar.Calendar(firstweekday=0)
    month_weeks = cal.monthdayscalendar(self.current_year, self.current_month)

    # --- Ensures row weights for the exact number of week rows (keeps layout consistent) ---
    week_count = len(month_weeks)
    for row in range(1, 1 + week_count):
        self.calendar_frame.grid_rowconfigure(row, weight=1)

    for row in range(1 + week_count, 7):
        self.calendar_frame.grid_rowconfigure(row, weight=0)  # unused rows don't take space

    # --- Creates Day Cells
    for row_idxex, week in enumerate(month_weeks, start=1):
        for col_idx, day in enumerate(week):

            # --- Create an empty cell for day==0 so grid stays consistent ---
            cell_container = ctk.CTkFrame(self.calendar_frame, corner_radius=6, border_width=1)
            cell_container.grid(row=row_idxex, column=col_idx, sticky="nsew", padx=3, pady=3)

            # --- Inner grid: row 0 is the day number label, row 1 is the expanding textbox ---
            cell_container.grid_rowconfigure(0, weight=0)
            cell_container.grid_rowconfigure(1, weight=1)
            cell_container.grid_columnconfigure(0, weight=1)

            if day == 0:

                # --- Blank (outside the month) ---
                continue

            # --- Day Number Label ---
            day_number_label = ctk.CTkLabel(
                master=cell_container,
                text=str(day),
                text_color = "yellow" if (str(self.current_day) == str(day) and str(self.current_month) == str(datetime.now().month)) else None,
                anchor="nw",
                font=("Arial", 20, "bold")
            )
            day_number_label.grid(row=0, column=0, sticky="nw", padx=6, pady=(4, 2))

            # --- Expanding Text Box ---
            txt_box = ctk.CTkTextbox(
                master=cell_container,
                font=("Arial", 20, "bold"),
                wrap="word"
            )

            txt_box.grid(row=1, column=0, sticky="nsew", padx=(6, 2), pady=(0, 6))

            # --- Sets label to current month and year
            date_key = f"{self.current_year}-{self.current_month:02d}-{day:02d}"

            if date_key in self.calendar_data:
                txt_box.insert("1.0", self.calendar_data[date_key])

            # --- Binds Auto Save Logic
            txt_box.bind("<KeyRelease>", make_on_change(self, date_key, txt_box))
                  
# --- Function used to save calendar data ---    
def save_calendar_data(self):
        with open(f"projects/{self.current_project}/calendar.json", "w", encoding="utf-8") as f:
            json.dump(self.calendar_data, f, indent=4)

# --- Function used to change the month in the calendar ---            
def change_month(self, offset):
        self.current_month += offset
        if self.current_month < 1:
            self.current_month = 12
            self.current_year -= 1
        elif self.current_month > 12:
            self.current_month = 1
            self.current_year += 1
        render_calendar(self)
        
# --- Save Changes -> update calendar_data then saves them to json ---
def make_on_change(self, date_key, textbox):
    def on_change(event=None):
        
        # -- Updates in-memory calendar data
        self.calendar_data[date_key] = textbox.get("1.0", "end-1c")

        # --- Cancel previous save if scheduled ---
        if date_key in self.save_after_ids:
            try:
                self.main_frame.after_cancel(self.save_after_ids[date_key])
            except Exception:
                pass

        # --- Schedule save after 1 second ---
        self.save_after_ids[date_key] = self.main_frame.after(
            1000, lambda: save_calendar_data(self)
        )
    return on_change              