# Learn logging in python

# Levels in logging 
1. DEBUG
2. INFO
3. WARNING
4. ERROR
5. CRITICAL

# Code 
## Simple Way (no / independent modules involved)
```Python 
import logging

logging.basicConfig(
    filename='path_to_logfile.log',
    level=logging.DEBUG,
    formatter='%(levelname)s: %(asctime)s: %(message)s'
)

first_name = 'Pinaki'
last_name = 'Brahma'
domain = 'walmart.com'
logging.debug(f"email: {first_name}.{last_name}@{domain}")
```

## Best Practice (dependency across multiple modules involved)
```Python
# module - basics.py
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s: %(asctime)s: %(funcName)s: %(message)s')

file_handler = logging.FileHandler('path_to_log_basics.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

## code starts here
first_name = 'Pinaki'
last_name = 'Brahma'
domain = 'walmart.com'
logging.debug(f"email: {first_name}.{last_name}@{domain}")

# module - utils.py
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s: %(asctime)s: %(message)s')

file_handler = logging.FileHandler('path_to_log_utils.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

## code starts here
empl_id = 'prb000j'
dept = 'GRT'
logger.debug(f"Cost Func: {dept}")

```