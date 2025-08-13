# --- Function that imports all files from definitons folder ---
def import_files(self):
    
    # --- Importing all files from functions ---
    modules_to_import = {
    "functions.start_screen.start_screen": ["start_screen"],

    "functions.create_new_project.create_new_project_screen": ["create_new_project_screen"],

    "functions.load_project.load_project_screen": ["load_project_screen"],

    "functions.project_manager.project_manager_screen": ["project_manager_screen"],
    
    "functions.project_manager.tools.to_do_list_tool": ["to_do_list_tool"],
    "functions.project_manager.tools.calendar_tool": ["calendar_tool"],
    "functions.project_manager.tools.mindmap_tool": ["mindmap_tool"],
    "functions.project_manager.tools.check_list_tool": ["check_list_tool"],
    "functions.project_manager.tools.sticky_notes_tool": ["sticky_notes_tool"],
    "functions.project_manager.tools.text_note_tool": ["text_note_tool"],
    "functions.project_manager.tools.delete_project_tool": ["delete_project_tool"],
    "functions.project_manager.tools.unbind_key_binds_tool": ["unbind_key_binds_tool"],
    
    "functions.settings.settings_screen": ["settings_screen"],
    
    "functions.settings.tools.appearance_tool": ["appearance_screen"],
    "functions.settings.tools.themes_tool": ["themes_screen"],
    "functions.settings.tools.key_binds_tool": ["key_binds_screen"],
    "functions.settings.tools.toggle_tools_tool":["toggle_tools_screen"],
    "functions.settings.tools.settings_change": ["settings_change"]
    }
    
    # --- Adding all imported functions as self ---
    for module_path, functions in modules_to_import.items(): #Developer Note: .items() retruns (key,value)
        module = __import__(module_path, fromlist=functions)
        for function_name in functions: #Developer Note: The reason behind using lists instead of one string above is to future proof the code in case I will need to import multiple functions from one file
            setattr(self, function_name, getattr(module, function_name))