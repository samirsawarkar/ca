#!/usr/bin/env python3
import os
import sys

def process_command(command):
    if "make a file" in command:
        filename = command.split()[-1]
        os.system(f"touch {filename}")
        print(f"Created file: {filename}")
    elif "make a directory" in command:
        dirname = command.split()[-1]
        os.system(f"mkdir {dirname}")
        print(f"Created directory: {dirname}")
    else:
        print("Command not recognized.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
        process_command(user_input)
    else:
        print("Usage: ca <command>")
