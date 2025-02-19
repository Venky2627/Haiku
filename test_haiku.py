# test_haiku.py
import os
import json
from io import StringIO
from unittest.mock import patch
from haiku import HaikuApp

def test_add_haiku_to_theme():
    app = HaikuApp()
    test_haiku_db = "test_haikus.json"
    app.haiku_db = test_haiku_db

    # Clear the test database before each test
    app.haikus = {"love": [], "happy": [], "sadness": []}  # Reset data
    app.save_haiku_data() # Save the empty data

    try:
        with patch('builtins.input', side_effect=["love", "Line 1", "Line 2", "Line 3"]):
            app.add_haiku_to_theme()
        assert len(app.haikus["love"]) == 1  # Now it should be 1
        assert "Line 1\nLine 2\nLine 3" in app.haikus["love"][0]
        print("test_add_haiku_to_theme passed")
    finally:
        try:
            os.remove(test_haiku_db)  # Keep cleanup in finally
        except FileNotFoundError:
            pass

def test_generate_custom_haiku():
    app = HaikuApp()
    test_haiku_file = "test_haikus.txt"
    app.haiku_file = test_haiku_file
    try:
        with patch('builtins.input', side_effect=["Line 1", "Line 2", "Line 3"]): # Mock input
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                app.generate_custom_haiku() # Call the original function
                assert "Your Custom Haiku" in mock_stdout.getvalue()
        with open(test_haiku_file, "r") as f:
            assert "Line 1\nLine 2\nLine 3" in f.read()
        print("test_generate_custom_haiku passed")
    finally:
        try:
            os.remove(test_haiku_file)
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    test_add_haiku_to_theme()
    test_generate_custom_haiku()