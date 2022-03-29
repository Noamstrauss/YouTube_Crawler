import logging.handlers
import sys
# Change root logger level from WARNING (default) to NOTSET in order for all messages to be delegated.
logging.getLogger().setLevel(logging.NOTSET)

# Add stdout handler, with level INFO
console = logging.StreamHandler(sys.stdout)
console.setLevel(logging.INFO)
formater = logging.Formatter('%(name)-13s: %(levelname)-8s %(message)s')
console.setFormatter(formater)
logging.getLogger().addHandler(console)

# Add file rotating handler, with level DEBUG
# rotatingHandler = logging.handlers.RotatingFileHandler(filename='logger/user.log', backupCount=5)
# rotatingHandler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# rotatingHandler.setFormatter(formatter)
# logging.getLogger().addHandler(rotatingHandler)

log = logging.getLogger("app." + __name__)