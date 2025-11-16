# Тестовое задание Avito QA
## Задание 1
### Bug List страницы AvitoTeam
#### Содержимое:
+ BUGLIST_TASK1.md
+ bug_screenshot.png
#### Формат баг-листа:
+ ID. Название
+ Описание бага
+ Приоритет бага
+ Причина присвоения приоритета
## Задание 2.1
### Задание на тестирование API
#### Требования к ПО
+ Python 3.10 и выше
#### Копирование репозитория и установка зависимостей
```
git clone https://github.com/ecoreee/test_task_qa_avito.git
cd test_task_qa_avito
python3 -m venv venv
pip install -r requirements.txt
```
#### Запуск тестов
+ Перед запуском тестов необходимо перейти в каталог test_task_qa_avito
##### Аргументы запуска:
+ pytest -v - запуск тестового фреймворка Pytest
+ -v - verbose, режим, чтобы видеть, какие тесты были запущены
##### Запуск API-тестов: 
```
pytest -v
```
##### Результат выполнения
```
=================================== test session starts ===================================
platform linux -- Python 3.12.3, pytest-9.0.1, pluggy-1.6.0 -- /home/ecoree/Документы/test_task_qa_avito/venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/ecoree/Документы/test_task_qa_avito
collected 12 items                                                                                                                                                                                                               

test_api.py::TestCreateItem::test_success_item_creation PASSED                                                                                                                                                             [  8%]
test_api.py::TestCreateItem::test_invalid_item_creation PASSED                                                                                                                                                             [ 16%]
test_api.py::TestCreateItem::test_03_empty_item_creation PASSED                                                                                                                                                            [ 25%]
test_api.py::TestCreateItem::test_create_item_without_seller_id PASSED                                                                                                                                                     [ 33%]
test_api.py::TestGetItemById::test_get_item_success PASSED                                                                                                                                                                 [ 41%]
test_api.py::TestGetItemById::test_get_not_existed_item PASSED                                                                                                                                                             [ 50%]
test_api.py::TestGetItemById::test_get_item_with_invalid_id PASSED                                                                                                                                                         [ 58%]
test_api.py::TestGetItemsBySeller::test_get_items_by_seller_id_success PASSED                                                                                                                                              [ 66%]
test_api.py::TestGetItemsBySeller::test_get_items_not_existed_seller_id PASSED                                                                                                                                             [ 75%]
test_api.py::TestGetItemsBySeller::test_get_items_with_invalid_seller_id PASSED                                                                                                                                            [ 83%]
test_api.py::TestGetStatistics::test_get_statistics_success PASSED                                                                                                                                                         [ 91%]
test_api.py::TestGetStatistics::test_get_statistics_not_existed_item PASSED                                                                                                                                                [100%]

=================================== 12 passed in 2.41s ===================================
```