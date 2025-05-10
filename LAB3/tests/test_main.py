import unittest
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import main


class TestMain(unittest.TestCase):
    @patch('main.ExpressionParser.parse_expression')
    @patch('main.build_truth_table')
    @patch('main.display_results')
    def test_main_flow(self, mock_display, mock_build, mock_parse):
        # Настройка моков
        mock_parse.return_value = (['a', 'b'], ['a', 'b', '|'])
        mock_build.return_value = {
            'index_form': '0111',
            'dnf_expression': 'test_dnf',
            'cnf_expression': 'test_cnf'
        }

        # Тестируем основной поток
        with patch('builtins.input', side_effect=['a | b', 'n']):
            with patch('main.display_minimization_results') as mock_min:
                main.main()

        # Проверяем вызовы
        mock_parse.assert_called_once_with("a | b")
        mock_build.assert_called_once()
        mock_display.assert_called_once()
        mock_min.assert_called_once()

    @patch('builtins.input', side_effect=['invalid', 'q'])
    def test_invalid_expression(self, mock_input):
        with self.assertRaises(ValueError):
            main.get_valid_expression()


if __name__ == '__main__':
    unittest.main()