# Daily Insights Generator

A **personal productivity and reflection automation tool** that retrieves todos from Apple Reminders, analyzes daily performance, generates insights, and pushes them to Notion. Designed for high performers, this pipeline helps track progress, identify areas for improvement, and maintain momentum on high-impact tasks.

---

## Features

- **Retrieve Apple Reminders**: Pulls completed and incomplete tasks from system (e.g., EventKit on macOS).  
- **Generate insights**: Uses OpenAI's ChatGPT to produce a structured end-of-day analysis, including completion rate, strengths, areas to improve, lessons learned, next steps, motivation, and affirmations.  
- **Generate Tailored Journal Prompts**: Uses ChatGPT to produce tailored journal prompts for daily reflection.
- **Push to Notion**: Automatically adds daily insights to a Notion database for easy review and tracking.  
- **Automated scheduling**: Run the pipeline daily using cron, with `caffeinate` support to keep your Mac awake while closed.  
- **Logging**: Timestamped logs capture each step of the pipeline for easy debugging.

---

## How It Works

1. **Retrieve Apple Reminders** – Reads daily tasks from a JSON file and categorizes them as completed or incomplete.  
2. **Generate insights** – Sends the task data to OpenAI to create a detailed performance reflection in JSON format.  
3. **Push to Notion** – Adds a page to Notion database with structured insights, journal prompts and a summary of the day.  
4. **Schedule daily execution** – Using cron and a shell script, the pipeline runs automatically at 11 PM daily.

---

## Technologies Used

- **Python** – For scripting the pipeline and processing JSON data.  
- **OpenAI API** – For generating insights and reflections automatically.  
- **Notion API** – For storing daily insights in a structured, trackable format.  
- **macOS Cron + Caffeinate** – For daily automated execution without needing the Mac awake manually.

---

## Output

- **Insights JSON** – Structured summary of completed/incomplete tasks, strengths, areas to improve, next steps, motivation, and affirmations.  
- **Notion page** – Automatically created in your Notion database for daily review.  
- **Logs** – Timestamped logs for each pipeline execution.

---

## Benefits

- Automates end-of-day reflection and productivity tracking.  
- Provides actionable insights to push the needle forward.  
- Helps maintain consistency, focus, and high performance.
- Having a daily audit for constant improvement and productivity.
