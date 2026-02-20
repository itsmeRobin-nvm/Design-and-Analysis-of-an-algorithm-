from openai import OpenAI

client = OpenAI(api_key="")


def chat():
    print("AI Chatbot Started (type 'exit' to quit)\n")

    messages = [
        {"role": "system", "content": "You are a helpful AI assistant."}
    ]

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        reply = response.choices[0].message.content
        print("AI:", reply)

        messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    chat()

