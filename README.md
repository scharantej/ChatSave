Here's the detailed design for creating a chatbot using Python Flask, featuring login with Firebase, chat history saving, and the ability to create new chats:

### HTML Files
- `index.html`:
    - This serves as the main HTML page for the chatbot.
    - It should include the necessary HTML elements for the chatbot interface, such as a chat message input field, a chat message display area, and buttons for login, creating new conversations, and opening existing ones.
    - It should also include the JavaScript code for handling the chat functionality, including sending and receiving messages, and performing login actions with Firebase.
- `preferences.html`:
    - This HTML page is used for managing user preferences, such as default chat settings and notification preferences.
    - It should include the necessary form elements for updating the user's preferences.

### Routes
- `/login`:
    - This route handles the login process with Firebase.
    - Upon successful login, it should set the necessary session variables to identify the logged-in user.
- `/logout`:
    - This route handles the logout process and should clear the session variables set during login.
- `/create-chat`:
    - This route handles the creation of a new chat.
    - It should create a new chat entry in the database and return the chat ID.
- `/get-chats`:
    - This route retrieves a list of all the chats created by the logged-in user.
- `/get-chat`:
    - This route retrieves the chat history for a specific chat ID.
- `/send-message`:
    - This route handles sending a new message to a specific chat.
    - It should save the message to the database and notify connected clients of the new message.