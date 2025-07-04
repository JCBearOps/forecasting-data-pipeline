import os
import pytest

def test_dags_folder_exists():
    assert os.path.exists("dags")
