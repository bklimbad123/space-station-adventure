# Space Station Adventure

A text-based "Choose Your Own Adventure" Python CLI game set on a mysterious sci-fi space station.

Repository: https://github.com/bklimbad123/space-station-adventure

## Contents

- `adventure_game.py` — the single-file Python game. Run this in your terminal.

## Prerequisites

- Python 3.8+ installed. Verify with:

  ```bash
  python3 --version
  ```

- (Optional but recommended) A virtual environment to keep dependencies isolated.

## Getting started — step-by-step

1. Clone the repository:

   ```bash
   git clone https://github.com/bklimbad123/space-station-adventure.git
   cd space-station-adventure
   ```

2. (Optional) Create and activate a Python virtual environment:

   On macOS / Linux:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   On Windows (PowerShell):
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. The game is a single script and has no external dependencies. Make it executable (optional):

   ```bash
   chmod +x adventure_game.py
   ```

4. Run the game:

   On macOS / Linux:
   ```bash
   ./adventure_game.py
   # or
   python3 adventure_game.py
   ```

   On Windows:
   ```powershell
   python adventure_game.py
   ```

5. How to play:
   - Enter the number of your choice (e.g., `1` or `2`) and press Enter.
   - Enter `q` at any prompt to quit immediately.

## Notes

- This is a terminal/CLI game. GitHub Pages cannot host or run this Python script directly. If you'd like a browser-playable version, I can convert the story to a single-page HTML/JavaScript game and deploy it to GitHub Pages.

- The repository is licensed under the MIT License.

## Contributing

Contributions are welcome. Suggestions:
- Add more branches, endings, or randomized outcomes
- Implement a save/load feature
- Create a web frontend for GitHub Pages deployment

To contribute, fork the repo, make changes in a branch, and open a pull request.

## License

This project uses the MIT License.
