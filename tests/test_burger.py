import pytest
from unittest.mock import Mock

from praktikum.bun import Bun
from constants import BurgerData


class TestBurger:
    # НОВЫЙ БУРГЕР СОЗДАЁТСЯ БЕЗ БУЛОЧКИ
    def test_init_burger_without_bun(self, burger):
        with pytest.raises(AttributeError):
            burger.get_price()
      
    # ВЫБОР БУЛОЧКИ
    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun is mock_bun

    # ДОБАВЛЕНИЕ ИНГРЕДИЕНТА
    def test_add_ingredient(self, burger, mock_filling):
        burger.add_ingredient(mock_filling)
        assert burger.ingredients == [mock_filling]

    # УДАЛЕНИЕ ИНГРЕДИЕНТА ПО ИНДЕКСУ
    def test_remove_ingredient(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)
        assert burger.ingredients == [mock_filling]

    # ПЕРЕМЕЩЕНИЕ ИНГРЕДИЕНТА НА НОВУЮ ПОЗИЦИЮ
    @pytest.mark.parametrize('index, new_index, expected', [
        (0, 2, [1, 2, 0]),
        (2, 0, [2, 0, 1]),
        (0, 1, [1, 0, 2]),
        (1, 1, [0, 1, 2])
    ])

    def test_move_ingredient(self, burger, mock_ingredient_first, mock_ingredient_second, mock_ingredient_third, index, new_index, expected):
        items = [mock_ingredient_first, mock_ingredient_second, mock_ingredient_third]
        burger.add_ingredient(mock_ingredient_first)
        burger.add_ingredient(mock_ingredient_second)
        burger.add_ingredient(mock_ingredient_third)
        burger.move_ingredient(index, new_index)
        assert burger.ingredients == [items[expected[0]], items[expected[1]], items[expected[2]]]

    # РАСЧЁТ ЦЕНЫ: ДВЕ БУЛОЧКИ + ИНГРЕДИЕНТЫ
    @pytest.mark.parametrize('bun_price, first_price, second_price, expected', [
        (100, 0, 0, 200),
        (100, 50, 0, 250),
        (50, 10, 20, 130),
        (99.5, 0.5, 0, 199.5)
    ])

    def test_get_price(self, burger, mock_ingredient_first, mock_ingredient_second, bun_price, first_price, second_price, expected):
        bun = Mock(spec=Bun)
        bun.get_price.return_value = bun_price
        mock_ingredient_first.get_price.return_value = first_price
        mock_ingredient_second.get_price.return_value = second_price
        burger.set_buns(bun)
        burger.add_ingredient(mock_ingredient_first)
        burger.add_ingredient(mock_ingredient_second)
        assert burger.get_price() == expected

    # ЧЕК БУРГЕРА С ИНГРЕДИЕНТАМИ
    def test_get_receipt_with_ingredients(self, burger, mock_bun, mock_sauce, mock_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        assert burger.get_receipt() == BurgerData.RECEIPT_WITH_INGREDIENTS

    # ЧЕК БУРГЕРА БЕЗ ИНГРЕДИЕНТОВ
    def test_get_receipt_without_ingredients(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.get_receipt() == BurgerData.RECEIPT_WITHOUT_INGREDIENTS
        