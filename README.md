# AI Assistant using OpenAI API

A simple AI-powered question-answering assistant built with **Python** and the **OpenAI API**. This project demonstrates how to securely integrate OpenAI models into a Python application using environment variables, following industry-standard project structure and Git best practices.

---

## Project Overview

This application allows users to send questions to an OpenAI language model and receive intelligent responses in real time.

The project focuses on building a clean and secure foundation for AI applications by implementing:

* OpenAI API integration
* Secure API key management using `.env`
* Environment variable loading with `python-dotenv`
* Virtual environment management
* Git and GitHub version control
* Professional project structure

---

## Features

* Ask questions using OpenAI models
* Secure API key management
* Clean and beginner-friendly Python code
* Modular project structure
* GitHub-ready repository
* Easy setup for new developers

---

## Tech Stack

* Python 3.x
* OpenAI Python SDK
* python-dotenv
* Git
* GitHub

---

## Project Structure

```text
ai-assistant-openai/
│
├── app.py                 # Main application
├── requirements.txt       # Project dependencies
├── README.md              # Documentation
├── .gitignore             # Ignored files and folders
├── .env                   # API key (not committed)
└── .venv/                 # Virtual environment (not committed)
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/phanisharma197/ai-assistant-openai.git
```

### 2. Navigate to the project

```bash
cd ai-assistant-openai
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

#### Windows

```bash
.venv\Scripts\activate
```

#### macOS/Linux

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configure API Key

Create a file named `.env` in the project root.

Add your OpenAI API key:

```text
OPENAI_API_KEY=your_api_key_here
```

> **Important:** Never commit your `.env` file to GitHub.

---

## Run the Application

```bash
python app.py
```

The assistant will send your prompt to the OpenAI API and display the generated response.

---

## Concepts Demonstrated

* REST API integration
* Environment variables
* Secure credential management
* OpenAI SDK usage
* Python project organization
* Dependency management
* Git workflow
* GitHub repository management

---

## Security Best Practices

* API keys stored in `.env`
* `.env` excluded using `.gitignore`
* Virtual environment excluded from version control
* Dependencies managed with `requirements.txt`

---

## Future Improvements

* Conversational chat interface
* Chat history and memory
* Streamlit web application
* Retrieval-Augmented Generation (RAG)
* Function calling and tool use
* Voice assistant integration
* Docker containerization
* Cloud deployment

---

## Author

**Phani Sharma**

GitHub: https://github.com/phanisharma197

---

## Acknowledgements

Built using the OpenAI API as part of my AI Engineering learning journey. This project serves as a foundation for developing advanced AI applications, including conversational assistants, RAG systems, and AI agents.
