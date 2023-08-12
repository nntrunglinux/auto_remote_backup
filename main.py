import sys
import os
import shutil

from datetime import datetime
from rocketry import Rocketry
from loguru import logger

from postgresql import Postgre
from scp import SCP
from settings import Setting


settings = Setting()
postgre = Postgre(
    host=settings.PGHOST,
    port=settings.PGPORT,
    database=settings.PGDATABASE,
    user=settings.PGUSER,
    password=settings.PGPASSWORD,
)
scp = SCP(
    user=settings.SOURCE_USER,
    password=settings.SOURCE_PASSWORD,
    ip=settings.SOURCE_IP
)
app = Rocketry()
BACKUP_DATETIME_FORMAT = "%Y.%m.%d.%H.%M.%S"


# def backup_filestore(current_backup_dir):
#     try:
#         filestore_new_dir = current_backup_dir + r"filestore"
#         shutil.copytree(settings.FILESTORE_PATH, filestore_new_dir)
#         logger.success("Backup filestore thanh cong")
#         return True
#     except Exception as e:
#         logger.error(f"Loi khi backup filestore: {e}")
#         return False


@app.task("every 10 minute")
def perform_backup():
    now_str = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    logger.info(f"------------------------Backup {now_str}------------------------")
    current_backup_dir = settings.BACKUP_DIR + "backup/"
    # if os.path.exists(current_backup_dir):
    #     shutil.rmtree(current_backup_dir)
    #
    # os.mkdir(current_backup_dir)
    # backup_file_path = current_backup_dir + r"dump.sql"
    # is_backup_success = postgre.backup(backup_file_path)
    # if is_backup_success:
    #     scp.backup(settings.SOURCE_FOLDER_PATH, current_backup_dir)
    scp.backup(settings.SOURCE_FOLDER_PATH, current_backup_dir)


def main():
    logger.info(f"Bat dau thuc thi backup")
    # app.run()
    perform_backup()

    logger.info(f"Ket thuc thuc thi backup")
    sys.exit()


if __name__ == "__main__":
    main()
