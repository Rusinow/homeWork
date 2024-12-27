def test_function():
    def inner_function():
        print("I'm in the area of external func test_function")
    inner_function() #Вызовите функцию inner_function внутри функции test_function

test_function()

# Попробуйте вызывать inner_function вне функции test_function
# и посмотрите на результат выполнения программы
# inner_function()
# результатом вызова функции inner_function вне функции test_function
# является ошибка: имя "inner_function" не определено.
# имя inner_function существует только локально внутри функции test_function
# и не может быть вызвано из глобального пространства
