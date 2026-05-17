# AI Engineering Journey

A personal sandbox for learning and building with modern AI tooling — starting with the OpenAI Python SDK and growing into agents, RAG, evaluation, and beyond.

## Stack

- **Python 3.10+**
- **OpenAI Python SDK** (`openai`)
- **python-dotenv** for local secrets management
- **Pydantic** for typed data models

## Quickstart

### 1. Clone and enter the project

```bash
git clone https://github.com/Vignan18/ai-engineering-journey.git
cd ai-engineering-journey
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # macOS / Linux
# .\venv\Scripts\activate  # Windows PowerShell
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Copy the example env file and fill in your OpenAI key:

```bash
cp .env.example .env
```

Then edit `.env` and set:

```
OPENAI_API_KEY=sk-...
```

Get a key from <https://platform.openai.com/api-keys>.

> `.env` is gitignored — never commit your real keys.

### 5. Run the hello-world script

```bash
python app.py
```

You should see a short completion printed to the console.

## Project structure

```
ai-engineering-journey/
├── app.py              # Entry point / hello-world example
├── requirements.txt    # Pinned Python dependencies
├── .env.example        # Template for required environment variables
├── .gitignore
└── README.md
```

## Roadmap

- [ ] Prompt engineering experiments
- [ ] Structured outputs with Pydantic
- [ ] Tool / function calling
- [ ] Retrieval-Augmented Generation (RAG)
- [ ] Agentic workflows
- [ ] Evaluation harness

## License

MIT — feel free to fork and learn along.
