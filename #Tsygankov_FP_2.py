#Tsygankov_FP_2

import turtle

def draw_pifagor_tree(t, branch_len, level):
    if level == 0:
        return
    t.forward(branch_len * level)
    t.right(45)
    draw_pifagor_tree(t, branch_len, level-1)
    t.left(90)
    draw_pifagor_tree(t, branch_len, level-1)
    t.right(45)
    t.backward(branch_len * level)

def main():
    level = int(input("Введіть рівень рекурсії: "))
    max_level = 10  # Максимальний рівень рекурсії

    # Перевірка на максимальний рівень рекурсії
    if level > max_level:
        print(f"Максимальний рівень рекурсії - {max_level}. Введіть значення менше або рівне {max_level}.")
        return

    # Налаштування вікна та черепахи
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Фрактал 'Дерево Піфагора'")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.color("green")

    # Перемістимо черепаху в початкову позицію
    t.penup()
    t.goto(0, -100)
    t.pendown()

    # Виклик функції для малювання дерева Піфагора
    draw_pifagor_tree(t, 20, level)

    # Завершення програми при кліку на вікно
    screen.mainloop()

if __name__ == "__main__":
    main()