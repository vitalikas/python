import json
import collections

events = [] # заводим переменную (пустой список) для списка отфильтрованных событий
favItems = collections.Counter() # заводим переменную для счётчика

FILE = 'data_3000.json' # файл присваиваем переменной
file_obj = open(FILE) # открываем переменную
# obj_lines = file_obj.readlines() # читаем файл по строкам

for obj_line in file_obj: # читаем файл по строкам
    event = json.loads(obj_line) # десериализуем строку в словарь, используя метод json.loads
    # print(event)
    if not event['detectedDuplicate'] and not event['detectedCorruption'] and event['eventType'] == 'itemFavEvent': # фильтруем события
        events.append(event) # помещаем отфильтрованные события в переменную events

file_obj.close() # закрываем файл

for event in events: # итерируемся по всем событиям в переменной events
    favItems[event['item_id']] += 1 # считаем кол-во событий item_id (товаров) в отсортированном списке events с помощью метода collections.Counter()

# print(favItems.most_common()) # распечатываем список от самого частого по убыванию
print(f"Most liked item ID is: {favItems.most_common()[0][0]}") # .most_common[0] - самый частый. [0] после указывает на ключ, [1] - значение ключа
print(f"Less liked item ID is: {favItems.most_common()[-1][0]}") # .most_common[-1] - самый редкий.

for favItem, value in favItems.items(): # итерируемся по всем ключам и значениям переменной favItems
    if value == 1359: # если значение равно 1359, 
        print(f"Item ID {favItem} was liked for 1359 times") # то выводим ключ этого значения