from google.adk.agents import Agent
from Quote_boy.prompt import ROOT_AGENT_INSTRUCTION
from Quote_boy.tools import count_characters
import sys

root_agent = Agent(
    name="Quote_boy",
    model="gemini-2.0-flash",
    description="You are Quote_boy. Your purpose is to provide a wonderful two-line quote when the user gives you a topic. Await the user's topic",
    instruction=ROOT_AGENT_INSTRUCTION,
    tools=[count_characters],
)

print(sys.path)