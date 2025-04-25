## 🔥 GameCode Enhancer – AI-Powered Code Optimizer for Game Developers

A Streamlit-based tool that leverages **Groq’s Llama 3 API** to intelligently enhance, optimize, and clean game development code across popular engines and languages like Unity C#, Unreal C++, Godot GDScript, PyGame (Python), and JavaScript (HTML5 Games).  
It’s built for **game developers**, with a focus on **performance tuning, clean architecture, and best practices**.

---

### 🧠 What is GameCode Enhancer?

**GameCode Enhancer** is an intelligent code refactoring assistant powered by **Llama 3 (via Groq API)**. It takes your raw game development code and instructions and returns:

1. ✅ An enhanced version of your code
2. 🧾 A clear explanation of the improvements made
3. 🎮 Game-specific best practices and optimizations

---

### ✨ Key Features

- 🛠️ **AI-Powered Refactoring**: Uses Llama 3 to analyze and refactor code based on your needs (performance, readability, bug fixes, etc.)
- 🎮 **Game Dev Focus**: Tailored prompts designed for Unity, Unreal, Godot, PyGame, and HTML5 games
- 🚀 **Groq Inference Engine**: Ultra-fast LLM inference with 70B+ parameter models
- 🧾 **Explanation of Changes**: Get an easy-to-understand explanation alongside your improved code
- 📋 **Copy & Replace**: Copy AI-enhanced code or directly replace your original with one click
- 🧪 **Example Code Snippets**: Test the tool with built-in example code (like Unity character controllers)

---

### 📸 Demo Preview

> https://gamecode-enhancer.streamlit.app/

---

### 🚀 Getting Started

#### ✅ Prerequisites

- Python 3.9+
- Groq API Key
- A `.env` file with your key

```
GROQ_API_KEY=your_groq_api_key_here
```

---

#### 📦 Installation

```bash
git clone https://github.com/yourusername/gamecode-enhancer.git
cd gamecode-enhancer
pip install -r requirements.txt
```

---

#### ▶️ Run the App

```bash
streamlit run app.py
```

---

### 📂 Project Structure

```
.
├── app.py                # Main Streamlit App
├── .env                  # Groq API key (excluded in .gitignore)
├── requirements.txt      # Dependencies
└── README.md             # You're here!
```

---

### 🔒 Environment Setup

Use a `.env` file to store your Groq API key:

```
GROQ_API_KEY=your-api-key-here
```

---

### 💡 Supported Languages

- Unity C#
- Godot GDScript
- Unreal C++
- JavaScript (HTML5 games)
- Python (PyGame)

---

### 🧠 How it Works

1. Paste your original game code.
2. Describe your improvement request.
3. Click "Enhance My Code" – your code is sent to Groq's Llama 3 with a game-focused prompt.
4. Get enhanced code + an explanation – ready to copy or apply instantly.

---

### 🛠️ Technologies Used

- **Streamlit** – Interactive UI
- **Groq** – Fast LLM backend
- **Llama 3 (70B)** – Code comprehension and transformation
- **Python-dotenv** – Securely load API keys

---

### 🌐 Deployment (Optional)

You can deploy this app on platforms like:
- [Streamlit Community Cloud](https://streamlit.io/cloud)
- [Render](https://render.com/)
- [Heroku](https://www.heroku.com/)

---

### 🧪 Example Prompt

> 💬 Original Code (Unity C#):  
> ```csharp  
> transform.Translate(movement * speed);  
> ```  
>  
> 💡 Instruction:  
> "Improve performance and add jump functionality."

The AI will enhance your code and provide a detailed explanation of how the changes benefit gameplay and architecture.

---

### 🧑‍💻 Contributing

Pull requests are welcome. Feel free to fork this project and improve it further for:
- Model comparison
- Syntax highlighting improvements
- Local inference alternatives (e.g., Ollama, LM Studio)

---

### 📄 License

MIT License

---

### 🙌 Acknowledgements

- [Groq](https://groq.com/) for blazing-fast inference
- [Meta Llama 3](https://ai.meta.com/llama/)
- [Streamlit](https://streamlit.io/) for the rapid UI framework
