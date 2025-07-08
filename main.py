from langchain_core.messages import HumanMessage
from langchain_together import ChatTogether
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

@tool
def calc(a: float,b:float)->str:
    """Useful for performing basic arithmetic calculations with numbers"""
    print("the tool  has been called")
    return f"The sum of {a} and {b} is {a+b}"


def main():
    'model =ChatOpenAI(temperature=0)'
    model = ChatTogether(
        model="meta-llama/Llama-3-70b-chat-hf",  
        temperature=0
    )


    tools=[calc]
    agent_executor=create_react_agent(model,tools)

    print("Hi I am your AI assitant type 'quit' to exit")
    print("Ask  me anything you want or chat with me")


    while True:
        user_input=input("\nYou: ").strip()
        if user_input=="quit":
            break
        print("\nAssistant: ",end="")
        for chunk in agent_executor.stream(
            {"messages":[HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content,end="")
        print()


if __name__=="__main__":
    main()                    