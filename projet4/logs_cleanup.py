import os
from datetime import datetime, timedelta

log_dir = '/var/log'
retention_period = 10  # jours


def cleanup_logs(directory, retention):
    now = datetime.now()
    cutoff_date = now - timedelta(days=retention)
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        file_stat = os.stat(file_path)
        file_mod_date = datetime.fromtimestamp(file_stat.st_mtime)
        if os.path.isfile(file_path) and file_mod_date < cutoff_date:
            print(f"Suppression : {file_path}")
            os.remove(file_path)


if __name__ == "__main__":
    cleanup_logs(log_dir, retention_period)

