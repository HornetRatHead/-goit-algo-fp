#Tsygankov_FP_6

def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорій до вартості у спадному порядку
    sorted_items = sorted(items, key=lambda x: x['calories'] / x['cost'], reverse=True)
    
    selected_items = []  # Список вибраних страв
    total_cost = 0  # Загальна вартість вибраних страв
    total_calories = 0  # Загальна калорійність вибраних страв
    
    # Проходимося по відсортованим стравам
    for item in sorted_items:
        # Додаємо страву у список вибраних, якщо вона не перевищує бюджет
        if total_cost + item['cost'] <= budget:
            selected_items.append(item)
            total_cost += item['cost']
            total_calories += item['calories']
    
    return selected_items, total_cost, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    K = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(budget + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif items[i - 1]["cost"] <= j:
                K[i][j] = max(items[i - 1]["calories"] + K[i - 1][j - items[i - 1]["cost"]], K[i - 1][j])
            else:
                K[i][j] = K[i - 1][j]

    selected_items = []
    total_cost = 0
    total_calories = 0

    j = budget
    for i in range(n, 0, -1):
        if K[i][j] != K[i - 1][j]:
            selected_items.append(items[i - 1])
            total_cost += items[i - 1]["cost"]
            total_calories += items[i - 1]["calories"]
            j -= items[i - 1]["cost"]
    
    return selected_items, total_cost, total_calories

if __name__ == "__main__":
    items = [
        {"name": "pizza", "cost": 50, "calories": 300},
        {"name": "hamburger", "cost": 40, "calories": 250},
        {"name": "hot-dog", "cost": 30, "calories": 200},
        {"name": "pepsi", "cost": 10, "calories": 100},
        {"name": "cola", "cost": 15, "calories": 220},
        {"name": "potato", "cost": 25, "calories": 350}
    ]

    budget = int(input("Введіть бюджет: "))

    selected_items_greedy, total_cost_greedy, total_calories_greedy = greedy_algorithm(items, budget)
    print("Результати виконання жадібного алгоритму:")
    print("Вибрані страви:", [item["name"] for item in selected_items_greedy])
    print("Загальна вартість:", total_cost_greedy)
    print("Загальна калорійність:", total_calories_greedy)

    selected_items_dp, total_cost_dp, total_calories_dp = dynamic_programming(items, budget)
    print("\nРезультати виконання алгоритму динамічного програмування:")
    print("Вибрані страви:", [item["name"] for item in selected_items_dp])
    print("Загальна вартість:", total_cost_dp)
    print("Загальна калорійність:", total_calories_dp)

