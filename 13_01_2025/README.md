[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/SVBazuev/my_test_tasks/blob/main/13_01_2025/README.md)
[![ru](https://img.shields.io/badge/lang-ru-blue.svg)](https://github.com/SVBazuev/my_test_tasks/blob/main/13_01_2025/README.md)
[![Repo stars](https://img.shields.io/badge/Repo-home-darkgreen.svg)](https://github.com/SVBazuev/my_test_tasks/blob/main/README.md)
# Test Tasks 
To apply, complete the following tasks that demonstrate your technical skills and ability to solve real-world challenges.  

## Task 1. Develop a function to determine the score in a game
Objective In the code example below, a list of game score states throughout a match is generated.
Develop the function get_score(game_stamps, offset), which will return the score at the moment of offset in the list of game_stamps.
It is necessary to understand the essence of the written code, notice the nuances, develop a function that fits in style with the existing code, preferably with adequate algorithmic complexity.

```python
from pprint import pprint
import random
import math

TIMESTAMPS_COUNT = 50000

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
        PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps


game_stamps = generate_game()

pprint(game_stamps)


def get_score(game_stamps, offset):
    '''
        Takes list of game's stamps and time offset for which returns the scores for the home and away teams.
        Please pay attention to that for some offsets the game_stamps list may not contain scores.
    '''
    # return home, away

```
### Deliverables 
[A link to the gist with the source code of the function.][0]

[0]: https://github.com/SVBazuev/ya-grazhdanin.online
 
---
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/SVBazuev/my_test_tasks/blob/main/13_01_2025/README.md)
[![ru](https://img.shields.io/badge/lang-ru-blue.svg)](https://github.com/SVBazuev/my_test_tasks/blob/main/13_01_2025/README.ru.md)
[![Repo stars](https://img.shields.io/badge/Repo-home-darkgreen.svg)](https://github.com/SVBazuev/my_test_tasks/blob/main/README.md)
