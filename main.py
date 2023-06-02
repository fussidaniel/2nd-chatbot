# Imports the os module and the openai library
import os
import openai

# Sets the OpenAI API key by using the environment variable called OPENAI_API_KEY
openai.api_key = os.getenv("OPENAI_API_KEY")

# Create a while loop that runs until the user types 'exit'
while True:
  # Gets input from the user to ask a question (blue text)
  question = input("\033[34mWhat is your question?\n\033[0m")
  
  # Checks if the user entered 'exit'
  if question.lower() == "exit":
    # Breaks the loop and prints a goodbye message (red text)
    print("\033[31mGoodbye!\033[0m")
    break
  
  # Uses the openai.ChatCompletion.create() method to generate a response to the question
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", # Uses the 'gpt-3.5-turbo' model
    messages=[
      {"role": "system", "content": "You are a helpful assistant. Answer the given question."}, # Instructs the AI with a system message
      {"role": "user", "content": question} # Uses the user's question as input
    ]
  )

  # Prints the response generated by the AI (green text) changes

  print("\033[32m" + completion.choices[0].message.content + "\n")