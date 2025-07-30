import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from calculator import plus, minus, multiplication, division


@pytest.mark.parametrize('num_user_1,num_user_2,result', [
    (1,1,2),
    (1,2,3),
    (14,2,16),
    (12,12,24),
    ])
def test_plus(num_user_1, num_user_2,result):
    assert plus (num_user_1,num_user_2) == result
