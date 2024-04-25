import streamlit as st
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
    completion = response.completions[0] if response.completions else None
    return completion.data.text.strip() if completion else "No response"

def main():
    st.title("AI21 Chat Tool")

    # Provide your API key here
    api_key = "NxUgDvHHuMqon94X6esghP1EzG4VYEmm"

    user_input = st.text_input("You:")
    if st.button("Send"):
        ai_response = get_ai_response(user_input, api_key)
        st.write("AI:", ai_response)

if __name__ == "__main__":
    main()
