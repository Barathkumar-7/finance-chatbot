from chatbot import FinanceChatbot

def run_chatbot():
    bot = FinanceChatbot()
    print("💰 Finance Control Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Goodbye! Stay financially healthy. 💸")
            break
        response = bot.get_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    run_chatbot()
