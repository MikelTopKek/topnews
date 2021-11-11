import os
from pathlib import Path

from dotenv import load_dotenv


def load_env():
    project_root = Path(__file__).parent.parent
    if os.getenv('environment_type') == 'local':
        env_file_path = "env/.env.local"
    else:
        env_file_path = "env/.env.example"

    dotenv_path = os.path.join(project_root, env_file_path)

    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    else:
        raise FileNotFoundError(f'Env file not found: {dotenv_path}')
