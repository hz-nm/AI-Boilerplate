from loguru import logger
from datetime import datetime

class LoggerService:
    def __init__(self, service_name: str = "Application"):
        self.service_name = service_name

    def get_date(self) -> str:
        # Format current date and time like the JavaScript version: "DD/MM/YYYY, hh:mm:ss AM/PM"
        return datetime.now().strftime('%d/%m/%Y, %I:%M:%S %p')

    def message_parser(self, message) -> str:
        # Convert non-string message to a JSON-like string representation
        if not isinstance(message, str):
            return str(message)
        return message

    def log(self, message):
        logger.info(f"{self.get_date()} LOG [{self.service_name}] {self.message_parser(message)}")

    def error(self, message):
        logger.error(f"{self.get_date()} ERR [{self.service_name}] {self.message_parser(message)}")

    def debug(self, message):
        logger.debug(f"{self.get_date()} DEBUG [{self.service_name}] {self.message_parser(message)}")