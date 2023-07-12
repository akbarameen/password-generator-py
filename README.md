# password-generator-py
PROJECT WORKFLOW
User Interface Setup:
Import the necessary modules and libraries, including PySimpleGUI.
Define the layout of the graphical user interface (GUI) using PySimpleGUI elements such as input fields, buttons, and text areas.
Create a window object using PySimpleGUI and set its layout to the defined GUI layout.
Initialize any necessary variables.

Event Loop:
Enter an event loop that listens for user interactions with the GUI.
Handle different events such as button clicks or window closures.
Implement event handlers to respond to user actions appropriately.

User Input:
Retrieve user input from the GUI elements.
Obtain the words or phrases provided by the user and the desired length of the password.

![outputMain](https://github.com/akbarameen/password-generator-py/assets/93811674/b4c9b3ec-0e8f-426b-9834-e24e96d4a5dd)

Password Generation:
Implement two password generation functions: generate_password1 and generate_password2.
generate_password1 takes the user's words, counts the length, and generates a password with shuffled words and additional random characters for complexity.
generate_password2 takes the user's words, shuffles them, counts the length, and generates a password with shuffled words and additional random characters for complexity.

Display Password:
Update the GUI to display the generated passwords.
Show the passwords to the user in separate text areas.
Allow the user to copy each password to the clipboard if needed.

![outputGeneratedPassword](https://github.com/akbarameen/password-generator-py/assets/93811674/59df1177-1bca-4803-8e49-80b7cd2c3dd4)

Error Handling:
Implement error handling mechanisms to handle any potential issues during the password generation process.
Display informative error messages to the user if input validation fails or other errors occur.

![validationForEmptyInput](https://github.com/akbarameen/password-generator-py/assets/93811674/e9ea6b32-d8ed-4d33-88d5-91b7bb7dc9cf)

Copying Password:
Implement the functionality to copy the generated passwords to the clipboard.
Handle user interactions with the "Copy" buttons.
Copy the respective passwords to the clipboard using the pyperclip module.
Provide feedback to the user indicating successful copying of the password.

![copiedpass2](https://github.com/akbarameen/password-generator-py/assets/93811674/cf433c43-321b-4cca-8bd2-8c3cadf533e2)

![copiedpass](https://github.com/akbarameen/password-generator-py/assets/93811674/a61b965f-06b5-4d58-a773-94e551c60f95)

Documentation and Testing:
Document the project, including the overall functionality, code structure, and usage instructions.
Include any dependencies and installation steps in the documentation.
Perform thorough testing to ensure the password generator works as expected in different scenarios.
