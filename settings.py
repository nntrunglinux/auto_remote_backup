from pydantic import BaseSettings


class Setting(BaseSettings):
    HOST: str = ""
    PORT: int = 0
    DATABASE: str = ""
    USER: str = ""
    PASSWORD: str = ""
    BACKUP_DIR: str = ""
    FILESTORE_PATH: str = ""

    class Config:
        env_file = ".env"