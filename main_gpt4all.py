from gpt4all import GPT4All

# Inisialisasi model dengan path lokal
model = GPT4All("Phi-3-mini-4k-instruct.Q4_0.gguf")

print("Welcome to AI Chat! Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Bye! Have a nice day!")
        break

    response = model.generate(user_input)
    print(f"AI: {response}")
