from pathlib import Path
from datetime import datetime
from reportlab.pdfgen import canvas
import markdown2

class ReportGenerator:
    def __init__(self, config):
        self.output_dir = Path(config["daily_report"]["output_dir"]).expanduser()
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.gen_pdf = config["daily_report"]["generate_pdf"]

    def generate(self):
        today = datetime.now().strftime("%Y-%m-%d")
        md_path = self.output_dir / f"daily_report_{today}.md"

        md_content = f"""# 工作日报 {today}

## 📌 今日完成
- 文件自动整理完成
- 系统巡检完成
- 邮箱未读汇总完成

## 📋 待办事项
- 待安排

## ⚠️ 异常提醒
- 无

## 🚀 明日计划
- 继续自动办公任务
"""

        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_content)

        pdf_path = None
        if self.gen_pdf:
            pdf_path = self.output_dir / f"daily_report_{today}.pdf"
            c = canvas.Canvas(str(pdf_path))
            c.setFont("Helvetica", 12)
            c.drawString(50, 800, f"OpenClaw 工作日报 {today}")
            c.drawString(50, 780, "自动生成")
            c.save()

        return {"markdown": str(md_path), "pdf": str(pdf_path) if pdf_path else None}
