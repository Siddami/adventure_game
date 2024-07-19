# Time Adventure Game

Welcome to the **Time Adventure Game**, an interactive text-based game where your choices determine the outcome of your adventure. You will navigate through time, encounter villains, and uncover secrets, all while making critical decisions that influence your journey.

## Table of Contents

1. [Game Overview](#game-overview)
2. [Installation](#installation)
3. [How to Play](#how-to-play)
4. [Game Flow](#game-flow)
5. [Functions](#functions)
6. [License](#license)

## Game Overview

In this game, you will:
- Select a team and an artifact.
- Encounter various villains.
- Use different weapons.
- Explore mysterious locations.
- Make decisions that lead to different endings.

Your goal is to protect the timeline and ensure a better future by making strategic choices.

## Installation

To play the game, follow these steps:

1. Ensure you have Python installed on your computer.
2. Download the `time_adventure.py` script.
3. Run the script in your terminal or command prompt using the following command:

```bash
python time_adventure.py
```

## How to Play

1. Run the script to start the game.
2. Follow the prompts and make choices by entering the corresponding number.
3. Read the narrative and make decisions at each step to progress through the story.
4. Try different choices to explore various endings and storylines.

## Game Flow

### Initial Setup

- A random team, artifact, villain, and weapon are selected at the start of the game.

### Introductory Narrative

- You are presented with a choice of locations to explore.

### Decision Points

- Throughout the game, you will encounter various decision points that will affect the outcome of the story. Examples include:
  - Choosing to purchase or leave an artifact.
  - Deciding whether to confront villains or evade them.
  - Making strategic choices in battles.

### Endings

- The game can end in different ways based on your decisions:
  - Winning by defeating the villains and safeguarding the timeline.
  - Losing by making unfavorable choices that lead to failure.
  - Getting trapped in time or joining forces with allies.

## Functions

### `run_game()`
- Initializes the game, sets up random elements, and starts the introductory narrative.

### `intro()`
- Introduces the story and prompts the player to choose a location to explore.

### `adventure_begins()`
- Guides the player on what to do with the artifact based on their chosen location.

### `theInput()`
- Prompts the player to select a location to explore.

### `startOver(callback)`
- Asks the player if they want to restart or continue from a certain point.

### `play_again(callback)`
- Asks the player if they want to play again after reaching an ending.

### `print_pause(message)`
- Prints a message and pauses for a brief period to enhance the narrative experience.

### `onWin()`
- Prints the winning narrative when the player successfully completes the game.

### `onLoss()`
- Prints the losing narrative when the player fails in their mission.

### Various Decision Functions
- Functions like `pick_artifact()`, `drop_artifact()`, `fight()`, `confrontation()`, `allies()`, `ambush()`, `strangers()`, `onDrop()`, `trappedInTime()`, `expose()`, `commotion()`, `distantFuture()`, `onBuy()`, `explore()`, and `purchase()` handle different decision points in the game, each influencing the storyline based on player choices.

## License

This project is licensed under the MIT License. Feel free to modify and distribute it as you wish.

Enjoy your adventure through time!
