import string
import random
import PySimpleGUI as sg
import pyperclip


def generate_password(words, count):
    # Combine the words provided by the user
    combined_words = ''.join(words)

    # Generate a random string of characters for additional complexity
    random_chars = ''.join(random.choices(
        string.ascii_letters + string.digits + string.punctuation, k=count))

    # Combine the words and random characters to create the password
    password = combined_words + random_chars
    return password


sg.theme('DarkBlue6')
sg.set_options(font='verdana 15')
layout = [
    [sg.Text('Enter some words:'), sg.Push(),
     sg.Input(size=15, key="-WORDS-")],
    [sg.Text('Length of Password :'), sg.Push(),
     sg.Input(size=15, key="-SIZE-")],
    [sg.Button('Generate', button_color="Green"),
     sg.Button("Copy"), sg.Button('Cancel')],
    [sg.Text('Generated Password:', visible=False, key="-PASSWORD_TEXT-"), sg.Push(),
     sg.Multiline(size=15, key="-PASSWORD-", visible=False, no_scrollbar=True)],
]


# Create the window
window = sg.Window("Password Generator", layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Cancel":
        break
    if event == "Generate":
        try:
            count = int(values['-SIZE-'])
            user_words = values["-WORDS-"].split()
            window["-PASSWORD_TEXT-"].update(
                "Generated Password: ", visible=True)
            password = generate_password(user_words, count)
            window["-PASSWORD_TEXT-"].update(visible=True)
            window["-PASSWORD-"].update(password, visible=True)

        except ValueError:
            window["-PASSWORD_TEXT-"].update("Enter Valid Value", visible=True)
            window["-PASSWORD-"].update(visible=False)
    if event == "Copy":
        password = values["-PASSWORD-"]
        if password != "":
            pyperclip.copy(password)
            sg.popup_no_buttons('Password copied successfully!', text_color='white',
                                auto_close=True, auto_close_duration=2, background_color='green', no_titlebar = True )

# Close the window
window.close()
