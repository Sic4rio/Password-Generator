import random
import string
import signal
from termcolor import colored

# Define colors using termcolor
SUCCESS_COLOR = 'green'
ERROR_COLOR = 'red'
RAINBOW_COLORS = [
    '\033[38;5;196m', '\033[38;5;202m', '\033[38;5;208m', '\033[38;5;214m',
    '\033[38;5;220m', '\033[38;5;226m', '\033[38;5;190m', '\033[38;5;154m',
    '\033[38;5;118m', '\033[38;5;82m', '\033[38;5;46m', '\033[38;5;47m',
    '\033[38;5;48m', '\033[38;5;49m', '\033[38;5;50m', '\033[38;5;51m',
    '\033[38;5;45m'
]

def center_text(text, width=80):
    return text.center(width)

def rainbow_banner(text):
    rainbow_text = ""
    for i, char in enumerate(text):
        rainbow_color = RAINBOW_COLORS[i % len(RAINBOW_COLORS)]
        rainbow_text += rainbow_color + char
    return rainbow_text + '\033[0m'

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    secure_password = ''.join(random.choice(characters) for _ in range(length))
    return secure_password

def signal_handler(signal, frame):
    print("\nExiting...")
    exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTSTP, signal_handler)

    banner = rainbow_banner(center_text("""
██████   █████  ███████ ███████ ██     ██  ██████  ██████  ██████       ██████  ███████ ███    ██ ███████ ██████   █████  ████████  ██████  ██████  
██   ██ ██   ██ ██      ██      ██     ██ ██    ██ ██   ██ ██   ██     ██       ██      ████   ██ ██      ██   ██ ██   ██    ██    ██    ██ ██   ██ 
██████  ███████ ███████ ███████ ██  █  ██ ██    ██ ██████  ██   ██     ██   ███ █████   ██ ██  ██ █████   ██████  ███████    ██    ██    ██ ██████  
██      ██   ██      ██      ██ ██ ███ ██ ██    ██ ██   ██ ██   ██     ██    ██ ██      ██  ██ ██ ██      ██   ██ ██   ██    ██    ██    ██ ██   ██ 
██      ██   ██ ███████ ███████  ███ ███   ██████  ██   ██ ██████       ██████  ███████ ██   ████ ███████ ██   ██ ██   ██    ██     ██████  ██   ██ 
                                                                                                                                                    
                                                                                                                                                    
		SICARIO - PYTHON PASSWORD GENERATOR | 24 
"""))

    print(colored(banner, 'yellow'))

    while True:
        try:
            password_length = int(input(colored("Please enter the length of the password you'd like to generate: ", 'red')))
            if password_length <= 0:
                print("Please enter a positive integer greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

    password = generate_password(password_length)
    print(colored(f"\nGenerated Secure Password: {password}", 'yellow'))

if __name__ == "__main__":
    main()
