import unittest


from my_get_score import get_score


class TestGetScore(unittest.TestCase):

    def setUp(self):
        """Preparing data for tests.
        Подготовка данных для тестов."""


        self.game_stamps = [
            {"offset": 0, "score": {"home": 0, "away": 0}},
            {"offset": 1, "score": {"home": 1, "away": 0}},
            {"offset": 4, "score": {"home": 1, "away": 1}},
            {"offset": 9, "score": {"home": 2, "away": 1}},
            {"offset": 10, "score": {"home": 2, "away": 2}}
        ]


    def test_get_score_at_existing_offset(self):
        """Test: Getting a bill for an existing offset.
        Тест: получение счета по существующему смещению."""


        result = get_score(self.game_stamps, 4)
        self.assertEqual(result, (1, 1))


    def test_get_score_beyond_last_offset(self):
        """Test: Getting a bill for an offset greater than the last one.
        Тест: получение счета по смещению, превышающему последнее."""


        result = get_score(self.game_stamps, 11)
        self.assertEqual(result, (2, 2))


    def test_get_score_for_non_existing_offset(self):
        """Test: Getting a bill for a non-existent offset.
        Тест: получение счета по несуществующему смещению."""


        result = get_score(self.game_stamps, 3)
        self.assertEqual(result, (1, 0))


    def test_get_score_with_empty_stamps(self):
        """Test: raising an exception with an empty list of labels.
        Тест: поднятие исключения при пустом списке меток."""


        with self.assertRaises(ValueError) as context:
            get_score([], 0)
        self.assertEqual(
            str(context.exception),
            "The game_stamps list cannot be empty."
            )


    def test_get_score_negative_offset(self):
        """Test: raising an exception at a negative offset.
        Тест: поднятие исключения при отрицательном смещении."""


        with self.assertRaises(ValueError) as context:
            get_score(self.game_stamps, -1)
        self.assertEqual(
            str(context.exception), "The offset cannot be negative."
            )


    def test_get_score_data_integrity_violation(self):
        """Test: raising an exception in case of data integrity violation.
        Тест: поднятие исключения при нарушении целостности данных."""


        with self.assertRaises(ValueError) as context:
            get_score(self.game_stamps, 8)
        self.assertEqual(
            str(context.exception),
            "Data integrity violation: "
            "gap in offset values exceeds OFFSET_MAX_STEP."
            )


if __name__ == '__main__':
    unittest.main()
  
