from logging import *

LOG_FORMAT= '{lineno} -- {name} -- {asctime} -- {message}'
basicConfig(filename='logfile.log',level=DEBUG,filemode='w',style='{',format=LOG_FORMAT)

logger = getLogger('Geek')

# Advance Python -- Video-117 -- Default Logger is Root

logger.debug('This is Debug')
logger.info('This is Info')
logger.warning("This is Warning")
logger.error('This is Error')
logger.critical('This is Critical')
 