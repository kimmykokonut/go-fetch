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
  print_greeting()
  store = {}
  while True:
    try:
      command = input("> ").strip()
      if not command:
        continue

      parts = command.split(maxsplit=2)
      cmd = parts[0].lower()
      if cmd == 'put':
        if len(parts) < 3:
          print("Invalid syntax.")
          continue
        key, value = parts[1], parts[2]
        store[key] = value
        print('ok')
      elif cmd == 'fetch':
        if len(parts) < 2:
          print("Invalid syntax.")
          continue
        key = parts[1]
        if key in store:
          print(store[key])
        else:
          print('Value not found')
      elif cmd == 'exit':
        print('Bye!')
        break
      else:
        print('Unknown command. Known commands are: put, fetch, exit.')
    except (EOFError, KeyboardInterrupt):
      break

if __name__ == '__main__':
  main()
