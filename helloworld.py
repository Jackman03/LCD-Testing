import time
import Driver as LCD
from datetime import datetime
LCD.setup()
#Clear screen 
LCD.clear()

while True:

	LCD.write("Hello, world!",LCD.LINE_1)


