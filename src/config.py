import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

BUDGET_FILENAME = os.getenv('BUDGET_FILENAME') or 'expences.csv'
BUDGET_FILE_PATH = os.path.join(dirname, '..', 'data', BUDGET_FILENAME)
