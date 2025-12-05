import unittest
import task


class TestBooleanVariables(unittest.TestCase):

    def test_group_1(self):
        """Test positive variable names"""
        # Check all variables are assigned (not None)
        self.assertIsNotNone(task.is_wearing_shoes, "GRP 1: shoes var not assigned")
        self.assertIsNotNone(task.ate_breakfast_1, "GRP 1: breakfast_1 var not assigned")
        self.assertIsNotNone(task.ate_breakfast_2, "GRP 1: breakfast_2 var not assigned")
        self.assertIsNotNone(task.is_awake, "GRP 1: awake var not assigned")
        self.assertIsNotNone(task.has_phone, "GRP 1: phone var not assigned")
        self.assertIsNotNone(task.near_sink, "GRP 1: sink var not assigned")

        # Check all are boolean type
        self.assertIsInstance(task.is_wearing_shoes, bool, "GRP 1: Use True/False")
        self.assertIsInstance(task.ate_breakfast_1, bool, "GRP 1: Use True/False")
        self.assertIsInstance(task.ate_breakfast_2, bool, "GRP 1: Use True/False")
        self.assertIsInstance(task.is_awake, bool, "GRP 1: Use True/False")
        self.assertIsInstance(task.has_phone, bool, "GRP 1: Use True/False")
        self.assertIsInstance(task.near_sink, bool, "GRP 1: Use True/False")

        # Check the values are correct
        self.assertFalse(task.is_wearing_shoes, "GRP 1: Check your logic")
        self.assertTrue(task.ate_breakfast_1, "GRP 1: Check your logic")
        self.assertFalse(task.ate_breakfast_2, "GRP 1: Check your logic")
        self.assertTrue(task.is_awake, "GRP 1: Check your logic")
        self.assertTrue(task.has_phone, "GRP 1: Check your logic")
        self.assertFalse(task.near_sink, "GRP 1: Check your logic")

    def test_group_2(self):
        """Test negative variable names"""
        # Check all variables are assigned (not None)
        self.assertIsNotNone(task.not_wearing_hat, "GRP 2: hat var not assigned")
        self.assertIsNotNone(task.not_forgot_homework, "GRP 2: homework var not assigned")
        self.assertIsNotNone(task.not_tired, "GRP 2: tired var not assigned")
        self.assertIsNotNone(task.not_have_pencil, "GRP 2: pencil var not assigned")
        self.assertIsNotNone(task.not_in_front, "GRP 2: front var not assigned")

        # Check all are boolean type
        self.assertIsInstance(task.not_wearing_hat, bool, "GRP 2: Ues True/False")
        self.assertIsInstance(task.not_forgot_homework, bool, "GRP 2 ERROR: Use True/False")
        self.assertIsInstance(task.not_tired, bool, "GRP 2: Use True/False")
        self.assertIsInstance(task.not_have_pencil, bool, "GRP 2: Use True/False")
        self.assertIsInstance(task.not_in_front, bool, "GRP 2: Use True/False")

        # Check the values are correct
        self.assertFalse(task.not_wearing_hat, "GRP 2: Check your logic")
        self.assertFalse(task.not_forgot_homework, "GRP 2: Check your logic")
        self.assertTrue(task.not_tired, "GRP 2: Check your logic")
        self.assertFalse(task.not_have_pencil, "GRP 2: Check your logic")
        self.assertFalse(task.not_in_front, "GRP 2: Check your logic")


if __name__ == '__main__':
    unittest.main()
