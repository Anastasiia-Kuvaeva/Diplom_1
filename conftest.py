import pytest
from praktikum.database import Database
from unittest.mock import Mock

database: Database = Database()


# Фикстура создания mock ingredient (первый ingredient из БД)
@pytest.fixture
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_price.return_value = database.available_ingredients()[0].get_price()
    mock_ingredient.get_name.return_value = database.available_ingredients()[0].get_name()
    mock_ingredient.get_type.return_value = database.available_ingredients()[0].get_type()
    return mock_ingredient

# Фикстура создания mock ingredient (второй ingredient из БД)
@pytest.fixture
def mock_ingredient_2():
    mock_ingredient = Mock()
    mock_ingredient.get_price.return_value = database.available_ingredients()[1].get_price()
    mock_ingredient.get_name.return_value = database.available_ingredients()[1].get_name()
    mock_ingredient.get_type.return_value = database.available_ingredients()[1].get_type()
    return mock_ingredient
