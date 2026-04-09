import datetime
import os
from pathlib import Path

LOG_DIR = Path(__file__).parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

class Logger:
    @staticmethod
    def _log(level, message):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_str = f"[{now}] [{level.upper()}] {message}"
        print(log_str)
        with open(LOG_DIR / "assistant.log", "a", encoding="utf-8") as f:
            f.write(log_str + "\n")

    @staticmethod
    def info(msg):
        Logger._log("info", msg)

    @staticmethod
    def warn(msg):
        Logger._log("warn", msg)

    @staticmethod
    def error(msg):
        Logger._log("error", msg)
