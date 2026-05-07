from math import pi
from typing import Any


def circle(
    radius: int,
) -> tuple[Any, Any]:
    area = pi * radius * radius
    circumference = 2 * 3.14161 * radius

    return area, circumference


radius = int(input("Enter the radius of the circle: "))

area, circumference = circle(radius)

print(
    f"As per the given radius ({radius}) of the circle:-\nThe Area of the Circle is: {area}\nThe Circumference of the circle is: {circumference}",
)
