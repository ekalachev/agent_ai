from src.agent import run_agent


def main():
    print("🔹 DeepSeek Agent (terminal mode). Type Ctrl-C or 'exit' to quit.\n")
    try:
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() in ("exit", "quit"):
                print("Goodbye!")
                break
            print(run_agent(user_input, 'default-session'))
    except KeyboardInterrupt:
        print("\nInterrupted. Goodbye!")


if __name__ == "__main__":
    main()
