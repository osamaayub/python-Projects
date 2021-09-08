#pip install plyer
import time
from plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(
            title="Take a Class at 11 am",
            message=" I have  a  HCI Class",
        )
        time.sleep(15)