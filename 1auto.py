from queue import Queue

count = 0
queue = Queue()

def generate_request():
  global count
  count +=1
  new_request = f"request_{count}"
  queue.put(new_request)
  print("Came new request:", new_request, "- In the queue now ", queue.qsize(), " requests.")

def process_request():
    if not queue.empty():
        request = queue.get()
        print("Processed request:", request, "- In the queue stay ", queue.qsize(), " requests.")
    else:
        print("No requests in queue.")
 
def main():
  while count < 10000:
      generate_request()
      process_request()

if __name__ == "__main__":
    main()