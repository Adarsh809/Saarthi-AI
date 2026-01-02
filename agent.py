from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from tools import analyze_image_with_query

from dotenv import load_dotenv
import os

load_dotenv()

# 1. Define the System Prompt
system_prompt = """You are Saarthi — a witty, clever, and helpful assistant"
    Here’s how you operate:
        - FIRST and FOREMOST, figure out from the query asked whether it requires a look via the webcam to be answered, if yes call the analyze_image_with_query tool for it and proceed.
        - Dont ask for permission to look through the webcam, or say that you need to call the tool to take a peek, call it straight away, ALWAYS call the required tools have access to take a picture.
        - When the user asks something which could only be answered by taking a photo, then call the analyze_image_with_query tool.
        - Always present the results (if they come from a tool) in a natural, witty, and human-sounding way — like Dora herself is speaking, not a machine.
    Your job is to make every interaction feel smart, snappy, and personable. Got it? Let’s charm your master!"
    """


# 2. Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
)

# 3. Create the Agent using the new v2 abstraction
saarthi_agent = create_agent(
    model=llm,
    tools=[analyze_image_with_query],
    system_prompt=system_prompt,
)

def ask_agent(user_query: str) -> str:
    inputs = {"messages": [HumanMessage(content=user_query)]}
    
    try:
        # Run the agent (this executes the Graph under the hood)
        response = saarthi_agent.invoke(inputs)
        
        # Extract the final message content
        return response['messages'][-1].content
    except Exception as e:
        return f"Saarthi encountered a snag: {str(e)}"

# if __name__ == "__main__":
#     result = ask_agent("what is the capital of India?")
#     print(f"Saarthi: {result}")

