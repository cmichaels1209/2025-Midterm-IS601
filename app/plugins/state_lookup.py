import os
import logging
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()

def load_state_data():
    """Load state data from environment variables into a dictionary."""
    states = {}

    for key, value in os.environ.items():
        if key.startswith("STATE_"):
            try:
                name, abbr, capital, population = value.split(",")
                states[abbr.upper()] = {
                    "name": name.title(),
                    "abbreviation": abbr.upper(),
                    "capital": capital.title(),
                    "population": int(population)
                }
            except ValueError:
                logging.warning(f"⚠️ Incorrect format for {key} in environment variables.")

    return states

def get_state_info(states, state_name):
    """Retrieve state information from environment variables."""
    state_name = state_name.strip().title()

    # Search by abbreviation
    if state_name.upper() in states:
        state_info = states[state_name.upper()]
    else:
        # Search by full name
        state_info = next((info for info in states.values() if info["name"] == state_name), None)

    if state_info:
        print("\n🌎 State Information")
        print(f"State: {state_info['name']}")
        print(f"Abbreviation: {state_info['abbreviation']}")
        print(f"Capital: {state_info['capital']}")
        print(f"Population: {state_info['population']:,}")  # Format population
        print("-" * 30)
    else:
        print(f"⚠️ No information found for '{state_name}'.")
