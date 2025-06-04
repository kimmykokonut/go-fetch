def print_greeting():
  print("""
        ============================
        Welcome to Go Fetch!

        Here are the rules:
        1. Save a key-value pair:
          put <key> <value>
        2. Retrieve the value of a key:
          fetch <key>
        3. Exit the program:
          exit

        Example:
          > put favorite_color purple
          (response: ok)
          > fetch favorite_color
          (response: purple)

        Have fun!
        =============================
        """)

def main():
  # display welcome message
  print_greeting()
  # initialize empty dir to store k-v pairs
  # temp storage-session based, cleared when exit
  store = {}
  # main progam loop, goes until 'exit'
  while True:
    try:
      # set up command line
      command = input("> ").strip() #remove lead/trail whitespace
      # skips empty inputs (empty enter)
      if not command:
        continue
      # split input into parts
      parts = command.split(maxsplit=2)
      # first word (put), make lowercase
      cmd = parts[0].lower()
      # > put key value  --> if exist, overwrite. response: ok
      if cmd == 'put':
        # check if key & value
        if len(parts) < 3:
          print("Invalid syntax.")
          continue
        key, value = parts[1], parts[2]
        # store in dict. if exists, overwritten.
        store[key] = value
        print('ok')
      # > fetch key --> return value or 'value not found'
      elif cmd == 'fetch':
        # check key is provided
        if len(parts) < 2:
          print("Invalid syntax.")
          continue
        key = parts[1]
        if key in store:
          print(store[key])
        else:
          print('Value not found')
      # > exit ---> return 'Bye! and exit
      elif cmd == 'exit':
        print('Bye!')
        break # exit loop
      # handle unknown commands
      else:
        print('Unknown command. Known commands are: put, fetch, exit.')
    # handle program interruption (Ctrl+C) or EOF (Ctrl+D)
    except (EOFError, KeyboardInterrupt):
      break

if __name__ == '__main__':
  main()
