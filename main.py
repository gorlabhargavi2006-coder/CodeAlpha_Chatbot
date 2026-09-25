def get_response(message):
    msg = message.lower().strip()
    if msg in ("hello", "hi", "hey"):
        return "Hi!"
    elif "how are you" in msg or msg == "how are you":
        return "I'm fine, thanks!"
    elif msg in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye!"
    elif msg in ("thanks", "thank you"):
        return "You're welcome!"
    else:
        return "Sorry, I don't understand."


def chat():
    print("Simple rule-based chatbot. Type 'bye' to exit.")
    while True:
        try:
            user = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            print("Bot: Goodbye!")
            break
        if not user:
            continue
        reply = get_response(user)
        print("Bot:", reply)
        if reply == "Goodbye!":
            break


if __name__ == "__main__":
    chat()
