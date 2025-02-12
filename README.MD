# AutoResearch

AutoResearch is a multi-agent research and writing framework powered by CrewAI. It leverages autonomous **Researcher** and **Writer** agents to analyze real-time tech trends using Google search data and Google Gemini AI for content generation.

## Features

- **Autonomous Research & Writing**: Agents fetch and process online information.
- **Google Search Integration**: Utilizes SerperDev API for retrieving search data.
- **AI-Powered Content Generation**: Uses Google Gemini AI for text synthesis.
- **Automated Task Execution**: Agents collaborate to complete research and documentation tasks.

## Prerequisites

Ensure the following dependencies are installed:

- **Python** (3.8 or higher)
- **Git** (for cloning the repository)
- API Keys for:
  - **Google Generative AI**
  - **SerperDev** (Google Search API)

## Project Structure

```plaintext
AutoResearch/
├── venv/                     # Virtual environment
├── .env                      # Environment variables (API keys)
├── agents.py                 # Definition of Researcher & Writer agents
├── crew.py                   # Main logic for task execution
├── tasks.py                  # Task definitions for agents
├── tools.py                  # Google search tools
├── output/                   # Directory for generated research content
├── requirements.txt          # Project dependencies
```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/AutoResearch.git
cd AutoResearch
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Keys
- Create a `.env` file in the root directory.
- Add your API keys in the following format:
```ini
GOOGLE_GEMINI_API_KEY=your_google_gemini_key
SERPERDEV_API_KEY=your_serperdev_key
```

### 5. Run the Project
```bash
python crew.py
```

## Usage
- The **Researcher Agent** fetches relevant data from Google.
- The **Writer Agent** synthesizes and structures the content.
- The output is saved in the `output/` directory as a Markdown file.

## Future Enhancements
- Expand search capabilities to include academic databases.
- Improve summarization techniques using advanced LLMs.
- Integrate a UI for seamless interaction.

---

Developed with ❤️ using CrewAI & Google Gemini.
