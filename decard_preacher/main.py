"""Cli-программа для перевода из Декартовых координат в сферические.

Основной функционал реализован в функции convert(), которая потом преобразуется в консольную команду.

Для её выполнения используеться parse_number, которая выполняет парсинг вводимых точек
и преобразует из строки в десятичную строку.
"""
import math
import re

import typer

app = typer.Typer()

def parse_number(input_str: str) -> float:
    """Функция для парсинга числового значения из CLI-параметра.

    Args:
        input_str (str): CLI-параметр из которого парсится значение

    Raises:
        ValueError: Ошибка, которая возникает, если пользователь
        передает параметр, который нельзя спарсить в числовое значение.

    Returns:
        float: Спаршеное значение из параметра.

    """
    input_str = input_str.strip().lower()

    if "/" in input_str:
        numerator, denominator = input_str.split("/")
        return parse_number(numerator) / parse_number(denominator)

    sqrt_match = re.match(r"^(√|sqrt\()\s*([0-9\.]+)\s*\)?$", input_str)
    if sqrt_match:
        number = sqrt_match.group(2)
        return math.sqrt(float(number))

    try:
        return float(input_str)
    except ValueError as err:
        raise ValueError(f"Неверный формат числа: {input_str}") from err

@app.command()
def convert(x: str,
         y: str,
         z: str) -> None:
    """Функция для преобразования координат из декартовых в сферические.

    Args:
        x (str): Кооридината по оси X
        y (str): Координата по оси Y
        z (str): Координата по оси Z

    """
    x_parsed: float
    y_parsed: float
    z_parsed: float
    x_parsed, y_parsed, z_parsed = parse_number(x), parse_number(y), parse_number(z)
    r = math.sqrt(x_parsed**2 + y_parsed**2 + z_parsed**2)
    if r == 0:
        raise ZeroDivisionError("Данные значения не подходят для конвертации в Сферическую систему координат")
    teta = math.acos(z_parsed/r)
    phi = math.atan2(y_parsed, x_parsed)
    typer.echo(f"r = {r:.0f}, θ = {math.degrees(teta):.0f}°, ϕ = {math.degrees(phi):.0f}°")


if __name__ == "__main__":
    app()
