# OpenAI Recipe Bot Sample

This example demonstrates how to build a simple Strands agent using OpenAI.
The agent acts as a cooking assistant and can search the web for recipes
using a `websearch` tool built with `duckduckgo-search`.

## Setup

1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
2. Create a `.env` file in this directory and add your OpenAI API key:
   ```bash
   OPENAI_API_KEY=sk-your-key
   ```

## Running the Bot

Run the `recipe_bot.py` script:

```bash
python recipe_bot.py
```

Interact with the bot at the command line. Type `exit` to quit.
