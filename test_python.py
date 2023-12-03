# import os
#
# def create_folder(new_data):
#     if not os.path.exists(new_data):
#         os.makedirs(new_data)
#     else:
#         print(f"Папка '{new_data}' уже существует.")
#
# create_folder('new_date')

import os
import shutil
import platform

# def delete_folder(new_date):
#     # Проверяем, существует ли папка
#     if os.path.isdir(new_date):
#         # Удаляем папку
#         try:
#             shutil.rmtree(new_date)
#             print(f"Папка '{new_date}' и все ее содержимое успешно удалены.")
#         except OSError as e:
#             print(f"Ошибка: {new_date} : {e.strerror}")
#     else:
#         # Если папка не существует, сообщаем об этом
#         print(f"Папка '{new_date}' не существует.")
#
# # Вызов функции для удаления папки 'example_folder'
# delete_folder('new_date')

# def copy_folder(new_date, date):
#     try:
#         shutil.copytree(new_date, date)
#         print(f"Папка '{new_date}' скопирована в '{date}'.")
#     except IOError as e:
#         print(f"Не удалось скопировать папку. {e}")
#
# # Вызов функции для копирования папки 'example_folder' в 'example_folder_backup'
# copy_folder('new_date', 'date')
# #

# contents = os.listdir()
# for item in contents:
#     print(item)

# contents = os.listdir()
# print("Папки в текущей директории:")
# for item in contents:
#     if os.path.isdir(item):
#         print(item)

# contents = os.listdir()
# print("Файлы в текущей директории:")
# for item in contents:
#     if os.path.isfile(item):
#         print(item)

#
# # Получение имени операционной системы
# print(f"Имя ОС: {os.name}")
#
# # Получение подробной информации об операционной системе
# print(f"Подробная информация об ОС: {platform.system()} {platform.release()}")
#
# # Получение информации о версии
# print(f"Версия ОС: {platform.version()}")
#
# # Получение информации о платформе
# print(f"Платформа: {platform.platform()}")
#
# # Получение информации о архитектуре процессора
# print(f"Архитектура: {platform.architecture()}")
#
# # Получение информации о машине (аппаратной платформе)
# print(f"Машина: {platform.machine()}")
#
# # Получение информации о процессоре
# print(f"Процессор: {platform.processor()}")
#
# # Получение информации о системном типе Python
# print(f"Системный тип Python: {platform.python_implementation()}")
#
# # Получение информации о версии Python
# print(f"Версия Python: {platform.python_version()}")

# # Информация о создателе программы
# CREATOR_NAME = "Имя создателя"
# CREATOR_EMAIL = "email@example.com"
# PROGRAM_VERSION = "1.0.0"
#
# def print_creator_info():
#     print(f"Программа версии {PROGRAM_VERSION}")
#     print(f"Создано {CREATOR_NAME}")
#     print(f"Контактный email: {CREATOR_EMAIL}")
#
# # Вывод информации о создателе
# print_creator_info()


#
# import chet

#
# import os
#
# def change_directory():
#     # Запрос пути у пользователя
#     new_path = input("Введите путь к новой рабочей директории: ")
#
#     try:
#         # Изменение рабочей директории
#         os.chdir(new_path)
#         print(f"Рабочая директория изменена на {os.getcwd()}")
#     except FileNotFoundError:
#         print(f"Ошибка: директория '{new_path}' не найдена.")
#     except NotADirectoryError:
#         print(f"Ошибка: '{new_path}' не является директорией.")
#     except Exception as e:
#         print(f"Произошла ошибка: {e}")
#
# # Вызов функции для смены рабочей директории
# change_directory()
