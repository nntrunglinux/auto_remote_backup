from pydantic import BaseSettings


class Setting(BaseSettings):
    PGHOST: str = ""
    PGPORT: int = 0
    PGDATABASE: str = ""
    PGUSER: str = ""
    PGPASSWORD: str = ""
    BACKUP_DIR: str = ""

    SOURCE_USER: str = ""
    SOURCE_PASSWORD: str = ""
    SOURCE_IP: str = ""
    SOURCE_FOLDER_PATH: str = ""

    class Config:
        env_file = ".env"