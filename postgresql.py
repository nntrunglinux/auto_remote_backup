import subprocess
from loguru import logger


class Postgre:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    def backup(self, backup_file_path):
        try:
            command = [
                "pg_dump",
                "--no-owner",
                f"--dbname=postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}",
                "--format=p",
                "--encoding=UTF8",
                f"--file={backup_file_path}",
            ]
            subprocess.run(command, check=True)
            logger.success("Backup database thanh cong")
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"Loi khi backup database: {e}")
            return False
