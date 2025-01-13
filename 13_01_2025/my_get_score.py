from typing import List, Tuple, Dict, Union


OFFSET_MAX_STEP = 3


def get_score(
    game_stamps: List[Dict[str, Union[int, Dict[str, int]]]],
    offset: int
) -> Tuple[int, int]:
    '''Returns the score of the home and away teams at a given time offset.

    Parameters:
    game_stamps (list): A list of game timestamps, where each timestamp
                        contains information about the score and offset.
    offset (int): The time offset for which the score needs to be retrieved.
                  Must be a non-negative integer.

    Returns:
    tuple: A tuple of two integers representing the scores of the home and
           away teams. If the time offset is greater than the last timestamp
           in the list, the score of the last timestamp is returned. If the
           time offset does not exist in the list, the score of the last
           timestamp that is less than the given offset is returned.

    Raises:
    ValueError: If the game_stamps list is empty, if the offset is negative,
                or if there is a data integrity violation (gap in offset values
                exceeds OFFSET_MAX_STEP).
    '''


    if not game_stamps:
        raise ValueError("The game_stamps list cannot be empty.")
    if offset < 0:
        raise ValueError("The offset cannot be negative.")

    if game_stamps[-1]["offset"] < offset:
        return (
            game_stamps[-1]["score"]["home"],
            game_stamps[-1]["score"]["away"]
            )
    else:
        check_stamps = [
            x for x in range(offset, offset - OFFSET_MAX_STEP, -1) if x >= 0
            ]
        for stamp in check_stamps:
            target = list(filter(lambda x: x["offset"] == stamp, game_stamps))
            if target:
                return (
                    target[0]["score"]["home"],
                    target[0]["score"]["away"]
                    )
        else:
            raise ValueError("Data integrity violation: "
                             "gap in offset values exceeds OFFSET_MAX_STEP."
                             )
          
