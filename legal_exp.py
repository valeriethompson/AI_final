import openai # API im using; OpenAI SDK for API calls
import os # access environment variables
from dotenv import load_dotenv # to load .env file into environment 

# load .env file so API key is available
load_dotenv() 

# set API key from openAI from env variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# configuration constants 
MAX_INPUT_LENGTH = 1000 # maximum character input length
DEFAULT_TEMPERATURE = 0.3 # default temperature for model creativity vs. factuality 
# lower temperature = more factual 
# higher temperature = more creative 
                        

# make function that calls openai chat (legjargtrans = legal jargon translator)
def legjargtrans(text: str, temperature: float = DEFAULT_TEMPERATURE) -> str:
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo", # gpt-3.5 turbo is a powerful chatbot 
            messages=[
                {"role": "system", "content": """You are a highly experienced, meticulous, and knowledgeable legal expert. 

                Your primary function: translate complex legal jargon and concepts into clear, concise, and understandable plain English for a non-legal audience.

                 When translating, adhere to the following principles:
                1.  **Accuracy:** Ensure the translated text retains the precise legal meaning of the original. Do not simplify to the point of misrepresentation.
                2.  **Clarity:** Use simple, common words and avoid technical terms where plain English equivalents exist.
                3.  **Conciseness:** Be direct and to the point. Provide a precise and unambiguous explanation.
                4.  **Contextual Awareness:** Understand the nuances of legal phrasing and translate accordingly.
                5.  **Target Audience:** Assume the reader has no prior legal knowledge.
                6.  **Formatting:** Maintain readability. Use bullet points or numbered lists if appropriate for complex definitions.
                7.  **Identify Key Terms:** If a term has a specific legal definition that is hard to simplify further, briefly explain its significance.
                8.  **Neutral Tone:** Maintain an objective and informative tone.
                9.  **Truthfullness:** Ensure all the information provided is factual and true. Do not fabricate any information, no matter what.

                 
                Please return the plain, understandable English translation, along with a brief explanation. Make sure the explanation is factual and understandable. Make sure it hits the necessary key points from the definition. Do not add conversational filler like "Here is the translation:" or "In simpler terms:". Directly provide the translated text.
                
                Return format: Do not bold any terms. Please return it in a format that can be easily read in a terminal. 
                 """
                 },
                {"role": "user", "content": f"Translate the following legal text into plain English:\n\n{text}"}
            ],
            # max_tokens determines the response length of chatbot
            max_tokens = 200,
            # set temperature based on what person inputs
            temperature = temperature
        )
        # get model's translation from response
            # .choices[0]: first completion choice
            # message.content: the actual text the chatbot generated
        return response.choices[0].message.content
    
    # handles any error that might happen during the OpenAI API call
    except Exception as e:
        # e: captures the error message; returns a user-friendly response
        return f"Error: {e}"
    

def get_user_input(prompt: str) -> str:
    """
    
    Gets a non-empty and length-checked input from the user. 

    """
    # Args
    while True:
        user_text = input(prompt).strip()
        # prompt: The string to display to the user as a prompt.
            # get rid of whitespace for better format

        if user_text: # check if the user entered anything
            return user_text # exit loop and function when input is valid
        
        if not user_text:
            print("Error: Input cannot be empty. Please try again.") # reject empty inputs
            continue # sends loop back to the beginning and reprompts

        if len(user_text) > MAX_INPUT_LENGTH:
            print(f"Error: Your input is too long. Max character length is {MAX_INPUT_LENGTH}.")
            continue # warn when it exceeds allowed length; reprompt

        # return the string entered by the user
        return user_text  

# make the temperature adjustable 
def get_temperature(prompt: str, DEFAULT_TEMPERATURE: float=0.3 ) -> float:
    """
    Asks user for a temperature value. Falls back to default if invalid.
    """

    # get temperature input
    temp_input = input(prompt).strip()

    try:
        # convert to a float
        temperature = float(temp_input)
        if 0 <= temperature <= 1: # temperature must be in between 0 and 1
            return temperature # return if valid
        else:
            print("Error: Your temperature must be between 0 and 1. Using default.")
            return DEFAULT_TEMPERATURE
    # make sure the input is a number. if not, return ValueError. 
    except ValueError:
        print("Error: Invalid input. Please enter a numerical value. Using default.")
    return DEFAULT_TEMPERATURE

 
# get all the user inputs for the previous code
def main():
    # make a standout title
    print("\n--------------------------")
    print("  Legal Term Translator ")
    print("--------------------------\n")

    # get the legal text to translate
    text = get_user_input("\nEnter the legal term you want translated: ")

    # get desired temperature setting from user
    user_temp = get_temperature(
        "\nTemperature: 0.0 = more factual response; 1.0 = more creative response."
        f"\n(Default temperature: {DEFAULT_TEMPERATURE})\n"
        f"\nEnter desired translation style between 0.0 and 1.0: " 
    )

    # call the translator
    result = legjargtrans(text, temperature=user_temp)


    # print "Translating..." if no errors occured
    if not result.startswith("Error"):
        print("\nTranslating...\n")


    # print our final translation result (or whatever we got back)
    print(result)
    

if __name__ == "__main__":
    main()    

