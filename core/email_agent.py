import imaplib
import email
from email.header import decode_header

class EmailAgent:
    def __init__(self, config):
        self.accounts = config["email_accounts"]

    def fetch_unread(self):
        result = []
        for acc in self.accounts:
            try:
                mail = imaplib.IMAP4_SSL(acc["imap_host"], acc["imap_port"])
                mail.login(acc["user"], acc["password"])
                mail.select("INBOX")
                _, data = mail.search(None, "UNSEEN")
                unread = len(data[0].split())
                result.append({
                    "title": acc["title"],
                    "unread": unread,
                    "error": None
                })
                mail.logout()
            except Exception as e:
                result.append({
                    "title": acc["title"],
                    "unread": 0,
                    "error": str(e)
                })
        return result
