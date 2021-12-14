[[sg.Frame("Connections Settings", [[sg.Text(text="Server IP:", size=(20, None), auto_size_text=True, justification="center"), sg.InputText(default_text="192.168.1.1", size=(25, None), justification="center", tooltip="Server IP", key="-SRVIP-"), sg.Text(text="Port:", auto_size_text=True, justification="center"), sg.InputText(default_text="25575", size=(25, None), justification="center", tooltip="RCON Port", key="-SRV-PRT-"), sg.Text(text="Password:", auto_size_text=True, justification="center"), sg.InputText(password_char="*", justification="center", tooltip="Rcon Password", key="-SRV-PASS-"), sg.Button(button_text="Connect", key="-BTN-CONNCT-"), sg.Button(button_text="Disconnect", key="-BTN-D-CONNCT-")]], element_justification="center")], [sg.Column([[sg.Output(size=(None, 15))]]), sg.Column([[sg.Text(text="Command"), sg.InputText(size=(25, None), key="-CMD-INPT-"), sg.Button(button_text="Send", key="-BTN-SBMT-CMD-")], [sg.Text(text="Chat", size=(8, None), justification="center"), sg.InputText(size=(24, None)), sg.Button(button_text="Send", key="-BTN-SBMT-MSG-")]]), sg.Column([[sg.Frame("Quick Commands", [[sg.Button(button_text="Players", key="-BTN-PLAYERS-"), sg.Button(button_text="Admins", key="-BTN-ADMINS-"), sg.Button(button_text="Server Save", key="-BTN-SERVER-SAVE")], [sg.Button(button_text="Kick Player", disabled=True, key="-BTN-KICK-"), sg.Button(button_text="Ban Player", disabled=True, key="-BTN-BAN-"), sg.Button(button_text="Stop Server", key="-STOP-SERVER-")]], element_justification="Center")]])]]