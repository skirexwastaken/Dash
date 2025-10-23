import customtkinter as ctk
import shutil

# --- Deleting Project Menu ---
def delete_project_tool(self):
    self.delete_project_gui = ctk.CTkFrame(master=self.root)
    self.delete_project_gui.pack(fill="both", expand=True)
    self.delete_project_gui.place(relx=0.5, rely=0.5, anchor="center")
        
    # --- Deleting Project label ---    
    delete_project_label = ctk.CTkLabel(
        master=self.delete_project_gui ,
        text="Are you sure?",
        font=("Arial", 90, "bold")
    )
    delete_project_label.pack(pady=(40,20),padx=40)
    
    # --- Delete Project button ---
    delete_button = ctk.CTkButton(
        master=self.delete_project_gui ,
        text="Delete",
        font=("Arial", 40, "bold"),
        command=lambda: (self.delete_project_gui.pack_forget(), self.delete_project_gui.place_forget(),shutil.rmtree(f"projects/{self.current_project}"),self.unbind_key_binds_tool(self), self.start_screen(self))
    )
    delete_button.pack(pady=20)
     
    # --- Button that brings user back to Project Manager ---    
    back_button = ctk.CTkButton(
        master=self.delete_project_gui ,
        text="Back",
        font=("Arial", 40, "bold"),
        command=lambda: (self.delete_project_gui.pack_forget(), self.delete_project_gui.place_forget(), self.project_manager_screen(self))
    )
    back_button.pack(pady=(20,40))