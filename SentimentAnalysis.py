!pip install openai==0.28
!python -m spacy download en_core_web_sm
#importing open ai library
import openai
import spacy

#Set the API key here
openai.api_key = "OPEN_API_KEY"
# Load Spacy NER model
nlp = spacy.load("en_core_web_sm")

# Define the function to analyze sentiment with word-level contributions using GPT
def analyze_sentiment_with_words(review, category):
    prompt = f"Analyze the sentiment of the following {category} review and provide sentiment contributions for each word (percentage):\n\nReview: {review}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a sentiment analysis assistant."},
            {"role": "user", "content": prompt},
        ]
    )

    sentiment_analysis = response['choices'][0]['message']['content']
    return sentiment_analysis.strip()
  # Function to perform Named Entity Recognition (NER)
def extract_entities(review):
    doc = nlp(review)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Main function to perform sentiment analysis and NER
def main():
    # Get input from user
    category = input("Enter the category of the review (e.g., Food, Product, Place, Other): ").capitalize()
    review = input(f"Enter your {category.lower()} review: ")

    # Analyze the sentiment of the review with word-level contributions
    if review:
        print("\nPerforming Sentiment Analysis...\n")
        sentiment_with_contributions = analyze_sentiment_with_words(review, category)
        print(f"Sentiment Analysis with Word-Level Contributions: \n{sentiment_with_contributions}")

        # Perform Named Entity Recognition (NER)
        print("\nPerforming Named Entity Recognition (NER)...\n")
        entities = extract_entities(review)
        print(f"Named Entities in the Review: \n{entities}")
    else:
        print("Please enter a valid review.")

# Run the main function
main()
