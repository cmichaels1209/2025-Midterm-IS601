# 2025-Midterm-IS601
 Project Overview
This is an advanced Python-based calculator featuring:

Command-Line Interface (REPL) for real-time interaction.
Arithmetic operations (Addition, Subtraction, Multiplication, and Division).
Calculation history management with Pandas.
State lookup functionality using CSV files or environment variables.
A plugin system to dynamically load additional features.
Comprehensive logging to track application events and errors.
Implementation of design patterns for scalable architecture.

Command Usage Examples
General REPL Commands:
>>> menu
Available Commands:
 - add <x> <y>: Perform addition
 - subtract <x> <y>: Perform subtraction
 - multiply <x> <y>: Perform multiplication
 - divide <x> <y>: Perform division
 - state <state_name>: Retrieve state information
 - history: View calculation history
 - clear_history: Clear calculation history
 - exit: Exit the calculator

Arithmetic Operations used:
>>> add 10 5
Result: 15.0

>>> subtract 20 8
Result: 12.0

>>> multiply 7 6
Result: 42.0

>>> divide 10 2
Result: 5.0

>>> divide 10 0
Error: Division by zero

Calculation History Management
bash
Copy
Edit
>>> history
Operation | Operand1 | Operand2 | Result
----------------------------------------
Add       | 10       | 5        | 15.0  
Subtract  | 20       | 8        | 12.0  
Multiply  | 7        | 6        | 42.0  
Divide    | 10       | 2        | 5.0  

>>> clear_history
Calculation history cleared.

State Lookup
>>> state NJ
🌎 State Information
State: New Jersey
Abbreviation: NJ
Capital: Trenton
Population: 9,288,994
------------------------------

>>> state Texas
🌎 State Information
State: Texas
Abbreviation: TX
Capital: Austin
Population: 30,000,000
------------------------------

Logging and Debugging
Logging is an essential part of the application for tracking events and debugging issues.

 Logging Features:
Log files are stored in the logs/ directory.
Different log levels (INFO, WARNING, ERROR) for monitoring.
Configurable log settings via environment variables.
 Log File Example (logs/app.log)
2025-03-19 22:31:05,918 - root - INFO - Logging initialized successfully! Logs saved in logs/app.log
2025-03-19 22:31:05,918 - root - INFO - Environment variables loaded.
2025-03-19 22:31:05,921 - root - INFO - Application started. Type 'exit' to exit

Design Patterns Used
This project follows best practices in software design by implementing multiple design patterns.

1. Facade Pattern - Simplified Interface for State Lookup
Where Used? load_state_data()
Why? It provides a single function to fetch state data from either CSV or environment variables.
2. Command Pattern - Organizing REPL Commands
Where Used? Arithmetic operations (AddCommand, SubtractCommand, etc.).
Why? Each operation is treated as a separate command class, making it modular and scalable.
3.  Factory Method Pattern - Dynamic Command Creation
Where Used? The REPL dynamically creates instances of command objects.
Why? It enables flexible command registration.
4.  Singleton Pattern - Managing Calculation History
Where Used? HistoryManager class.
Why? Ensures only one history instance exists at any time.
5. Strategy Pattern - Arithmetic Operations Selection
Where Used? Arithmetic operations (AddCommand, SubtractCommand, etc.).
Why? Allows dynamic selection of different operations.
✅ Development, Testing, and Best Practices
Testing and Code Quality
 Pytest Coverage: 90%+ test coverage using pytest.
 Pylint Compliance: Ensures PEP 8 coding standards.

