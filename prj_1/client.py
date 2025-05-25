#
from openai import OpenAI
client= OpenAI(
    api_key="sk-proj-WxS17ehGk2PnwmzCHcDwT3BlbkFJFMj6bYTk9jG1bqZaFTcj"
)
completion=client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system", 
            "content": "You are a virtual assitant named jarvi"
        },
        {
            "role":"user",
            "content":"what is program"
        }
    ]
)
print(completion.choices[0].messages.content)