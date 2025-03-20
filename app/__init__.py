import os
import sys
import cmd
import logging
import pandas as pd
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()

class App(cmd.Cmd):
    prompt = ">>> "  # REPL prompt

    def __init__(self):
        super().__init__()
        self.logs_dir = 'logs'
        os.makedirs(self.logs_dir, exist_ok=True)
        self.configure_logging()
        self.settings = self.load_environment_variables()

        # ✅ Load state data
        self.state_df = self.load_state_data()
        if self.state_df is not None:
            print("✅ State data loaded successfully!")
        else:
            print("⚠️ Warning: State data could not be loaded.")

    ### ✅ Arithmetic Operations ###
    def do_add(self, args):
        """Usage: add x y - Perform addition"""
        try:
            x, y = map(float, args.split())
            result = x + y
            print(f"Result: {result}")
        except Exception:
            print("⚠️ Invalid input. Usage: add x y")

    def do_subtract(self, args):
        """Usage: subtract x y - Perform subtraction"""
        try:
            x, y = map(float, args.split())
            result = x - y
            print(f"Result: {result}")
        except Exception:
            print("⚠️ Invalid input. Usage: subtract x y")

    def do_multiply(self, args):
        """Usage: multiply x y - Perform multiplication"""
        try:
            x, y = map(float, args.split())
            result = x * y
            print(f"Result: {result}")
        except Exception:
            print("⚠️ Invalid input. Usage: multiply x y")

    def do_divide(self, args):
        """Usage: divide x y - Perform division"""
        try:
            x, y = map(float, args.split())
            if y == 0:
                print("❌ Error: Division by zero")
                return
            result = x / y
            print(f"Result: {result}")
        except Exception:
            print("⚠️ Invalid input. Usage: divide x y")

    ### ✅ State Lookup ###
    def load_state_data(self):
        """Load state data from CSV file or environment variables."""
        csv_path = os.getenv("STATE_CSV", "data/states.csv")

        if os.path.exists(csv_path):
            try:
                df = pd.read_csv(csv_path)
                df.columns = df.columns.str.strip()  # Remove any whitespace in column names
                return df
            except Exception as e:
                logging.error(f"Error reading CSV file: {e}")
                return None
        else:
            logging.warning("State CSV file not found. Attempting to use environment variables.")
            return self.load_state_from_env()

    def load_state_from_env(self):
        """Load state data from environment variables if CSV is missing."""
        states = []
        for key, value in os.environ.items():
            if key.startswith("STATE_"):
                try:
                    name, abbr, capital, population = value.split(",")
                    states.append({"State": name, "Abbreviation": abbr, "Capital": capital, "Population": int(population)})
                except ValueError:
                    logging.warning(f"⚠️ Incorrect format for {key} in environment variables.")

        return pd.DataFrame(states) if states else None

    def do_state(self, args):
        """Usage: state <state_name_or_abbreviation> - Retrieve state info"""
        if not args:
            print("⚠️ Please provide a state name or abbreviation.")
            return

        state_name = args.strip().title()
        result = self.state_df[
            (self.state_df["State"].str.title() == state_name) |
            (self.state_df["Abbreviation"].str.upper() == state_name.upper())
        ]

        if not result.empty:
            state_info = result.iloc[0]
            print("\n🌎 State Information")
            print(f"State: {state_info['State']}")
            print(f"Abbreviation: {state_info['Abbreviation']}")
            print(f"Capital: {state_info['Capital']}")
            print(f"Population: {int(state_info['Population']):,}")  # Format population
            print("-" * 30)
        else:
            print(f"⚠️ No information found for '{state_name}'.")

    ### ✅ Command Handling ###
    def default(self, line):
        """Handle unknown commands and attempt state lookup or arithmetic commands."""
        line = line.strip()

        # ✅ Check if it's an arithmetic command
        if line.split()[0] in ["add", "subtract", "multiply", "divide"]:
            self.onecmd(line)
            return

        # ✅ Try running the `state` command if user enters a state name directly
        if self.state_df is not None:
            if line.title() in self.state_df["State"].values or line.upper() in self.state_df["Abbreviation"].values:
                self.do_state(line)
                return

        print(f"❌ Unknown command: {line}. Type 'menu' for options.")

    def do_menu(self, args):
        """Display the available calculator and state commands."""
        commands = {
            "add <x> <y>": "Perform addition",
            "subtract <x> <y>": "Perform subtraction",
            "multiply <x> <y>": "Perform multiplication",
            "divide <x> <y>": "Perform division",
            "state <state_name>": "Retrieve state information",
            "menu": "Show this command menu",
            "exit": "Exit the calculator",
        }

        print("\nAvailable Commands:")
        for command, description in commands.items():
            print(f" - {command}: {description}")

    ### ✅ Logging ###
    def configure_logging(self):
        log_file_path = os.path.join(self.logs_dir, "app.log")
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            handlers=[logging.StreamHandler(sys.stdout), logging.FileHandler(log_file_path, mode="a")]
        )
        logging.info(f"Logging initialized successfully! Logs saved in {log_file_path}")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    ### ✅ Exit ###
    def do_exit(self, args):
        """Usage: exit - Exit the application"""
        print("Exiting calculator...")
        logging.info("Application exited.")
        sys.exit(0)

    def start(self):
        """Start the REPL loop"""
        logging.info("Application started. Type 'exit' to exit.")
        print("Welcome to the Calculator App! Type 'menu' to see commands.")
        self.cmdloop()

if __name__ == "__main__":
    app = App()
    app.start()
