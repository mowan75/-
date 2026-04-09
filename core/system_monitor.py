import psutil

class SystemMonitor:
    def __init__(self, config):
        self.disk_th = config["system_monitor"]["disk_alert_threshold"]
        self.mem_th = config["system_monitor"]["mem_alert_threshold"]

    def check(self):
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent
        net = psutil.net_io_counters()
        alerts = []

        if mem > self.mem_th:
            alerts.append(f"内存占用过高: {mem}%")
        if disk > self.disk_th:
            alerts.append(f"磁盘占用过高: {disk}%")

        return {
            "cpu": cpu,
            "memory": mem,
            "disk": disk,
            "net_sent": net.bytes_sent,
            "net_recv": net.bytes_recv,
            "alerts": alerts
        }
