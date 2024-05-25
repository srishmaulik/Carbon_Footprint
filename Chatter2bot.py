import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

# Simple function to generate responses
def generate_response(input_text):
    doc = nlp(input_text)
    if "hello" in input_text.lower():
        return "Hi there!"
    elif "how are you" in input_text.lower():
        return "I'm doing well, thank you."
    elif "bye" in input_text.lower():
        return "Goodbye!"
    else:
        return "I'm not sure how to respond to that."

# Chat function
def chatbot():
    print("Hi, I'm the spaCy ChatBot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("ChatBot: Goodbye!")
            break
        response = generate_response(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    chatbot()
