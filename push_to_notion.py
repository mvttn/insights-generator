import os 
from notion_client import Client
from dotenv import load_dotenv
from get_daily_insights import get_daily_insights

load_dotenv()
insights = get_daily_insights()

def title(text):
    return {
        "object": "block",
        "type": "heading_1",
        "heading_1": {"rich_text": [{"text": {"content": text}}]}
    }

def heading(text):
    return {
        "object": "block",
        "type": "heading_2",
        "heading_2": {"rich_text": [{"text": {"content": text}}]}
    }

def paragraph(text):
    return {
        "object": "block",
        "type": "paragraph",
        "paragraph": {"rich_text": [{"text": {"content": text}}]}
    }

def bullet(text):
    return {
        "object": "block",
        "type": "bulleted_list_item",
        "bulleted_list_item": {"rich_text": [{"text": {"content": text}}]}
    }

def todo(text, checked=False):
    return {
        "object": "block",
        "type": "to_do",
        "to_do": {
            "rich_text": [{"text": {"content": text}}],
            "checked": checked
        }
    }

def divider():
    return {
        "object": "block",
        "type": "divider",
        "divider": {}
    }

# Construct Notion blocks from insights
blocks = []

blocks.append(title("📅 " + insights["date"]))

blocks.append(heading("🧠 Summary"))
blocks.append(paragraph(insights["summary"]))

blocks.append(divider())

blocks.append(heading("📊 Performance"))
blocks.append(paragraph(f"Completion rate: {insights['completion_rate']}%"))
blocks.append(paragraph(f"Efficiency: {insights['efficiency']}"))


blocks.append(divider())

blocks.append(heading("✅ Completed Tasks"))
if insights["completed_tasks"]:
    for task in insights["completed_tasks"]:
        blocks.append(todo(task, checked=True))
else:
    blocks.append(paragraph("No tasks completed today."))

blocks.append(heading("❌ Incomplete Tasks"))
for task in insights["incomplete_tasks"]:
    blocks.append(todo(task, checked=False))

blocks.append(divider())

blocks.append(heading("💪 Strengths"))
for item in insights["strengths"]:
    blocks.append(bullet(item))

blocks.append(divider())


blocks.append(heading("⚠️ Areas to Improve"))
for item in insights["areas_to_improve"]:
    blocks.append(bullet(item))

blocks.append(divider())


blocks.append(heading("📘 Lessons Learned"))
for item in insights["lessons_learned"]:
    blocks.append(bullet(item))

blocks.append(divider())


blocks.append(heading("🔜 Next Steps"))
for step in insights["next_steps"]:
    blocks.append(todo(step, checked=False))

blocks.append(divider())


blocks.append(heading("🔥 Motivation"))
blocks.append(paragraph(insights["motivation"]))

blocks.append(divider())

blocks.append(heading("🧘 Affirmation"))
blocks.append(paragraph(insights["affirmation"]))

blocks.append(divider())


# Push to Notion
notion = Client(auth=os.getenv("NOTION_API_KEY"))
DATABASE_ID = os.getenv("DATA_SOURCE_ID")


response = notion.pages.create(
    parent={"database_id": DATABASE_ID},
    properties={
        "Date": {
            "title": [
                {"text": {"content": insights["date"]}}
            ]
        },
        "Completion Rate": {
            "number": insights["completion_rate"]
        },
        "Summary": {
            "rich_text": [
                {"text": {"content": insights["summary"]}}
            ]
        }
    },
    children=blocks     
)
