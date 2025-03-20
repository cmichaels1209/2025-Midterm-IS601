import cmd
from app.commands import CommandHandler
from app.history_manager import HistoryManager
from app.plugins.state_lookup import load_state_data, get_state_info

class CalculatorREPL(cmd.Cmd):
    prompt = "(calc) "

    def __init__(self):
        super().__init__()
        self.command_handler = CommandHandler()
        self.history_manager = HistoryManager()
        self.states = load_state_data()  # Load state data from CSV

    def do_menu(self, args):
        """List all available commands"""
        commands = [
            "add", "subtract", "multiply", "divide",
            "history", "clear_history", "logs", "clear_logs",
            "state", "exit"
        ]
        print("\nAvailable Commands:")
        for cmd in commands:
            print(f" - {cmd}")

    def do_state(self, args):
        """Retrieve state info by name or abbreviation"""
        if not args:
            print("⚠️ Please provide a state name or abbreviation.")
            return
        get_state_info(self.states, args)

    def do_exit(self, args):
        """Exit the calculator"""
        print("Exiting calculator...")
        return True

if __name__ == "__main__":
    CalculatorREPL().cmdloop()
