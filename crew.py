#Crew represents a group of agents working together to complete a set of tasks
from crewai import Crew,Process
from tasks import research_task,write_task  
from agents import news_researcher,news_writer

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[news_researcher,news_writer],
    tasks=[research_task,write_task],
    verbose=True,
    #A sequential process ensures that each task depends on the output of the previous one.
    #Here writer_agent will wait for researcher_agent for collecting the data
    process=Process.sequential,
)

## starting the task execution process wiht enhanced feedback
result=crew.kickoff(inputs={'topic':'AI in healthcare'})
print(result)