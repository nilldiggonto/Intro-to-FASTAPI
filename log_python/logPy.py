import logging
from logging import root
"""
DEBUG
INFO
WARNING
ERROR
CRITICAL

"""
#----------
def test():
    print('*'*20)
    level = logging.getLevelName(logging.getLogger().getEffectiveLevel())
    print(f'log level: {level}')
    print('----------')
    logging.debug('working with debug')
    print('----------')
    logging.info('some info here')
    print('----------')
    logging.warning('some kind of warning')
    print('---------------')
    logging.error('well its error')
    print('---------------')
    logging.critical('well well its critical')
    print('----------')

    print('*'*20)

test()

#-----------
print('-----------')

#warning 
rootlog = logging.getLogger()
print('Level '+ logging.getLevelName(logging.getLogger().getEffectiveLevel()))

#debug level
rootlog.setLevel(logging.DEBUG)
test()

#CREATING A FORMATTER FOR DEBUG
handler = logging.FileHandler('file.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
rootlog.addHandler(handler)
rootlog.setLevel(logging.DEBUG)
rootlog.debug('Debug running')
test()