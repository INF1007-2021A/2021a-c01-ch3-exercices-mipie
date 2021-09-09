#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    return math.sqrt(a)


def square(a: float) -> float:
    return a**2


def average(a: float, b: float, c: float) -> float:
    liste=[a,b,c]
    moyenne= sum(liste)/len(liste)
    return moyenne


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    radian= math.radians(angle_degs)
    x = angle_mins * math.pi/(60*180)
    y = angle_secs * math.pi/(180*3600)
    angle_total = radian + x + y
    return angle_total


def to_degrees(angle_rads: float) -> tuple:
    degres_total = math.radians(angle_rads)
    degres= math.floor(degres_total)
    reste_degres = degres_total - degres

    minutes_total = reste_degres * 60
    minutes = math.floor(minutes_total)
    reste_minutes = minutes_total - minutes

    secondes_total = reste_minutes * 60

    return degres, minutes,secondes_total


def to_celsius(temperature: float) -> float:
    celsius = (temperature - 32)/1.8
    return celsius


def to_farenheit(temperature: float) -> float:
    farenheit = (temperature-32)*5/9
    return farenheit


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 180 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
