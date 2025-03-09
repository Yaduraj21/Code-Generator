# 🧠 Code Generator

A modern AI-powered code generation assistant built with Streamlit and Ollama. This application helps developers generate code, debug issues, and get coding assistance in real-time.

## 🌟 Features

- 💻 **Code Generation**: Get help with writing code in various programming languages
- 🐛 **Debugging Assistant**: Identify and fix code issues
- 📝 **Code Documentation**: Generate clear and concise documentation
- 🎨 **Modern UI**: Clean and responsive interface with custom styling
- 💬 **Interactive Chat**: Natural conversation interface for coding queries

## 🚀 Technologies Used

- [Streamlit](http://streamlit.io/) - Frontend framework
- [Ollama](http://ollama.ai/) - Local AI model hosting
- [LangChain](http://python.langchain.com/) - LLM framework
- [DeepSeek](http://deepseek.ai/) - AI model provider

## 📋 Prerequisites

- Python 3.8 or higher
- Ollama installed and running locally
- Sufficient system memory for running AI models

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/Yaduraj21/Code-Generator.git
cd Code-Generator
```

2. Install required Python packages:
```bash
pip install streamlit langchain-ollama
```

3. Make sure Ollama is installed and running with the required model:
```bash
ollama pull deepseek-r1:1.5b
```

## 🎮 Usage

1. Start the application:
```bash
streamlit run main.py
```

2. Open your browser and navigate to:
```
http://localhost:8501
```

3. Start asking coding questions in the chat interface!

## 💡 Features in Detail

### Model Configuration
- Customizable AI model selection
- Temperature control for response creativity
- Local model execution for privacy

### Chat Interface
- Real-time code generation
- Syntax highlighted code blocks
- Conversation history
- Markdown support for formatted responses

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Developer

Developed by Yaduraj Singh Yadav

## 🙏 Acknowledgments

- Thanks to Ollama for providing local AI model hosting
- Thanks to Streamlit for the amazing web framework
- Thanks to LangChain for the LLM tools
- Thanks to DeepSeek for the AI model 