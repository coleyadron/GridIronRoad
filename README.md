# GridIron Road

GridIron Road is an interactive football management game inspired by the classic Oregon Trail. Players take on the role of a General Manager, making strategic decisions to lead their team to victory. From drafting players to managing staff and playing through the season, every decision impacts the team's success.

---

## Features

- **Team Management**: Select your team, hire coaching staff, and manage your roster.
- **Draft System**: Build your team by drafting players with unique stats and contracts.
- **Season Simulation**: Play through a regular season and postseason, facing off against opponents.
- **Mini-Games**: Engage in interactive mini-games like punt returns to influence game outcomes.
- **Dynamic Scenarios**: Encounter pregame and postgame decisions that affect your team's performance.
- **Save and Load**: Save your progress and continue your journey at any time.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/GridIronRoad.git
   cd GridIronRoad
   ```

2. **Install Dependencies**:
   Ensure you have Python 3 installed. Install the required libraries using:
   ```bash
   pip install pygame
   ```

3. **Run the Game**:
   Start the game by running:
   ```bash
   python3 main.py
   ```

---

## How to Play

1. **Start a New Game**:
   - Select your experience level.
   - Choose your team and hire coaching staff.
   - Draft players to build your roster.

2. **Play Through the Season**:
   - Compete against opponents in regular season games.
   - Make strategic decisions during pregame and postgame scenarios.
   - Participate in mini-games to influence game outcomes.

3. **Postseason**:
   - Qualify for the playoffs based on your season record.
   - Compete in postseason matchups to win the championship.

4. **Save and Load**:
   - Save your progress at any time.
   - Load your saved game to continue where you left off.

---

## File Structure

- **`main.py`**: Entry point for the game.
- **`gridironRoad.py`**: Core logic for managing game state, saving, and updating data.
- **screens**: Contains modules for different game screens (e.g., team selection, in-game actions).
- **logic**: Contains game logic, such as scheduling and mini-game objects.
- **minigames**: Contains the logic to run the mini-games.
- **json**: Stores game data, including team rosters, free agents, and saved states.
- **assets**: Contains images, fonts, and other resources used in the game.

---

## Key Modules

### main.py
- Handles the main game loop and transitions between screens.
- Starts a new game or loads a saved game.

### gridironRoad.py
- Manages global game state, including experience, team, staff, and draft.
- Handles saving and loading game data.

### screens
- **`experienceSelection.py`**: Allows players to choose their experience level.
- **`teamSelection.py`**: Enables team selection based on experience.
- **`coachingStaff.py`**: Handles hiring coaching staff.
- **`inGame.py`**: Manages in-game actions and updates the scoreboard.

### logic
- **`scheduler.py`**: Generates the season schedule.
- **`probEngine.py`**: Handles probability of the user winning a drive.

---

## JSON Files

- **`userTeam.json`**: Stores the user's team name and roster.
- **`userState.json`**: Tracks the user's progress and game state.

---

## Future Enhancements

- Add more mini-games to diversify gameplay.
- The ability to pick team colors
- The ability to change screen size
- Implement contracts (resigning players, and contract expiration)

---

## Credits

- **Developer**: Joseph Loriso and Cole Yadron
- **Inspiration**: Oregon Trail, Retro Bowl, and football management games.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.