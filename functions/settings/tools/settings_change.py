import json

# --- Function that changes app settings ---
def settings_change(type,arg):
    with open("app_data.json","r") as file:
        app_data=json.load(file)
    app_data[type]=arg
    with open("app_data.json","w") as file:
        json.dump(app_data, file,indent=4)