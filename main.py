version = "1.0.0"
import logging
from os import error
from types import NoneType
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
main_layout = [[sg.Frame("Connections Settings", [[sg.Text(text="Server IP:", size=(20, None), auto_size_text=True, justification="center"), sg.InputText(default_text="192.168.1.1", size=(25, None), justification="center", tooltip="Server IP", key="-SRVIP-"), sg.Text(text="Port:", auto_size_text=True, justification="center"), sg.InputText(default_text="25575", size=(25, None), justification="center", tooltip="RCON Port", key="-SRV-PRT-"), sg.Text(text="Password:", auto_size_text=True, justification="center"), sg.InputText(password_char="*", justification="center", tooltip="Rcon Password", key="-SRV-PASS-"), sg.Button(button_text="Connect", key="-BTN-CONNCT-"), sg.Button(button_text="Disconnect", key="-BTN-D-CONNCT-")]], element_justification="center")], [sg.Column([[sg.Output(size=(None, 15))]]), sg.Column([[sg.Text(text="Command"), sg.InputText(size=(25, None), key="-CMD-INPT-"), sg.Button(button_text="Send", key="-BTN-SBMT-CMD-")], [sg.Text(text="Chat", size=(8, None), justification="center"), sg.InputText(size=(24, None), key="-CHAT-INPUT-"), sg.Button(button_text="Send", key="-BTN-SBMT-MSG-")]]), sg.Column([[sg.Frame("Quick Commands", [[sg.Button(button_text="Players", key="-BTN-PLAYERS-"), sg.Button(button_text="Admins", key="-BTN-ADMINS-"), sg.Button(button_text="Server Save", key="-BTN-SERVER-SAVE-"), sg.Button(button_text="Stop Server", key="-STOP-SERVER-")], [sg.Button(button_text="Kick Player", key="-BTN-KICK-"), sg.Button(button_text="Ban Player", key="-BTN-BAN-"), sg.Button(button_text="Unban Player", key="-BTN-UNBAN-")], [sg.Text(text="Player: "), sg.InputText(size=(20, None), tooltip="Player Name", key="-PLAYER-ID-")]], element_justification="Center")]])]]
## TODO
# kick_layout 
# ban layout
# admin layout
# whitelist layout
# server status layout
sg_main_window = sg.Window("Factorio RCON Client", main_layout)


while True:
    event, values = sg_main_window.read()
    # print(str(event) + ":" + str(values))
    if event == "-BTN-CONNCT-":
        try:
            IP_ADDR = str(values["-SRVIP-"])
            SRV_PRT = int(values["-SRV-PRT-"])
            SRV_PSWD = str(values["-SRV-PASS-"])
            rcon = rconcreate(IP_ADDR,SRV_PRT,SRV_PSWD)
            rcon.timeout = 30
            rcon.connect()
            ftime = rcon.send_command("/time")
            fseed = rcon.send_command("/seed")
            fplayer_count = rcon.send_command("/players c")
            fevo = rcon.send_command("/evolution")
            print(" [INFO] " + "Successfully connected to " + str(rcon.ip_address) + " using port " + str(rcon.port))
            print(" [SERVER INFO] \n"  + str(fplayer_count) + "\n" + "Game Time: " + str(ftime) + "\n" + "Evolution: " + str(fevo) + "\n" + "Server seed: " + fseed)
            sg_main_window.refresh()
        except(RCONConnectError):
            print("There was an error connecitng to the RCON server.\n Please ensure that you have entered you settings correctly. If all of the settings are entered correctly please try:\n - Making sure your Factorio server is online\n - RCON is enabled on your server\n - Your computer has a working internet connection\nIf you have validated all this please submit a bug report at\n :https://github.com/ComputerComa/Facotorio-RCON-GUI/issues ")
        except(RCONNetworkError):
            print("There was an error communicating with the RCON server.\n Please ensure that you have entered you settings correctly. If all of the settings are entered correctly please try:\n - Making sure your Factorio server is online\n - RCON is enabled on your server\n - Your computer has a working internet connection\nIf you have validated all this please submit a bug report at\n :https://github.com/ComputerComa/Facotorio-RCON-GUI/issues ")
        except:
            logging.exception("message")

    if event == "-BTN-SBMT-CMD-":
        try:
            if len(values["-CMD-INPT-"]) > 0:
                print("Attempting to send command: " + str(values["-CMD-INPT-"]))
                response = rcon.send_command(str(values["-CMD-INPT-"]))
                print(" [SERVER] " + str(response))
            else:
                print(" [ERROR] Please include a command to run!")
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
    if event == "-BTN-ADMINS-":
        try:
            response = rcon.send_command("/admins")
            print(str(response))
        except(NameError):
            print("Unable to handle this command.Please verify that there is an open connection to RCON and that your server is running.")
        except:
            logging.exception("Error")
    if event == "-BTN-D-CONNCT-":
        try:
            rcon.close()
            rcon = None
            print(" [INFO] Successfuly closed the RCON connection.")
        except(AttributeError):
            print(" [INFO] There is no connection to close.")
        except(NameError):
            print(" [INFO] There is no connection to close.")
        except:
            logging.exception("Error")
    if event == "-STOP-SERVER-":
        try:
            print(" [INFO] Attempting to stop the Factorio server")
            response = rcon.send_command("/quit")
        except:
            logging.exception("Error:")
    if event == "-BTN-SBMT-MSG-":
        try:
            response = rcon.send_command("/shout " + str(values["-CHAT-INPUT-"]))
            print("Chat sent: " + str(values["-CHAT-INPUT-"]))
        except:
            logging.exception("Message: ")
    if event == "-BTN-KICK-":
        try:
            if len(values["-PLAYER-ID-"]) > 0:   
                response = rcon.send_command("/kick " + str(values["-PLAYER-ID-"]))
                if response == None:
                   print("Sucessfully kicked " + str(values["-PLAYER-ID-"])) 
                else:
                    print(str(response))
            else:
                print("Please provide a player to kick.")
        except(NameError):
            print("Unable to handle this command.Please verify that there is an open connection to RCON and that your server is running.")
        except:
            logging.exception("Error")
    if event == "-BTN-BAN-":
        try:
            if len(values["-PLAYER-ID-"]) > 0:   
                response = rcon.send_command("/ban " + str(values["-PLAYER-ID-"]))
                if response == None:
                   print("Sucessfully banned " + str(values["-PLAYER-ID-"])) 
                else:
                    print(str(response))
            else:
                print("Please provide a player to ban.")
        except(NameError):
            print("Unable to handle this command.Please verify that there is an open connection to RCON and that your server is running.")
        except:
            logging.exception("Error")
    if event == "-BTN-UNBAN-":
        try:
            if len(values["-PLAYER-ID-"]) > 0:   
                response = rcon.send_command("/unban " + str(values["-PLAYER-ID-"]))
                if response == None:
                   print("Sucessfully unbanned " + str(values["-PLAYER-ID-"])) 
                else:
                    print(str(response))
            else:
                print("Please provide a player to unban.")
        except(NameError):
            print("Unable to handle this command.Please verify that there is an open connection to RCON and that your server is running.")
        except:
            logging.exception("Error")
        
    

    if event == sg.WIN_CLOSED:
        try:
            rcon.close()
        except:
            break
        break

