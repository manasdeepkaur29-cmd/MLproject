import logging
import os
from datetime import datetime

# 1. Create a unique file name based on the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Define the path where the 'logs' folder will be created
logs_path = os.path.join(os.getcwd(), "logs")

# 3. Create the directory if it doesn't already exist
os.makedirs(logs_path, exist_ok=True)

# 4. Combine the folder path and file name to get the full file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# 5. Configure the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

