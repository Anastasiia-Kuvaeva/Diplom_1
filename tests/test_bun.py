import pytest
from praktikum.bun import Bun
from praktikum.database import Database


# Тестовый набор для класса Bun
class TestBun:
    database: Database = Database()

    # Тестирование метода get_name()
    @pytest.mark.parametrize('name, price', [
        (database.available_buns()[0].get_name(), database.available_buns()[0].get_price()),
        (database.available_buns()[1].get_name(), database.available_buns()[1].get_price()),
        (database.available_buns()[2].get_name(), database.available_buns()[2].get_price())
    ])
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    # Тестирование метода get_price()
    @pytest.mark.parametrize('name, price', [
        (database.available_buns()[0].get_name(), database.available_buns()[0].get_price()),
        (database.available_buns()[1].get_name(), database.available_buns()[1].get_price()),
        (database.available_buns()[2].get_name(), database.available_buns()[2].get_price())
    ])
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
