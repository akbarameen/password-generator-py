import string
import random
import PySimpleGUI as sg
import pyperclip


def generate_password1(words, count):
    # Combine the words provided by the user
    
    combined_words = ''.join(words)
    word_length= len(str(combined_words))
    # Generate a random string of characters for additional complexity
    random_chars = ''.join(random.choices(
            string.ascii_letters + string.digits + string.punctuation, k=count-word_length))
    
    if  word_length> count:
         # make list before shuffling
        List= list(combined_words)
        random.shuffle(List)
        mixed_combineed_words = ''.join(List)
        password = mixed_combineed_words + random_chars
        return password
    else:
        
        # Combine the words and random characters to create the password
        password = combined_words + random_chars
        return password
    
def generate_password2(words, count):
    # Combine the words provided by the user
    combined_words = ''.join(words)

    # make list before shuffling
    List= list(combined_words)
    random.shuffle(List)
    mixed_combineed_words = ''.join(List)

    # find the length of the user input words
    word_length= len(str(mixed_combineed_words))
    # Generate a random string of characters for additional complexity
    random_chars = ''.join(random.choices(
        string.ascii_letters + string.digits + string.punctuation, k=count-word_length))

    # Combine the words and random characters to create the password
    password = mixed_combineed_words + random_chars

    return password


# chaning the theme of the window
sg.theme('DarkBlue6')

# changing the size and font
sg.set_options(font='verdana 15')

# GUI interface window design
layout = [
    [sg.Text('Enter some words:'), sg.Push(),
     sg.Input(size=15, key="-WORDS-")],
    [sg.Text('Length of Password :'), sg.Push(),
     sg.Input(size=15, key="-SIZE-")],
    [sg.Button('Generate', button_color="Green"),  sg.Push(), sg.Button("Copy 1"), sg.Push(), sg.Button("Copy 2"), sg.Push(), sg.Button('Cancel')],
    [sg.Text('Generated Password 1:', visible=False, key="-PASSWORD_TEXT_1-"), sg.Push(),
     sg.Multiline(size=15, key="-PASSWORD_1-", visible=False, no_scrollbar=True)],
    [sg.Text('Generated Password 2:', visible=False, key="-PASSWORD_TEXT_2-"), sg.Push(),
    sg.Multiline(size=15, key="-PASSWORD_2-", visible=False, no_scrollbar=True)],

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
            window["-PASSWORD_TEXT_1-"].update(visible=True)

            # For generated password 1
            password1 = generate_password1(user_words, count)
            window["-PASSWORD_TEXT_1-"].update(visible=True)
            window["-PASSWORD_1-"].update(password1, visible=True)

            # For generated password 2
            password2 = generate_password2(user_words, count)
            window["-PASSWORD_TEXT_2-"].update(visible=True)
            window["-PASSWORD_2-"].update(password2, visible=True) 

        except ValueError:
            # Clearning Fields
            window["-PASSWORD_TEXT_1-"].update(visible=False)
            window["-PASSWORD_TEXT_2-"].update(visible=False)
            window["-PASSWORD_1-"].update("", visible=False)
            window["-PASSWORD_2-"].update("", visible=False)
            # error popup message
            sg.popup_no_buttons('Enter Valid Values', text_color='white',
                                auto_close=True, auto_close_duration=2, background_color='Red', no_titlebar = True )
          

    # copying password  
    if event == "Copy 1":
        password1 = values["-PASSWORD_1-"]
        if password1 != "":
            pyperclip.copy(password1)
            sg.popup_no_buttons('Password 1 copied successfully!', text_color='white',
                                auto_close=True, auto_close_duration=2, background_color='green', no_titlebar = True )
    if event == "Copy 2":
        password1 = values["-PASSWORD_2-"]
        if password1 != "":
            pyperclip.copy(password1)
            sg.popup_no_buttons('Password 2 copied successfully!', text_color='white',
                                auto_close=True, auto_close_duration=2, background_color='green', no_titlebar = True )

# Close the window
window.close()
