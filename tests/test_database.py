from praktikum.database import Database


# Тестовый набор для класса Database
class TestDatabase:

    # Тестирование размера списка булочек
    def test_buns_list_count(self):
        database: Database = Database()
        # Проверка
        assert len(database.available_buns()) == 3

    # Тестирование размера списка ингредиентов
    def test_ingredients_list_count(self):
        database: Database = Database()
        # Проверка
        assert len(database.available_ingredients()) == 6
