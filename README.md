# Decard Preacher

## Описание

CLI-утилита для преобразования декартовых координат в сферические с поддержкой дробей и корней.

## Особенности

- Поддержка сложных форматов ввода:
  - Дроби: `1/2`, `3/4`
  - Квадратные корни: `√2`, `sqrt(9)`
  - Смешанные выражения: `√3/2`, `1+sqrt(5)`
- Вывод в градусах
- Поддержка 3D-координат

## Установка

```bash
pip install https://github.com/Cewerty/Decart-Preacher.git
```

## Использование

```bash
decart-preacher [X] [Y] [Z]
```

### Примеры

Преобразование простых координат:

```bash
decart-preacher 1 1 1
# r = 1, θ = 54.74°, φ = 45.00°
```

Работа с дробями и корнями:

```bash
decart-preacher "√3/2" "1/2" "0"
# r = 1, θ = 90°, φ = 30°
```

## Разработка

Клонируйте репозиторий:

```bash
git clone https://github.com/Cewerty/Decart-Preacher.git
cd Decart-Preacher
```

Установите зависимости:

```bash
pip install -e .
```
