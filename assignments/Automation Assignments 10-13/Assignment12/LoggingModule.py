import logging
import time

def logg(strmsg):
    logging.basicConfig(filename=f"ProcessInfoLog-{time.strftime('%Y-%m-%d_%H-%M-%S')}.log", level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    logger = logging.getLogger(__name__)
    
    # logger.info("Logging Activity is Starting.............")
    logger.info(strmsg)
