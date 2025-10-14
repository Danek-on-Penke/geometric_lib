# Документация к geometric_lib

## Общее описание библиотеки

Библиотека `geometric_lib` предоставляет набор функций для вычисления площади и периметра основных геометрических фигур:
- Круг (Circle)
- Квадрат (Square)
- Прямоугольник (Rectangle)
- Треугольник (Triange)
Каждая функция реализована в отдельном модуле и снабжена документацией (docstring) с описанием и примером вызова.

## Описание функций

### circle.py
`area_circle(r)` — вычисляет площадь круга по радиусу `r`.
Формула: `S = r * r * pi`
Пример: `area_circle(3)` → `28.274333882308138`

`perimeter_circle(r)` — вычисляет длину окружности (периметр круга) по радиусу `r`.  
Формула: `c = 2 * r * pi`
Пример: `perimeter_circle(3)` → `18.84955592153876`

---

### square.py
`area_square(a)` — вычисляет площадь квадрата по длине стороны `a`.  
Формула: `S = a²`
Пример: `area_square(4)` → `16`

`perimeter_square(a)` — вычисляет периметр квадрата по длине стороны `a`.  
Формула: `S = 4 * a`
Пример: `perimeter_square(4)` → `16`

---

### rectangle.py
`area_rectangle(a, b)` — вычисляет площадь прямоугольника по сторонам `a` и `b`.  
Формула: `S = a * b`
Пример: `area_rectangle(4, 5)` → `20`

`perimeter_rectangle(a, b)` — вычисляет периметр прямоугольника по сторонам `a` и `b`.  
Формула: `P = 2 * (a + b)`
Пример: `perimeter_rectangle(4, 5)` → `18`

---

### triangle.py
`area_triangle(a, h)` — вычисляет площадь треугольника по длине стороны `a` и высоте `h`.  
Формула: `S = a * b / 2`
Пример: `area_triangle(1, 2)` → `2`

`perimeter_triangle(a, b, c)` — вычисляет периметр треугольника.  
Формула: `P = a + b + c` 
Пример: `perimeter_triangle(3, 4, 5)` → `12`

---

## История изменений
- `a32bc71` — Добавлены rectangle.py и triangle.py с документацией функций  
- `8ba9aeb` — Инициализация проекта: добавлены circle.py и square.py  
- `d078c8d` — Создана папка docs и начата документация















## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah/2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: S = a + b + c