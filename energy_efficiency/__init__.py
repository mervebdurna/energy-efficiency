from dotenv import load_dotenv
from energy_efficiency.logger import logging
logging.info(f"Loading enviroment variable from .env file.")
load_dotenv()