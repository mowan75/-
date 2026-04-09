import os
import shutil
from pathlib import Path

class FileOrganizer:
    def __init__(self, config):
        self.watch_paths = [Path(p).expanduser() for p in config["file_organizer"]["watch_paths"]]
        self.target_root = Path(config["file_organizer"]["target_root"]).expanduser()

    def organize(self):
        log = []
        for folder in self.watch_paths:
            if not folder.exists():
                continue
            for item in folder.iterdir():
                if item.is_file():
                    dest_dir = self._get_category_dir(item.suffix.lower())
                    dest_dir.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(item), dest_dir / item.name)
                    log.append(f"已归档: {item.name} → {dest_dir}")
        return log

    def _get_category_dir(self, ext):
        if ext in [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"]:
            return self.target_root / "Images"
        if ext in [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".md", ".txt"]:
            return self.target_root / "Documents"
        if ext in [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"]:
            return self.target_root / "Archives"
        if ext in [".mp4", ".mov", ".avi", ".mkv", ".flv"]:
            return self.target_root / "Videos"
        return self.target_root / "Others"
