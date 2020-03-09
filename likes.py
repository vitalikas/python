import json
import collections

events = [] # заводим переменную для списка отфильтрованных событий
favItems = collections.Counter() # заводим переменную для счётчика

FILE = 'data_3000.json'
file_obj = open(FILE)
# obj_lines = file_obj.readlines() # читаем файл по строкам

for obj_line in file_obj: # читаем файл по строкам
    event = json.loads(obj_line) # десериализуем строку в словарь, используя метод json.loads
    # print(event)
    if not event['detectedDuplicate'] and not event['detectedCorruption'] and event['eventType'] == 'itemFavEvent': # фильтруем события
        events.append(event)

file_obj.close()

for event in events: # итерируемся по всем событиям
    favItems[event['item_id']] += 1 # считаем кол-во item_id в отсортированном списке events

# print(favItems.most_common()) # распечатываем список от самого частого по убыванию
print(f"Most liked item ID is: {favItems.most_common()[0][0]}")
print(f"Less liked item ID is: {favItems.most_common()[-1][0]}")

for favItem, value in favItems.items():
    if value == 1359:
        print(f"Item ID {favItem} was liked for 1359 times")