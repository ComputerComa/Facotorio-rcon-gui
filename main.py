import logging
from os import error
from typing import ValuesView
from PySimpleGUI.PySimpleGUI import ConvertArgsToSingleString, Debug, Print
from construct import debug
import factorio_rcon
import PySimpleGUI as sg
def rconcreate(IP_ADDR: str, SRV_PORT: int, SRV_Password: str) -> factorio_rcon.RCONClient:
    "Create the RCON connection"
    client = factorio_rcon.RCONClient(IP_ADDR, SRV_PORT, SRV_Password)
    return client
sg.theme('Dark')
main_layout = [[sg.Text(text="Server IP:", auto_size_text=True), sg.InputText(default_text="192.168.1.1", tooltip="Server IP", key="-SRVIP-"), sg.Text(text="Port:", auto_size_text=True), sg.InputText(default_text="25575", tooltip="RCON port", key="-SRV-PRT-"), sg.Text(text="Password:", auto_size_text=True), sg.InputText(password_char="*", tooltip="Rcon Password", key="-SRV-PASS-"), sg.Button(button_text="Connect", key="-BTN-CONNCT-")], [sg.StatusBar("Ready", key="-APP-STAT-")], [sg.Column([[sg.Output(size=(150, 15), echo_stdout_stderr=True, key="CMD-OUT-")]]), sg.Column([[sg.Text(text="Command"), sg.InputText(key="-CMD-INPT-"), sg.Button(button_text="Submit Command", auto_size_button=True, key="-BTN-SBMT-CMD-")]])]]
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
        except:
            logging.exception("message")

    if event == "-BTN-SBMT-CMD-":
        try:
            print("Attempting to send command: " + str(values["-CMD-INPT-"])) 
            response = rcon.send_command(str(values["-CMD-INPT-"]))
            print(" [SERVER] " + str(response))
        except:
            logging.exception("Error Message")
    if event == sg.WIN_CLOSED:
        break

