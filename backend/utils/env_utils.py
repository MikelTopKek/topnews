import os
from pathlib import Path

from dotenv import load_dotenv


def load_env():
    project_root = Path(__file__).parent.parent
    env_file_path = os.getenv('environment_file_path')

    dotenv_path = os.path.join(project_root, env_file_path)

    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    else:
        raise FileNotFoundError(f'Env file not found: {dotenv_path}')
