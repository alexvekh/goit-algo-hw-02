from queue import Queue
import msvcrt  # For keyboard input

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
  queue = Queue()
  print("Press [Tab] for generate new request, [Space] - for proceess, [Esc] - exit   ")

  while True:

    if msvcrt.kbhit():  # Check if a key is pressed
      key = msvcrt.getch().decode()

      if key == chr(9):  # Check for Tab key
        generate_request()

      if key == chr(32):
        process_request()
        

      elif key == chr(27):  # Check for escape (ESC key has ASCII code 27)
        print("Bye-bye")
        break

if __name__ == "__main__":
    main()