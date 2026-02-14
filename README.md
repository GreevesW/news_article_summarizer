# Web Scraper to Audio Summary

A Python application that scrapes webpage content, generates a summary using ChatGPT, and converts it to an audio file using text-to-speech.

## Overview

This project automatically:
1. Scrapes text content from any webpage
2. Generates a concise summary using ChatGPT
3. Converts the summary to an MP3 audio file

## How It Works

### Workflow

1. **webscraper.py** - Extracts webpage content
   - Prompts user for a URL
   - Uses BeautifulSoup to extract text from `<body>` tags
   - Validates and removes special characters (e.g., `©`, `&`)
   - Passes cleaned content to ChatGPT module

2. **chatgpt.py** - Generates summary
   - Receives scraped content
   - Sends content to ChatGPT API with custom prompt
   - Returns AI-generated summary

3. **main.py** - Creates audio file
   - Receives ChatGPT summary
   - Converts text to speech using Audiostack API
   - Saves output as `Summary.mp3`

## File Structure

```
.
├── main.py
├── chatgpt.py
├── webscraper.py
├── README.md
└── requirements.txt
```

## Installation

### Prerequisites

- Python 3.7+
- OpenAI API key
- Audiostack API key

### Setup Steps

1. **Install ChatGPT requirements**
   
   Follow the [ChatGPT Quick Start Guide](https://platform.openai.com/docs/quickstart) for detailed instructions.

2. **Install Audiostack SDK**
   
   ```bash
   pip install -U audiostack
   ```
   
   or
   
   ```bash
   pip3 install -U audiostack
   ```
   
   See [Audiostack SDK Quick Start](https://docs.audiostack.ai/docs/getting-started#quickstarts) for more information.

3. **Install BeautifulSoup**
   
   ```bash
   pip install beautifulsoup4
   ```

## Configuration

### API Keys

You'll need to configure API keys in the following locations:

- **ChatGPT API**: Line 6 in `chatgpt.py`
- **Audiostack API**: Line 12 in `main.py`

API keys can be stored as environment variables or imported as needed.

### ChatGPT Prompt Settings

The ChatGPT prompt can be customized with the following parameters:

- **Temperature**: Controls randomness of the response
- **Max Tokens**: Set to 300 to ensure complete responses
- **Character Limit**: Response limited to 340 characters (produces ~30 second audio)
  - Can be adjusted to any desired length

## Usage

1. Run the webscraper:
   ```bash
   python webscraper.py
   ```

2. Enter the URL when prompted

3. Wait for processing to complete

4. Find your audio summary saved as `Summary.mp3`

## Known Issues

- Some webpages may cause errors if the ChatGPT response contains special characters incompatible with the Audiostack TTS model
- Characters like `\` or `|` may cause processing failures

## Troubleshooting

If you encounter errors:

1. **Check ChatGPT output** - Verify the script doesn't contain unusual special characters (e.g., `\`, `|`)
2. **Verify installations** - Ensure all APIs and libraries are correctly installed:
   - ChatGPT API
   - Audiostack API
   - BeautifulSoup library
3. **Test API keys** - Confirm both API keys are valid and properly configured

## Output

The final audio file will be saved as **Summary.mp3** in the project directory.

## Dependencies

- `beautifulsoup4` - Web scraping
- `openai` - ChatGPT API integration
- `audiostack` - Text-to-speech conversion

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]