#Task class is used to define specific tasks that the agents will perform
from crewai import Task

#SerperDevTool which is imported from tools.py 
from tools import tool

#agents are imported from agent.py
from agents import news_researcher,news_writer

# Research task
research_task = Task(
  #describes goal and focus 
  description=(
    "Identify the next big trend in {topic}."
    "Focus on identifying pros and cons and the overall narrative."
    "Your final report should clearly articulate the key points,"
    "its market opportunities, and potential risks."
  ),

  expected_output='A comprehensive 3 paragraphs long report on the latest AI trends.',
  tools=[tool],
  agent=news_researcher,
)

# Writing task with language model configuration
write_task = Task(
  description=(
    "Compose an insightful article on {topic}."
    "Focus on the latest trends and how it's impacting the industry."
    "This article should be easy to understand, engaging, and positive."
  ),
  expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
  tools=[tool],
  agent=news_writer,

  #False as system waits for the research task to complete before proceeding to the writing task.
  async_execution=False,
  output_file='output.md'  # Example of output customization
)