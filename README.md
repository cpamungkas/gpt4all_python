## GPT 4 All 

runs large language models (LLMs) privately on everyday desktops & laptops.

No API calls or GPUs required

## Install GPT4All Python
```bash
pip install gpt4all
```
my recommend installing gpt4all into its own virtual environment using venv

```python
from gpt4all import GPT4All

# Inisialisasi model
# If it's your first time loading a model, it will be downloaded to your device and saved
model = GPT4All("Phi-3-mini-4k-instruct.Q4_0.gguf") 

print("Welcome to AI Chat! Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Bye! Have a nice day!")
        break

    response = model.generate(user_input)
    print(f"AI: {response}")
```
