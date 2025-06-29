import smtplib
from email.message import EmailMessage
from config.settings import SMTP_USER, SMTP_PASS

def send_task_email(to_email, tasks, subject="Meeting To-Do Tasks"):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = SMTP_USER
    msg['To'] = to_email
    msg.set_content(f"Hello,\n\nHere are your tasks from today's meeting:\n\n{tasks}\n\nBest,\nAI Assistant Bot")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SMTP_USER, SMTP_PASS)
            smtp.send_message(msg)
            print(f"[📧] Email sent to {to_email}")
    except Exception as e:
        print(f"[⚠️] Failed to send email to {to_email}: {e}")
