from dotenv import load_dotenv
load_dotenv()
import os

#SERPER_API_KEY is stored in Environment Variable as to keep it secure and set it in Python Environment
os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

#SerperDevTool is The World's Fastest & CheapestGoogle Search API
#It will interact with Google Search data
try:
    from crewai_tools import SerperDevTool
    print("SerperDevTool imported successfully!")
except ImportError as e:
    print(e)

# Initialize the tool for internet searching capabilities
tool = SerperDevTool()