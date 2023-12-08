from gptool.gptool import Gptool
import os

tool = Gptool(
    openai_key=os.environ.get("OPENAI_KEY"),
    openai_url=os.environ.get("OPENAI_URL"),
)


# In a CI/CD pipeline or in dev mode on startup/hot reload
tool.index()


# Please make sure setup the TMDB environment variables:
# TMDB_API_KEY, TMDB_SESSION_ID, TMDB_LANGUAGE
message = "Tell me about the movie Interstellar"
print(f"Message: {message}")
response = tool.chat(
    messages=[{"role": "user", "content": message}],
    model="gpt-3.5-turbo-1106",
    top_n=5,
)
print(f"Response: {response}")
