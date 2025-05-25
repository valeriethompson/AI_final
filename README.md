What the PoC does:

My proof-of-concept is a legal jargon translator with an adjustable temperature. Python and OpenAI's GPT-3.5-turbo model prompts users to enter a legal term—mens rea, amicus curiae, etc.—–and temperature——a hyperparameter controlling the output's creativity level. 

My code first imports necessary libraries (see the "How to set it up" question) and calls my API key to interact with GPT-3.5-turbo. Then, it sets two constants: max_input_length and default_temperature. Max_input_length sets the maximum amount of characters the chatbot can take. Default_temperature sets baseline creativity level as 0.3—mostly factual with a pinch of creativity. 

Next, my legal_exp.py defines the function "legjargtrans." It has two parameters: text–—a string—–and temperature–—a float, normally set to "default_temperature." The text string allows the user to input the legal phrase or jargon that they want to translate. The temperature float, on the other hand, controls the scope of the translation. A lower temperature will return a more direct and less abstract translation, while a higher temperature will return a varied and potentially creative response. 

Within my legjargtrans function are the chatbot "principles". It first connects to OpenAI, selecting the GPT-3.5-turbo model and opening a new chat. The model is given a plethora of parameters—it is instructed to act as an expert legal translator and ensures an accurate, unbiased response. The user's term is then passed through as the last prompt. 

This function also handles any OpenAI errors. "except Exception as e:" handles any error that might happen during the OpenAI API call, while "return f"Error: {e}"" captures the error message and returns a user-friendly response.

The "get_user_input" function gets a non-empty and length-checked input from the user. It's only parameter is "prompt"––the string that asks the user for an input. The function body has one major argument: while True. Under this, the user's input is saved and stripped of any potential whitespace (characters that represent empty or blank space). If the user's input is valid and only contains english characters, the function returns user_text. If the user's input is empty, the function rejects the input and prints an Error, reprompting the user. Additionally, if the user's input exceeds the max_input_length of 1000, it warns the user, reprompting them. The function loops until the user has input a valid term. 

The "get_temperature" function takes 2 parameters: the user's prompt—–a string—–and the default_temperature—–a float with a value of 0.3. It asks the user for a temperature value after entering a legal term. If their input is invalid, the function defaults to 0.3. Additionally, if the user inputs a non-numerical value, a ValueError is raised, and the temperature defaults. 

The final function——def main()—prints a title "Legal Term Translator" enclosed by dashes for emphasis. It then prompts the user for their term——"text = get_user_input"——and their desired temperature––"user_temp = get_temperature." The translator is then called, passing the user's text and temperature through the "def legjargtrans()" function. 

If no Errors are raised, the function prints a "Translating..." message. For both aesthetics and reassurance, this aspect confirms that the user's request has been received and the program is actively working. Following this and concluding my code, the function displays the result: an accurate legal translation with a brief explanation. 

My proof-of-concept embodies my research paper's point about increased accessibility. It takes complex legal terms and translates them into understandable, plain English for a non-legal audience. It also acts as a "double-edged magnifying glass." On one hand, it clearly shows the power of LLMs, highlighting their ability to translate and simplify. On the other hand, it magnifies AI limitations, such as the loss of nuance or potential oversimplification. This tool serves as a concrete example of the multifaceted impact AI is already having on Law. 


How to set it up (libraries needed - provide requirements.txt):

Setting up my legal translator requires installing two libraries: OpenAI—–for interacting with the OpenAI API––and Python dotenv––for securely loading your API key from an environment (.env) file. To install these, use pip's "pip install -r requirements.txt. I've provided the necessary libraries within the requirements.txt file. 


How to run it:

To run the Legal Term Translator, first ensure you've completed the "How to set it up" steps. Once the correct libraries are downloaded, open your terminal or command prompt and navigate to the project's main directory where your Python script (e.g., legal_exp.py) is located. Then, type "python legal_exp.py" and press Enter (Note: Depending on your Python installation, you may need to use python3 instead of python). The application will then prompt you to enter a legal term to translate and your desired temperature setting, returning the translated result. 


Any API keys needed (explain how the user should provide their own):

This application requires an OpenAI API key to function. This key ensures the program can access and interact with OpenAI's language models for term translation. If you don't already have one, first navigate to OpenAI's platform and create an account ([OpenAI's Platform Homepage](https://platform.openai.com/docs/overview)). Once logged in, you can typically find the option to create new API keys under "API keys" or "Personal" settings. Generate a new secret key and make sure to save it in a secure place. 

Next, create a .env file in your project directory. This file is used to securely store your API key. Inside the .env file, add your API key in the following format (without any quotes):

OPENAI_API_KEY="your_actual_secret_api_key_here"

Replace "your_actual_secret_api_key_here" with the actual secret API key you obtained from OpenAI.


It is important to note that I had to fill up my API key with money to use it. I have provided my API key in my .env file, so feel free to use that when running the code.  


Data source and format (if applicable):

I don't use a traditional data source. Instead, my program interacts with OpenAI's GPT-3.5-turbo. 


