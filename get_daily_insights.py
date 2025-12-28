from openai import OpenAI
import json

def get_daily_insights():
    client = OpenAI() 
    with open("prompt.txt", "r") as f:
        prompt = f.read()

    with open("reminders_output.txt", "r") as f:
        reminders = f.read()


    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "system", "content": prompt + "\n"},
            {"role": "user", "content": "Here is the list of reminders:\n" + reminders + "\n"}
        ]
    )  

    print(response.choices[0].message.content)
    content = response.choices[0].message.content
    if content is None:
        raise ValueError("No content returned from OpenAI response.")
    return json.loads(content)

