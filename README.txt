Explanation of the code:

The webscraper.py file runs first and asks for the URL of a webpage to be entered. Using the beautiful soup module from the bs4 libary, the program gets all of the text between the body tags of the websites html file. Validation is then carried out using a for loop to remove any unusable special characters from the code ( such as "©" and "&"). The content between the body tags is then imported into the chatgpt.py file. The content is then inserted into a prewritten chatGPT prompt and the response is saved. The chatGPT response is then sent to the main.py file where it is saved as a script. The script is then compiled into a TTS audio file which is saved as Summary.mp3 .

File list:

main.py
chatgpt.py
webscraper.py
README.txt

The audio file will be saved as Summary.mp3 after the code has been run.

ChatGPT prompt:

- The temperature variable changes the randomness of the chatGPT response.
- The max tokens is set to 300 to ensure that a full response can be retrieved from chatGPT.
- The prompt asks ChatGPT to keep the response under 340 characters. This is done to keep the audio file under 30 seconds, but can be changed to any desired value.

API Keys:

Unique API keys for the chatGPT API and Aflorithmic Audiostack API are required for line 6 in chatgpt.py and line 12 in main.py respectively. These API keys can be imported or stored as privates. 

Installation:

- follow the chat gpt quick start guide for information on how to install the requirements. https://platform.openai.com/docs/quickstart

- The SDK for audiostack can be installed using the command 
"pip install -U audiostack" or "pip3 install -U audiostack"
Audiostack SDK quick start: https://docs.audiostack.ai/docs/getting-started#quickstarts

- Beautiful soup can be installed using the command "pip install beautifulsoup4"

Known Bugs:

- Some webpages may cause an error to occur if the chatGPT reply contains special characters wwhich cannot be used in the audiostack TTS model.

Troubleshooting:

- Check that the chatGPT script does not have any unusual special characters. (E.g. \ or | )

-Verify that the chatGPT API, audiostack API, and BeautifulSoup libary have been correctly installed.



