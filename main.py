version = "1.0.0"
import logging
from os import error
from typing import ValuesView
from PySimpleGUI.PySimpleGUI import ConvertArgsToSingleString, Debug, Print
from construct import debug
import factorio_rcon
import PySimpleGUI as sg
from factorio_rcon.factorio_rcon import RCONConnectError, RCONNetworkError
def rconcreate(IP_ADDR: str, SRV_PORT: int, SRV_Password: str) -> factorio_rcon.RCONClient:
    "Create the RCON connection"
    client = factorio_rcon.RCONClient(IP_ADDR, SRV_PORT, SRV_Password)
    return client
sg.theme('Dark')
main_layout = [[sg.Frame("Connections Settings", [[sg.Text(text="Server IP:", size=(20, None), auto_size_text=True, justification="center"), sg.InputText(default_text="192.168.1.1", size=(25, None), justification="center", tooltip="Server IP", key="-SRVIP-"), sg.Text(text="Port:", auto_size_text=True, justification="center"), sg.InputText(default_text="25575", size=(25, None), justification="center", tooltip="RCON Port", key="-SRV-PRT-"), sg.Text(text="Password:", auto_size_text=True, justification="center"), sg.InputText(password_char="*", justification="center", tooltip="Rcon Password", key="-SRV-PASS-"), sg.Button(button_text="Connect", key="-BTN-CONNCT-"), sg.Button(button_text="Disconnect", key="-BTN-D-CONNCT-")]], element_justification="center")], [sg.Column([[sg.Output(size=(None, 15))]]), sg.Column([[sg.Text(text="Command"), sg.InputText(size=(25, None), key="-CMD-INPT-"), sg.Button(button_text="Send", key="-BTN-SBMT-CMD-")], [sg.Text(text="Chat", size=(8, None), justification="center"), sg.InputText(size=(24, None)), sg.Button(button_text="Send", key="-BTN-SBMT-MSG-")]]), sg.Column([[sg.Frame("Quick Commands", [[sg.Button(button_text="Players", key="-BTN-PLAYERS-"), sg.Button(button_text="Admins", key="-BTN-ADMINS-"), sg.Button(button_text="Server Save", key="-BTN-SERVER-SAVE-")], [sg.Button(button_text="Kick Player", disabled=True, key="-BTN-KICK-"), sg.Button(button_text="Ban Player", disabled=True, key="-BTN-BAN-"), sg.Button(button_text="Stop Server", key="-STOP-SERVER")]], element_justification="Center")]])]]

window = sg.Window("Factorio RCON Client", main_layout)


while True:
    event, values = window.read()
    # print(str(event) + ":" + str(values))
    if event == "-BTN-CONNCT-":
        try:
            IP_ADDR = str(values["-SRVIP-"])
            SRV_PRT = int(values["-SRV-PRT-"])
            SRV_PSWD = str(values["-SRV-PASS-"])
            rcon = rconcreate(IP_ADDR,SRV_PRT,SRV_PSWD)
            rcon.connect()
            print("INFO | " + "Successfully connected to " + str(rcon.ip_address) + " using port " + str(rcon.port))
            window.refresh()
        except(RCONConnectError):
            print("There was an error connecitng to the RCON server.\n Please ensure that you have entered you settings correctly. If all of the settings are entered correctly please try:\n - Making sure your Factorio server is online\n - RCON is enabled on your server\n - Your computer has a working internet connection\nIf you have validated all this please submit a bug report at\n :https://github.com/ComputerComa/Facotorio-RCON-GUI/issues ")
        except(RCONNetworkError):
            print("There was an error communicating with the RCON server.\n Please ensure that you have entered you settings correctly. If all of the settings are entered correctly please try:\n - Making sure your Factorio server is online\n - RCON is enabled on your server\n - Your computer has a working internet connection\nIf you have validated all this please submit a bug report at\n :https://github.com/ComputerComa/Facotorio-RCON-GUI/issues ")
        except:
            logging.exception("message")

    if event == "-BTN-SBMT-CMD-":
        try:
            print("Attempting to send command: " + str(values["-CMD-INPT-"])) 
            response = rcon.send_command(str(values["-CMD-INPT-"]))
            print(" [SERVER] " + str(response))
        except(NameError):
            print("Unable to handle this command.Please verify that there is an open connection to RCON and that your server is running.")
        except:
            logging.exception("Error")
    if event == "-BTN-SERVER-SAVE-":
        try:
            print("Attempting to save the game")
            response = rcon.send_command("/server-save")
            print(" [SERVER] " + str(response))
        except(NameError):
            print("Unable to handle this command.Please verify that there is an open connection to RCON and that your server is running.")
        except:
            logging.exception("Error")
        

    if event == "-BTN-PLAYERS-":
        try:
            response = rcon.send_command("/players")
            print(str(response))
        except(NameError):
            print("Unable to handle this command.Please verify that there is an open connection to RCON and that your server is running.")
        except:
            logging.exception("Error")
    if event == "-BTN-D-CONNCT-":
        try:
            rcon.close()
        except:
            logging.exception("Error")
    

    if event == sg.WIN_CLOSED:
        break

