import pytest
from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from constants import BurgerData

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def mock_bun():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = BurgerData.BUN_NAME
    bun.get_price.return_value = BurgerData.BUN_PRICE
    return bun

@pytest.fixture
def mock_sauce():
    sauce = Mock(spec=Ingredient)
    sauce.get_name.return_value = BurgerData.SAUCE_NAME
    sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    sauce.get_price.return_value = BurgerData.SAUCE_PRICE
    return sauce

@pytest.fixture
def mock_filling():
    filling = Mock(spec=Ingredient)
    filling.get_name.return_value = BurgerData.FILLING_NAME
    filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    filling.get_price.return_value = BurgerData.FILLING_PRICE
    return filling

@pytest.fixture
def mock_ingredient_first():
    return Mock(spec=Ingredient)

@pytest.fixture
def mock_ingredient_second():
    return Mock(spec=Ingredient)

@pytest.fixture
def mock_ingredient_third():
    return Mock(spec=Ingredient)
