import pytest
from main import *

class TestEmail:
    @pytest.mark.parametrize("test_input", ["test@test.ru", "w@w.com", "123QWE@mmm.mmm"])
    def test_positive_example(self, log_file_name, test_input):
        """Позитивный тест."""
        result = valid_email(test_input)
        log(log_file_name, "test passed!\n")
        assert result

    @pytest.mark.parametrize("test_input", ["test@test.", "a@", "@tt"])
    def test_negative_example(self, log_file_name, test_input):
        """Негативный тест."""
        result = valid_email(test_input)
        log(log_file_name, "test failed!\n")
        assert result is False
