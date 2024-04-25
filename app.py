#Working AI21 Model Abhishek

from ai21 import AI21Client
from ai21.models import Penalty

def get_ai_response(prompt, api_key):
    client = AI21Client(api_key=api_key)
    response = client.completion.create(
        model="j2-ultra",
        prompt=prompt,
        num_results=1,
        max_tokens=200,
        temperature=0.7,
        top_k_return=0,
        top_p=1,
        presence_penalty=Penalty(
            scale=1,
            apply_to_numbers=True,
            apply_to_punctuation=True,
            apply_to_stopwords=True,
            apply_to_whitespaces=True,
            apply_to_emojis=True
        ),
        count_penalty=Penalty(
            scale=1,
            apply_to_numbers=True,
            apply_to_punctuation=True,
            apply_to_stopwords=True,
            apply_to_whitespaces=True,
            apply_to_emojis=True
        ),
        frequency_penalty=Penalty(
            scale=1,
            apply_to_numbers=True,
            apply_to_punctuation=True,
            apply_to_stopwords=True,
            apply_to_whitespaces=True,
            apply_to_emojis=True
        ),
        stop_sequences=[]
    )
    completion = response.completions[0]  # Get the first completion
    return completion.data.text.strip()  # Extract text from the completion



def main():
    print("Welcome to the AI21 Chat Tool!")
    print("You can start chatting. Type 'exit' to end the conversation.")
    
    # Provide your API key here
    api_key = "key"
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        ai_response = get_ai_response(user_input, api_key)
        print("AI: ", ai_response)

if __name__ == "__main__":
    main()
