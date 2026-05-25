import time

while True:
    
    current_time = time.localtime()
    formatted_time = time.strftime("%I:%M:%S %p", current_time)
    
    print(formatted_time)
    time.sleep(1)