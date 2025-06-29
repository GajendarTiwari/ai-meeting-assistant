import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))

def send_task_emails(tasks):
    if not tasks:
        print("❌ No tasks to send.")
        return

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            print("📨 Preparing to send task emails...")

            for name, task in tasks.items():
                if not isinstance(task, (str, list)):
                    print(f"⚠️ Skipping invalid task entry: {name}: {task}")
                    continue

                # Join list of tasks if needed
                task_str = "\n- " + "\n- ".join(task) if isinstance(task, list) else task

                # Replace with actual employee email mapping
                to_email = f"{name.lower().replace(' ', '')}@example.com"  # Placeholder email

                msg = MIMEText(f"Hello {name},\n\nHere are your assigned tasks:\n{task_str}\n\nBest,\nAI Meeting Assistant")
                msg["Subject"] = "Your Meeting Tasks"
                msg["From"] = EMAIL
                msg["To"] = to_email

                try:
                    server.sendmail(EMAIL, [to_email], msg.as_string())
                    print(f"✅ Email sent to {name} ({to_email})")
                except Exception as e:
                    print(f"❌ Failed to send email to {name}: {e}")
    except Exception as e:
        print(f"❌ Email sending failed: {e}")
