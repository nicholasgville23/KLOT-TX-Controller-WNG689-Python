import sys

def main():
    print("KLOT/WNG689 Transmitter Controller - Valparaiso, IN")
    while True:
        cmd = input("Enter command (on/off/status/exit): ").strip().lower()
        if cmd == "on":
            print("Transmitter ON")
        elif cmd == "off":
            print("Transmitter OFF")
        elif cmd == "status":
            print("Transmitter status: ON")  # Simulated
        elif cmd == "exit":
            print("Exiting controller.")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()