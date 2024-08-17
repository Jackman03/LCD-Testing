import Driver as LCD
import time
from datetime import datetime
LCD.setup()
LCD.clear()


try:
    while True:
        now = datetime.now()
        Curdate = str(now.strftime("%d-%m-%Y"))
        Curtime = str(now.strftime("%H:%M:%S"))
        LCD.write(Curdate,LCD.LINE_1)
        LCD.write(Curtime,LCD.LINE_2)
        time.sleep(1)
        
except KeyboardInterrupt:
    LCD.clear()
    print("LCD finished")
