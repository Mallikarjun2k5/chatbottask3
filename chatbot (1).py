# Basic Chatbot App using Python

def chatbot():
    print("ChatBot: Hello! I'm ChatBot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ['hi', 'hello']:
            print("ChatBot: Hello there! How can I help you?")
        elif "your name" in user_input:
            print("ChatBot: I'm a simple chatbot created with Python.")
        elif "how are you" in user_input:
            print("ChatBot: I'm doing great! Thanks for asking.")
        elif "help" in user_input:
            print("ChatBot: Sure! You can ask me basic questions like time, date, or just chat.")
        elif "time" in user_input:
            from datetime import datetime
            print("ChatBot: The current time is", datetime.now().strftime("%H:%M:%S"))
        elif "date" in user_input:
            from datetime import date
            print("ChatBot: Today's date is", date.today().strftime("%B %d, %Y"))
        elif user_input == "bye":
            print("ChatBot: Goodbye! Have a nice day!")
            break
        else:
            print("ChatBot: I'm sorry, I don't understand that.")

# Run the chatbot
chatbot()
