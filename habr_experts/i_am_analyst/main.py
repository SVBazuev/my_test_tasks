""""""

import io
import json
import pandas as pd
from collections import Counter
from concurrent.futures import ThreadPoolExecutor


with io.open(r"resources\golden.json", "r", encoding="utf-8") as json_file:
    golden = json.load(json_file)
    # pp.pprint(golden[:5])
    golden = pd.DataFrame(golden)
    # print(golden.head(20))

data = pd.read_csv(r'resources\main.csv', sep=';')
# print("Исходные данные:")
# print(data.head(20))

merged_data = pd.merge(data, golden, on='task', how='left')
print("Объединённые данные:")
print(merged_data.head(20))

# Получение ответов с помощью метода большинства
# предполагает игнорирование оценки качества исполнителей
majority_votes = data.groupby('task')['label'].agg(lambda x: x.mode()[0]).reset_index()
majority_votes.columns = ['task', 'majority_label']
# print("\nОтветы по методу большинства:")
# print(majority_votes.head(20))

# Добавим столбец с точностью исполнителей
merged_data = merged_data.assign(
    accuracy=merged_data.groupby('worker')['true_label']
    .transform(lambda x: round(x.mean(), 2))
).sort_values(by="task")
print("\nДанные с accuracy:")
print(merged_data.head(20), end='\n\n')


# Определение исполнителей для каждой задачи
task_workers = merged_data.groupby('task')['worker'].apply(list).reset_index()
task_workers.sort_values(by='task', key=lambda x: x.str[1:].astype(int), inplace=True) # type: ignore
task_workers.columns = ['task', 'workers']

# Выдернем воркеров с весами
precision = merged_data[
    ['worker', 'accuracy']].drop_duplicates().reset_index(drop=True)

def get_most_common_label(task, workers):
    # Получаем срез фрейма по задаче
    task_data = merged_data.loc[[task]]
    # print(task_data)

    # Сортируем исполнителей по их точности в порядке убывания
    sorted_workers = (
        precision[precision['worker'].isin(workers)]
        .sort_values(by='accuracy', ascending=False)
    )

    _len = len(sorted_workers)
    if _len > 2:
        half_count = (len(sorted_workers) // 2) + 1
    else:
        # если 2 или 1 учитывем все доступные
        half_count = _len

    # Берем большую половину исполнителей
    first_half_workers = sorted_workers['worker'].head(half_count).tolist()
    print(task, first_half_workers)

    # Получаем метки от первых половины исполнителей
    labels_first_half = task_data[task_data['worker'].isin(first_half_workers)]['label']

    # Определяем наиболее частое значение label
    if not labels_first_half.empty:
        most_common_label = Counter(labels_first_half).most_common(1)
        return task, most_common_label[0][0] if most_common_label else None
    # если результата нет
    return task, None


def main():
    with ThreadPoolExecutor(max_workers=1000) as executor:
        results = list(executor.map(lambda x: get_most_common_label(x[0], x[1]), task_workers.values))

    results_df = pd.DataFrame(results, columns=['task', 'accuracy_label'])
    return results_df


# Добавим индекс перед долгой обработкой
merged_data.set_index('task', inplace=True)
accuracy_label = main()

merged_data = pd.merge(merged_data, majority_votes, on='task', how='left')
merged_data = pd.merge(merged_data, accuracy_label, on='task', how='left')

print("\nОбъединенные данные с majority_label, accuracy_label:")
print(merged_data.head())

# Выбор необходимых столбцов
selected_columns = merged_data[['worker', 'task', 'label', 'majority_label', 'accuracy_label', 'accuracy']]
# Фильтрация строк, где absolute_accuracy отличается от good_accuracy_label
filtered_data = selected_columns[selected_columns['majority_label'] != selected_columns['accuracy_label']]
# Печать отфильтрованных данных
print("\nСтроки, где majority_label отличается от accuracy_label:")
print(filtered_data)
