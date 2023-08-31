import logging

logger = logging.getLogger('ConsoleLogger')

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# console_handler = logging.StreamHandler()
DebugFileHandler = logging.FileHandler('Debugs.log','w')
ErrorFileHandler = logging.FileHandler('Error.log','w')
CriticalFileHandler = logging.FileHandler('Warnings.log','w')

# console_handler.setFormatter(formatter)
# console_handler.setLevel(logging.INFO)

DebugFileHandler.setFormatter(formatter)
DebugFileHandler.setLevel(logging.DEBUG)

ErrorFileHandler.setFormatter(formatter)
ErrorFileHandler.setLevel(logging.ERROR)

CriticalFileHandler.setFormatter(formatter)
CriticalFileHandler.setLevel(logging.CRITICAL)

# logger.addHandler(console_handler)
logger.addHandler(DebugFileHandler)
logger.addHandler(ErrorFileHandler)
logger.addHandler(CriticalFileHandler)



logger.debug("This message will be printed to the console")
logger.info("This message will be printed to the console")
logger.warning("This message will be printed to the console")
logger.error("This message will be printed to the console")
logger.critical("This message will be printed to the console")

