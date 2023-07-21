import os
import openai
from webscraper import content
#Imorts the webpage text from the webscraper.py file

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_prompt(content):
  return """You are an AI Article Summeriser, 
The summaries you provide will be synthesized using Text to speech 

Here is an Article:{}

please give me an accurate summary of this article, including all important information, but keep it below 340 characters.""".format(
    content.capitalize())
#defines the general prompt given to chat gpt
#The websites text will be entered between {}


response = openai.Completion.create(
  model="text-davinci-003",
  prompt=generate_prompt(content),
  temperature=0.6,
  max_tokens = 300
  #Max tokens is set to 300 to ensure that the chatGPT API returns a full response
)
print(response)
final = response.choices[0].text
#Stores the text portion of the response from chatGPT in the variable final

originalchr = [ chr(34), chr(39), chr(194), "©", chr(92), "&"]
newchr = [ "", "", "", "", "", "and"]

for i in range(0,6):
  final = final.replace( originalchr[i], newchr[i])
print(final)

#Final is later imported into the main.py file



