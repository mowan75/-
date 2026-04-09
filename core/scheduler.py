import schedule
import time
from core.logger import Logger

class Scheduler:
    def __init__(self, assistant):
        self.assistant = assistant

    def start(self):
        schedule.every().day.at("18:00").do(self.assistant.organize_files)
        schedule.every().day.at("20:00").do(self.assistant.generate_daily_report)
        schedule.every(60).minutes.do(self.assistant.monitor_system)
        schedule.every(30).minutes.do(self.assistant.check_emails)

        Logger.info("定时任务已启动：18:00整理文件 | 20:00生成日报 | 每小时巡检")
        while True:
            schedule.run_pending()
            time.sleep(1)
