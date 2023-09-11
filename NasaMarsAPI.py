import threading
import requests
import time

# Global list to store the API data
global_list = []

# self generated api
api = "4bOaDypa4mq2rEacKbJBXh4jd1focojzCi6eJtsz"

lock=threading.Lock()

# Function to make API request and process the response
def worker(earth_date, thread_id):
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={earth_date}&api_key={api}"
    response = requests.get(url).json()
    time.sleep(2)  # delay
    photos = response['photos']
    for photo in photos:
        #using lock to prevent data corruption during multithreading concurrency
        with lock:
            img_url = photo["img_src"]
            earth_date = photo["earth_date"]
            global_list.append(f"{img_url}, {earth_date}, Thread-{thread_id}")

# thread creation
threads = []
t1 = threading.Thread(target=worker, args=("2018-01-01/2018-01-10", 1))
threads.append(t1)
t2 = threading.Thread(target=worker, args=("2019-01-01/2019-01-10", 2))
threads.append(t1)
t3 = threading.Thread(target=worker, args=("2020-01-01/2020-01-10", 3))
threads.append(t1)

# Start all threads
t1.start()
t2.start()
t3.start()

# thread join (wait)
t1.join()
t2.join()
t3.join()

# print list
for item in global_list:
    print(item)
