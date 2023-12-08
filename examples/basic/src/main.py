from gptool.gptool import Gptool
import os

tool = Gptool(
    openai_key=os.environ.get("OPENAI_KEY"),
    openai_url=os.environ.get("OPENAI_URL"),
)


# In a CI/CD pipeline or in dev mode on startup/hot reload
tool.index()

# Anywhere in the codebase
message = "What's the weather like in Toronto right now?"
response = tool.chat(
    messages=[{"role": "user", "content": message}],
    model="gpt-3.5-turbo-1106",
    top_n=3,
)

print(f"Message: {message}")
print(f"Response: {response}")
