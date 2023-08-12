import subprocess
from loguru import logger


class SCP:
    def __init__(self, user, password, ip):
        self.user = user
        self.password = password
        self.ip = ip

    def backup(self, source_folder_path, dest_folder_path):
        try:
            command = [
                f'sshpass -p "{self.password}" scp -r {self.user}@{self.ip}:{source_folder_path} {dest_folder_path}'
            ]
            subprocess.run(command, check=True)
            logger.success("Backup filestore thanh cong")
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"Loi khi backup database: {e}")
            return False