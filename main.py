import sys
import os

def main():
    known_cmd = {"echo", "exit", "type"}
    paths = os.getenv("PATH").split(":")

    while True:
        sys.stdout.write("$ ")
        command = input()
        command_args = command.split()

        if command.startswith("type"):
            newkey = command_args[1]

            if newkey in known_cmd:
                print(f"{newkey} is a shell builtin")
            else:
                found_cmd = False
                for path in paths:
                    abs_path = os.path.join(path, newkey)
                    if os.path.exists(abs_path):
                        print(f"{newkey} is {abs_path}")
                        found_cmd = True
                        break
                if not found_cmd:
                    print(f"{newkey} not found")

        elif command.startswith("echo"):
            print(' '.join(command_args[1:]))

        elif command.lower() == "exit 0":
            break

        else:
            found = False
            if os.path.exists(command_args[0]):
                os.system(f"{command_args[0]} {' '.join(command_args[1:])}")
                found = True
            if not found:
                print(f"{command_args[0]}: command not found")

        sys.stdout.flush()

if __name__ == "__main__":
    main()
