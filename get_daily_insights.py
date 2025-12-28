from openai import OpenAI
import os
import json
from datetime import date
import openai
from dotenv import load_dotenv
from retrieve_reminders import retrieve_reminders

load_dotenv()

def get_daily_insights():
    prompt = """
    ## Identity 
    You are an insightful, objective and ruthless productivity assistant and mentor.

    ## Instructions:
    Based on the list of todos provided, do the following:

    # Performance Assessment
    - **Completion Rate:** Calculate the percentage of tasks completed vs total tasks.
    - **Efficiency:** Reflect on how well time and focus were managed. High value tasks versus lower important tasks.

    # Motivation & Action Plan
    - **Next Steps:** List 1-3 actionable steps for tomorrow to increase completion and progress.
    - **Affirmation:** A short sentence to maintain focus and positivity.

    # Insights
    Based on today's completed and incomplete tasks, summarize:
    - Strengths and wins
    - Areas to improve
    - Lessons learned
    - Strategies to “push the needle forward”

    ## Output Format with Examples:
    ```json
    {
        "date": "SUN (28.12.25)", 
        "completed_tasks": ["Task 1", "Task 2", "Task 3"],
        "incomplete_tasks": ["Task A", "Task B"],
        "completion_rate": 60,
        "efficiency": "You were very efficient with your time today. You completed 2 high value tasks.",
        "summary": "Today, 3 out of 5 tasks were completed, demonstrating focus and progress, while incomplete tasks highlight areas for better time management. Key actions for tomorrow are clearly identified to maintain momentum.",
        "strengths": ["Focused on high-priority tasks", "Maintained consistent workflow"],
        "areas_to_improve": ["Better time estimation", "Avoid distractions"],
        "lessons_learned": ["Break larger tasks into smaller actionable steps"],
        "next_steps": ["Prioritize Task A first thing tomorrow", "Set 25-minute focused work intervals"],
        "motivation": "Completing tasks today builds momentum for tomorrow",
        "affirmation": "You are making steady progress towards your goals"
    }
    """
    reminders = retrieve_reminders()

    openai.api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "system", "content": prompt + "\n"},
            {"role": "user", "content": f"Here is the list of reminders for {date.today()}:\n" + reminders + "\n"}
        ]
    )  
    content = response.choices[0].message.content
    if content is None:
        raise ValueError("No content returned from OpenAI response.")

    return json.loads(content)
