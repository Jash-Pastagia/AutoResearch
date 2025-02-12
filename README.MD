# CrewAI-Project
 This project implements a Multi Agents Framework using Crew AI. Here, models will search on Google search data andd fetch the information and store in a particular file.



## Prerequisites

Ensure the following software is installed:

- **Python** (version 3.8 or higher)
- **Git** (for cloning the repository)
- An **API Key** for Google Generative AI and SerperDev

## Project Structure

```plaintext
RAG PROJECT/
├── venv/                     # Virtual environment
├── .env                      # Environment variables (API keys)
├── agents.py                 # Multiple Agents defined 
├── crew.py                   # Main logic for creating tasks, assigning agents, and triggering tasks
├── tasks.py                  # Tasks is defined which will done by Agents
├── tools.py                  # Tools for search data on google 
├── new-blog-post.md         # Ouput of the model is stored here
├── requirements.txt          # List of dependencies
```
## Setup Instructions

Follow these steps to set up and run the project on your local machine:

### 1. Install Python
- Download Python from the [official Python website](https://www.python.org/downloads/).
- During installation, make sure to check the box **Add Python to PATH**.

### 2. Clone the Repository
- Open a terminal or command prompt.
- Clone the repository using
```terminal
git clone https://github.com/your-username/crewai-project.git
```
- Navigate into the project folder:
```terminal
cd crewgooglegemini
```
### 3. Set up a Virtual Environment
- Create a virtual environment to manage dependencies:
bash
```terminal
python -m venv venv
```
- Activate the virtual environment:
-- On Windows:
```terminal
Python Virtual Envirnment
.\\venv\\Scripts\\activate
```
- On macOS and Linux:
```bash
source venv/bin/activate
```command in your terminal:
  ```bash
  python --version
