def rule_based_chatbot():
    knowledge_base = {
        "hello": "Hello! Welcome to DecodeLabs AI Support. How can I assist you today?",
        "hi": "Hi there! What can I help you with?",
        "what is your name": "I am the DecodeLabs Rule-Based AI Chatbot v1.0.",
        "who created you": "I was designed as part of the DecodeLabs AI Engineering Internship.",
        "help": "You can ask about my name, creation, available courses, or type 'exit' to quit.",
        "courses": "DecodeLabs offers training tracks in Artificial Intelligence, Machine Learning, and Data Science.",
        "bye": "Goodbye! Have a productive day coding."
    }

    print("      AI CHATBOT  ")
    print("Type 'exit' or 'quit' at any time to leave.\n")

    while True:
        raw_input = input("You: ")
        clean_input = raw_input.strip().lower()

        if clean_input in ["exit", "quit", "bye"]:
            print("Bot:", knowledge_base.get("bye", "Goodbye!"))
            print("\n[Session Terminated Cleanly]")
            break

        if not clean_input:
            continue

        fallback_response = "I'm sorry, I don't understand that command yet. Type 'help' to see what I can answer."
        response = knowledge_base.get(clean_input, fallback_response)

        print(f"Bot: {response}\n")

if __name__ == "__main__":
    rule_based_chatbot()