# WorkBuddy AI: Your Intelligent Business Assistant

## Overview

WorkBuddy AI is an all-in-one solution for streamlining everyday business tasks. This proof of concept application leverages advanced natural language processing to help you:

- Draft professional emails in seconds
- Summarize lengthy documents effortlessly
- Quickly access key information

## Features

1. **Text Assistant**: Summarize content from PDF files, web pages, or pasted text.
2. **Communication Assistant**: Generate various types of business documents, including tax memos, engagement letters, and emails with different tones.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/jatwg/AIConcepts
   cd AIConcepts
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   # On MacOS, use source venv/bin/activate  
   # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory and add the following variables:
   ```
   AZURE_OPENAI_API_KEY=your_api_key
   AZURE_OPENAI_VERSION=your_api_version
   AZURE_OPENAI_ENDPOINT=your_endpoint
   AZURE_DEPLOYMENTNAME=your_deployment_name
   ```

## Usage

Run the Streamlit app:


Navigate through the sidebar to access different features:
- Text Assistant
- Communication Assistant

## Docker Support

To run the application using Docker:

1. Build the Docker image:
   ```
   docker build -t aiconcepts .
   ```

2. Run the container:
   ```
   docker run -p 8501:8501 aiconcepts
   ```

Access the application at `http://localhost:8501` in your web browser.

## Project Structure

- `🏠 Home.py`: Main entry point of the application
- `pages/`: Contains individual pages for different features
- `llmhelper.py`: Handles interactions with the Azure OpenAI API
- `webhelper.py`: Provides web scraping functionality
- `filehelper.py`: Handles file operations (PDF reading, image processing)
- `emailhelper.py`: Generates email content based on user input and tone

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
