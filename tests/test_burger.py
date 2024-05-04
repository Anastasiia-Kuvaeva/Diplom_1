from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.bun import Bun
import pytest


# Тестовый набор для класса Burger
class TestBurger:
    database: Database = Database()

    # Тестирование метода set_buns
    def test_set_buns(self):
        database: Database = Database()
        # Создание булки
        bun = Bun(database.available_buns()[0].get_name(), database.available_buns()[0].get_price())
        # Создание бургера
        burger = Burger()
        burger.set_buns(bun)
        # Проверка
        assert burger.bun == bun

    # Тестирование метода add_ingredients()
    @pytest.mark.usefixtures("mock_ingredient")
    def test_add_ingredients(self, mock_ingredient):
        database: Database = Database()
        # Создание бургера
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        # Проверка
        assert burger.ingredients[0].get_price() == database.available_ingredients()[0].get_price()
        assert burger.ingredients[0].get_name() == database.available_ingredients()[0].get_name()
        assert burger.ingredients[0].get_type() == database.available_ingredients()[0].get_type()

    # Тестирование метода remove_ingredient()
    @pytest.mark.usefixtures("mock_ingredient")
    def test_remove_ingredient(self, mock_ingredient):
        # Создание бургера
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        # Проверяем, что ингредиент действительно добавлен
        assert len(burger.ingredients) == 1
        burger.remove_ingredient(0)
        # Проверка
        assert len(burger.ingredients) == 0

    # Тестирование метода move_ingredient
    @pytest.mark.usefixtures("mock_ingredient")
    @pytest.mark.usefixtures("mock_ingredient_2")
    def test_move_ingredient(self, mock_ingredient, mock_ingredient_2):
        # Создание бургера
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient_2)
        # Перемещение ингредиента
        burger.move_ingredient(0, 1)
        # Проверка
        assert burger.ingredients[0] == mock_ingredient_2
        assert burger.ingredients[1] == mock_ingredient

    # Тестирование метода get_price()
    def test_get_price(self):
        database: Database = Database()
        # Создание бургера
        burger = Burger()
        burger.set_buns(database.available_buns()[1])
        burger.add_ingredient(database.available_ingredients()[0])
        burger.add_ingredient(database.available_ingredients()[1])
        burger.add_ingredient(database.available_ingredients()[2])
        burger.add_ingredient(database.available_ingredients()[3])
        # Проверка
        assert burger.get_price() == 1100

    # Проверка метода get_receipt()
    def test_get_receipt(self):
        database: Database = Database()
        # Создание бургера
        burger = Burger()
        burger.set_buns(database.available_buns()[1])
        burger.add_ingredient(database.available_ingredients()[0])
        burger.add_ingredient(database.available_ingredients()[1])
        burger.add_ingredient(database.available_ingredients()[2])
        burger.add_ingredient(database.available_ingredients()[3])
        # Проверка
        expected_receipt = '''(==== white bun ====)\n= sauce hot sauce =\n= sauce sour cream =\n= sauce chili sauce =\n= filling cutlet =\n(==== white bun ====)\n\nPrice: 1100'''
        assert burger.get_receipt() == expected_receipt
