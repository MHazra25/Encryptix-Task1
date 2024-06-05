import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_input(user_input):
    # Tokenize the user input
    tokens = word_tokenize(user_input.lower())
    # Remove stopwords
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return tokens

def chatbot_response(user_input):
    tokens = preprocess_input(user_input)
    
    # Join tokens back to a single string for pattern matching
    processed_input = " ".join(tokens)
    
    # Define patterns and responses
    greetings_pattern = r"\b(hi|hello|hey)\b"
    goodbye_pattern = r"\b(bye|goodbye|see you)\b"
    how_are_you_pattern = r"\b(how you|how going)\b"
    name_pattern = r"\b(name|who you)\b"
    
    # Matching patterns with user input
    if re.search(greetings_pattern, processed_input):
        return "Hello! How can I assist you today?"
    elif re.search(goodbye_pattern, processed_input):
        return "Goodbye! Have a great day!"
    elif re.search(how_are_you_pattern, processed_input):
        return "I'm a chatbot, so I don't have feelings, but I'm here to help you!"
    elif re.search(name_pattern, processed_input):
        return "I am a simple rule-based chatbot created by an AI enthusiast."
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

# Main interaction loop
def main():
    print("Chatbot: Hi there! I am a simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye", "see you"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
