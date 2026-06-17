#
while True:
    
    raw_input_text = input("You: ")
    clean_input = raw_input_text.lower().strip()

    
    if clean_input in ("bye", "exit", "quit"):
        print("Chatbot: Goodbye! Have a great day.")
        break

    reply = responses.get(clean_input, "I do not understand. Could you rephrase that?")
    print("Chatbot:", reply)