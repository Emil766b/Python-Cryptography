import PySimpleGUI as sg
from cryptography.fernet import Fernet

#Definere layout
layout = [
    [
        #Input besked tekst
        [sg.Text("Input Besked")],
        #Input felt og key til input felt
        ([[sg.InputText('', size=(30,1), key='input_message')]]),
        #Tilføj knap
        [sg.Button("Tilføj")],
        #Krypter knap
        [sg.Button("Krypter")],
        #Dekrypter knap
        [sg.Button("Dekrypter")],
    ],
    [
        #Original besked tekst
        [sg.Text("Original Besked")],
        #Felt der indeholder listbox key og viser den originale besked
        sg.Multiline(enable_events=True, size=(30,5), key='listbox')
    ],
    [
        #Ktypteret besked tekst
        [sg.Text("Krypteret Besked")],
        #Felt der indeholder encrypt key og viser den krypteret besked
        sg.Multiline(enable_events=True, size=(30,5), key='encrypt')
    ],
    [
        #Dekrypteret besked tekst
        [sg.Text("Dekrypteret Besked")],
        #Felt der indeholder decrypt key og viser den dekrypteret besked
        sg.Multiline(enable_events=True, size=(30,5), key='decrypt')
    ]
]

#Definere vinduet der skal laves og laver det ud fra layout
window = sg.Window("crypto", layout)

#Generere en krypterings nøgle med fernet i cryptography komponentet
key = Fernet.generate_key()

#Lager den genereret nøgle
fernet = Fernet(key)

#Kører loopet hvis sandt
while True:
    #Læs hvad vinduet er i gang med
    event, values = window.read()
    #Hvis vinduet bliver lukket slukket programmet
    if event == sg.WIN_CLOSED:
        break
    #Else if i python og bliver brugt som en switch 
    #Else if event tilføj
    elif event == 'Tilføj':
        #Definere message og input til message
        message = values['input_message']
        #Opdatere listbox key med input til message
        window['listbox'].update(message) 
    #Else if event krypter    
    elif event == 'Krypter':
        #Kryptere message med nøglen 
        encMessage = fernet.encrypt(message.encode())
        #Opdatere encrypt key med den krypteret besked
        window['encrypt'].update(encMessage) 
    #Else if event Dekrypter
    elif event == 'Dekrypter':
        #Dekryptere message med nøglen
        decMessage = fernet.decrypt(encMessage).decode()
        #Opdatere decrypt key med den dekrypteret besked
        window['decrypt'].update(decMessage)  
#Lukker vinduet
window.close()

#for at køre koden installer 
#pip install cryptography
#pip install PySimpleGUI