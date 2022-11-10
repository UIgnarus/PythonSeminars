
from datetime import datetime

def get_random():
    nowTime1 = datetime.now().microsecond
    nowTime2 = datetime.now().second + 1
    uniqueNum = (nowTime2 * nowTime1)**2
    return uniqueNum
print(get_random())