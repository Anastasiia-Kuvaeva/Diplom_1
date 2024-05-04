import pytest
from praktikum.ingredient import Ingredient
from praktikum.database import Database


# Тестовый набор для класса Ingredient
class TestIngredient:
    database: Database = Database()

    # Тестирование конструктора класса
    @pytest.mark.parametrize('ingredient_type, ingredient_name, ingredient_price', [
        (database.available_ingredients()[0].get_type(), database.available_ingredients()[0].get_name(),
         database.available_ingredients()[0].get_price()),
        (database.available_ingredients()[1].get_type(), database.available_ingredients()[1].get_name(),
         database.available_ingredients()[1].get_price()),
        (database.available_ingredients()[2].get_type(), database.available_ingredients()[2].get_name(),
         database.available_ingredients()[2].get_price())
    ])
    def test_init(self, ingredient_type, ingredient_name, ingredient_price):
        # Создание ингредиента
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        # Проверка
        assert ingredient.type == ingredient_type
        assert ingredient.name == ingredient_name
        assert ingredient.price == ingredient_price

    # Тестирование метода get_price()
    @pytest.mark.parametrize('ingredient_type, ingredient_name, ingredient_price', [
        (database.available_ingredients()[0].get_type(), database.available_ingredients()[0].get_name(),
         database.available_ingredients()[0].get_price()),
        (database.available_ingredients()[1].get_type(), database.available_ingredients()[1].get_name(),
         database.available_ingredients()[1].get_price()),
        (database.available_ingredients()[2].get_type(), database.available_ingredients()[2].get_name(),
         database.available_ingredients()[2].get_price())
    ])
    def test_get_price(self, ingredient_type, ingredient_name, ingredient_price):
        # Создание ингредиента
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        # Проверка
        assert ingredient.get_price() == ingredient_price

    # Тестирование метода get_name()
    @pytest.mark.parametrize('ingredient_type, ingredient_name, ingredient_price', [
        (database.available_ingredients()[0].get_type(), database.available_ingredients()[0].get_name(),
         database.available_ingredients()[0].get_price()),
        (database.available_ingredients()[1].get_type(), database.available_ingredients()[1].get_name(),
         database.available_ingredients()[1].get_price()),
        (database.available_ingredients()[2].get_type(), database.available_ingredients()[2].get_name(),
         database.available_ingredients()[2].get_price())
    ])
    def test_get_name(self, ingredient_type, ingredient_name, ingredient_price):
        # Создание ингредиента
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        # Проверка
        assert ingredient.get_name() == ingredient_name

    # Тестирование метода get_type()
    @pytest.mark.parametrize('ingredient_type, ingredient_name, ingredient_price', [
        (database.available_ingredients()[0].get_type(), database.available_ingredients()[0].get_name(),
         database.available_ingredients()[0].get_price()),
        (database.available_ingredients()[1].get_type(), database.available_ingredients()[1].get_name(),
         database.available_ingredients()[1].get_price()),
        (database.available_ingredients()[2].get_type(), database.available_ingredients()[2].get_name(),
         database.available_ingredients()[2].get_price())
    ])
    def test_get_type(self, ingredient_type, ingredient_name, ingredient_price):
        # Создание ингредиента
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        # Проверка
        assert ingredient.get_type() == ingredient_type
