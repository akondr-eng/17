import pytest
 
from shipping import delivery_cost, delivery_days
 
 
@pytest.mark.parametrize(
    "distance, expected",
    [(1, 1), (100, 1), (101, 3), (500, 3), (501, 7), ],
)
def test_delivery_days_boundaries(distance, expected):
    assert delivery_days(distance) == expected
 
 
def test_weight_above_limit_is_rejected():
    with pytest.raises(ValueError):
        delivery_cost(1, 100) == 999
