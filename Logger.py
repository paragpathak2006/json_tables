""" Logger Class """
class Logger:
    log_enabled = False

    @staticmethod
    def log(message: str):
        if Logger.log_enabled:
            print(message)

    @staticmethod
    def error(message: str):
        if Logger.log_enabled:
            print(f"ERROR: {message}")

    # pass

