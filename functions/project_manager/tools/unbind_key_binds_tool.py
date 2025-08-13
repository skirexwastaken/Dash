# --- Functions that removes all key binds used in Project Manager upon leaving it ---               
def unbind_key_binds_tool(self):
    for key_bind in self.app_data["key_binds"].values():
        self.root.unbind(key_bind)                                 