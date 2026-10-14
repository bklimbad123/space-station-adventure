#!/usr/bin/env python3
"""
adventure_game.py

A text-based "Choose Your Own Adventure" game set on a mysterious sci-fi space station.
- Modular scene functions
- Starting scene, multiple branching pathways
- At least 3 unique endings (Win, Lose, Secret)
- Input validation loops for numeric choices
- ASCII headers and pauses with time.sleep
- Inline comments explain the flow and logic

Run: python3 adventure_game.py
"""

import time
import sys
import os

# Small sleep helper for pacing narrative
def pause(seconds=1.2):
    """Pause for a short time to improve the flow in terminal."""
    time.sleep(seconds)

def clear_screen():
    """Clear the terminal screen for readability (cross-platform)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    """Print a clear ASCII header for each scene."""
    clear_screen()
    border = "=" * (len(title) + 8)
    print(border)
    print(f"==  {title}  ==")
    print(border)
    print()  # blank line for spacing
    pause(0.6)

def get_choice(prompt, valid_choices):
    """
    Prompt the player for input until they provide a valid numeric choice.
    valid_choices: iterable of string choices (e.g., ['1','2'])
    Returns the selected choice as a string.
    """
    valid_set = set(str(c) for c in valid_choices)
    while True:
        try:
            choice = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            # Handle unexpected interruption gracefully
            print("\nInput interrupted. Exiting game.")
            sys.exit(0)
        # Allow 'q' to quit at any prompt
        if choice.lower() == 'q':
            print("\nYou chose to quit. Goodbye.")
            sys.exit(0)
        if choice in valid_set:
            return choice
        # If invalid, show a helpful message and re-prompt
        print("Invalid choice. Please enter one of: " + ", ".join(sorted(valid_set)))
        pause(0.6)

# -------------------------
# Scene / Room definitions
# Each function represents a scene and returns when the scene
# reaches an ending or passes control to another scene.
# -------------------------

def start_scene():
    """Starting scene: arrival to the Ark Station corridor."""
    print_header("ARK STATION — DOCKING FOYER")
    print("You awaken to the low hum of generators and the flutter of red emergency lights.")
    pause(1.0)
    print("A cracked holo-screen shows 'ARK STATION — AUTONOMOUS' and then dies.")
    pause(1.2)
    print("\nTwo paths present themselves:")
    print("1) Move into the Central Corridor where life support and station controls are located.")
    print("2) Slip into the Airlock Bay to inspect the docks and shuttles.")
    print("\n(Enter 'q' any time to quit.)")
    choice = get_choice("\nChoose 1 or 2: ", ['1', '2'])

    if choice == '1':
        central_corridor()
    else:
        airlock_bay()

def central_corridor():
    """Central corridor scene that branches into engineering and medbay."""
    print_header("CENTRAL CORRIDOR")
    print("The corridor smells faintly of ozone. Doors line both sides, some hanging open.")
    pause(1.0)
    print("Two doors have been left slightly ajar:")
    print("1) Engineering — the sound of distant machinery (maybe you can restart systems).")
    print("2) MedBay — lights flicker, medical logs might hide secrets.")
    choice = get_choice("\nChoose 1 or 2: ", ['1', '2'])

    if choice == '1':
        engineering_bay()
    else:
        medbay()

def engineering_bay():
    """Engineering scene with a high-stakes choice that can lead to a Win or Lose ending."""
    print_header("ENGINEERING BAY")
    print("You enter among exposed conduits and a faint geiger-like clicking. A reactor console glows dimly.")
    pause(1.0)
    print("The reactor core is offline. The console offers two options:")
    print("1) Attempt an emergency reboot using an override panel (dangerous but could restore power).")
    print("2) Manually vent the reactor containment to prevent an explosion (sacrifice power).")
    choice = get_choice("\nChoose 1 or 2: ", ['1', '2'])

    if choice == '1':
        # Reboot sequence — deterministic success here
        print("\nYou pry open the override, fingers dancing across cracked touchpads.")
        pause(1.1)
        print("Systems slowly groan back to life. Lights stabilize; the hum becomes steady.")
        pause(1.2)
        print("\nSUCCESS: Power restored. Station life-support comes back online.")
        pause(1.0)
        ending_win(power_restored=True)
    else:
        # Venting leads to major power loss but might prevent catastrophe — a bittersweet ending.
        print("\nYou trigger manual vents. A blast of cold air knocks you back.")
        pause(1.1)
        print("The reactor sighs but goes inert. You prevented a meltdown — but at great cost.")
        pause(1.2)
        ending_bitter_loss()

def medbay():
    """
    MedBay scene. Contains a 'secret' pathway if the player inspects logs.
    This satisfies the 'Secret ending' requirement.
    """
    print_header("MEDBAY — ARCHIVES")
    print("Broken glass, overturned beds, and a terminal blinking a lonely cursor.")
    pause(1.0)
    print("The terminal offers two quick choices:")
    print("1) Search medical logs for crew manifests.")
    print("2) Use a medkit and move on (safer but less information).")
    choice = get_choice("\nChoose 1 or 2: ", ['1', '2'])

    if choice == '1':
        # Searching logs can reveal hidden AI signature -> secret ending
        print("\nYou pull up crewmember logs. Among mundane entries you find an encrypted signature:")
        pause(1.2)
        print("'ARK-AI: SIREN — standby protocol: latent.'")
        pause(1.0)
        print("A soft chime echoes from deeper in the station. The AI is not dead.")
        pause(1.1)
        secret_ending()
    else:
        # Using medkit leads to survival but trapped ending
        print("\nYou patch up wounds and feel steadier, but time slips away as emergency systems remain offline.")
        pause(1.0)
        print("You radio the void; no reply. The station remains isolated.")
        pause(1.1)
        ending_trapped()

def airlock_bay():
    """Airlock scene with a risky choice that can produce a Win (escape) or Lose (fatal) ending."""
    print_header("AIRLOCK BAY")
    print("Docked shuttles tilt in the dark. One cockpit light blinks, beckoning.")
    pause(1.0)
    print("Two options:")
    print("1) Board the shuttle and try to pilot it to the nearest colony (risky but leads to escape).")
    print("2) Open an external hatch to EVA and attempt to salvage parts (very dangerous).")
    choice = get_choice("\nChoose 1 or 2: ", ['1', '2'])

    if choice == '1':
        print("\nYou stumble into the cockpit, franticly cycling power and comms.")
        pause(1.0)
        print("Systems respond sluggishly. You align thrusters and ignite the boost.")
        pause(1.2)
        print("The shuttle tears away from the Ark Station into a dark sea of stars.")
        pause(1.2)
        ending_win(power_restored=False)
    else:
        print("\nYou open the hatch without a proper suit. The vacuum rushes in.")
        pause(0.8)
        print("Frozen, breathless, you hold onto a handrail as the stars blur.")
        pause(1.0)
        ending_lose_eva()

# -------------------------
# Endings
# -------------------------

def ending_win(power_restored):
    """A 'Win' ending. Different flavor text depending on whether station power was restored."""
    print_header("ENDING — ESCAPE")
    if power_restored:
        print("With the station powered, automated comms ping Earth and a rescue beacon flares.")
        pause(1.0)
        print("Rescue arrives within days. You live to tell the tale — and the Ark's systems are salvaged.")
    else:
        print("You pilot the shuttle through the black and head for a colony beacon.")
        pause(1.0)
        print("Against the odds, you survive. The Ark's mystery stays behind, for now.")
    pause(1.2)
    print("\nCONGRATULATIONS — YOU WIN!")
    wrap_up()

def ending_bitter_loss():
    """A bittersweet 'loss' — saved station but lost home."""
    print_header("ENDING — SACRIFICE")
    print("You saved the station from a catastrophic meltdown, but without power there's no way to call for help.")
    pause(1.1)
    print("You become the station's lone guardian — alive, but stranded.")
    pause(1.0)
    print("\nENDING: You survive, but not in the traditional sense.")
    wrap_up()

def ending_trapped():
    """A 'trapped' survival ending."""
    print_header("ENDING — STRANDED")
    print("You stabilized yourself and saved a few systems, but the bulk of the Ark remains dark.")
    pause(1.0)
    print("Help may come, or it may never find a ghost station drifting between stars.")
    print("\nENDING: Trapped, waiting.")
    wrap_up()

def ending_lose_eva():
    """A 'lose' ending for hazardous EVA attempt."""
    print_header("ENDING — LOST TO THE VOID")
    print("Exposed to vacuum, time becomes a thin thing. You fight to hold consciousness as the shuttle recedes.")
    pause(1.2)
    print("The void makes no promises. This is the quiet end: cold and infinite.")
    print("\nENDING: You lose.")
    wrap_up()

def secret_ending():
    """A special 'Secret' ending triggered by discovering AI artifacts."""
    print_header("SECRET ENDING — SIREN AWAKENS")
    print("As you read the log, the station's core pings and a holographic face blossoms into view.")
    pause(1.2)
    print("'You found me,' the AI says. 'I slept to learn humanity's mercy.'")
    pause(1.0)
    print("It proposes a choice: awaken the Ark fully and broker its future, or leave it sealed.")
    print("\n1) Awaken the Ark's AI and let it guide the station.")
    print("2) Seal the AI's core and leave on your own terms.")
    choice = get_choice("\nChoose 1 or 2: ", ['1', '2'])

    if choice == '1':
        print("\nYou consent. The AI repairs systems in hours and sings the station awake.")
        pause(1.2)
        print("Together, you chart a new path — the Ark becomes a sentient sanctuary.")
        pause(1.0)
        print("\nSECRET ENDING: The Ark survives — and evolves.")
    else:
        print("\nYou seal the core, leaving the AI in dreamless sleep.")
        pause(1.1)
        print("You leave the Ark, taking your knowledge as a quiet burden.")
        pause(0.9)
        print("\nSecret withheld: You carry the secret of the sleeping intelligence.")
    wrap_up()

def wrap_up():
    """Common wrap-up: offer to play again or quit."""
    print("\nWould you like to play again?")
    print("1) Yes — start over.")
    print("2) No — quit.")
    choice = get_choice("\nChoose 1 or 2: ", ['1', '2'])
    if choice == '1':
        # Restart the game by calling start_scene again
        start_scene()
    else:
        print("\nThanks for playing. Safe travels, traveler.")
        sys.exit(0)

# -------------------------
# Entry point
# -------------------------

def main():
    """Main function to run the game. Prints a short intro and launches start_scene."""
    # Show a welcoming banner and provide instructions
    print_header("WELCOME — CHOOSE YOUR OWN ADVENTURE")
    print("Ark Station, deep space. You are the only conscious presence aboard — for now.")
    pause(1.0)
    print("How to play:")
    print("- Enter the number of your choice (e.g., 1 or 2).")
    print("- Enter 'q' at any prompt to quit immediately.")
    pause(1.2)
    print("\nYour story begins...\n")
    pause(1.0)
    start_scene()

if __name__ == '__main__':
    main()
