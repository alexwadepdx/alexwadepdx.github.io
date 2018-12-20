# Baseball functions
import time
import random
import baseball


def stolen_base():
    stolen_base = False
    number = random.randint(1, 10)
    if number < 4:
        print("runner goes.......")
        time.sleep(3)
        safe_number = random.randint(1, 10)
        if safe_number < 4:
            time.sleep(3)
            print ("runner is safe!")
            stolen_base = True
        if safe_number > 3:
            time.sleep(3)
            print ("runner is out!")
        return stolen_base
