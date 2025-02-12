# Importing the Agent class from the crewai module, agents are used executing tasks.
from crewai import Agent, LLM

#SerperDevTool which is imported from tools.py 
from tools import tool

# dotenv helps load environment variables from a .env file into the system.
from dotenv import load_dotenv
# Load environment variables from the .env file into the application.
load_dotenv()
#Use to integrates with Google's Generative AI tools
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai

import os

api_key = os.getenv("GOOGLE_API_KEY")
credential_path = r"D:\Nirma University\Sem - 5\Natural Language Computing_Processing (NLP)\Innovative Assignment\CrewAI\crewgooglegemini\client_secret_883697634622-ovbt477hc6uuc8e5g6uv6s1fgj7dj7hr.apps.googleusercontent.com.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
genai.configure(api_key=api_key)
llm=LLM(model="gemini-1.5-flash",api_key=api_key)

# ## call the gemini model
# llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
#                            verbose=True, #When set to True, this enables detailed output or logs for debugging and transparency.
#                            temperature=0.5, #Lower values (closer to 0) make responses more deterministic and focused.
#                                             #Higher values (closer to 1) make responses more creative and diverse.
#                            google_api_key=os.getenv("GOOGLE_API_KEY")) #Loading from .env file


# Creating a senior researcher agent with memory and verbose mode
news_researcher=Agent(
    
    # Many role available in CrewAI
    # Researcher(Focused on exploring topics and gathering data), 
    # Assistant(help with tasks such as scheduling, answering questions, or summarizing information.)
    # Advisor(Offers strategic advice)
    # Teacher(Explains concepts or guides users)
    role="Senior Researcher",

    #specifies the agent's objective
    goal='Unccover ground breaking technologies in {topic}',

    #enables detailed logging or output during the execution of tasks or processes
    verbose=True,

    #Model can remember past information i.e. remember context
    memory=True,

    #Backstory Shape the tone, style, or approach of the agent's responses
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."
    ),
    tools=[tool],
    #OpenAI will be by default LLM if not specified
    llm=llm,
    #If true agent can interact with other agents
    allow_delegation=True

)

## creating a write agent with custom tools responsible in writing news blog

news_writer = Agent(
  # The writer agent's main task is to create, generate, or assist in the production of written content
  role='Writer',
  goal='Narrate compelling tech stories about {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools=[tool],
  llm=llm,
  #Writer task is writing content without relying on other agents for assistance.
  allow_delegation=False
)

