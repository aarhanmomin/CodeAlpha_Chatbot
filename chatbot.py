def chatbot():
    print("Chatbot: Hi! I am your simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()   # take input & convert to lowercase

        if user_input == "hello":
            print("Chatbot: Hi!")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user_input == "what is your name":
            print("Chatbot: I am a basic rule-based chatbot.")

        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break   # exit loop

        else:
            print("Chatbot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()
