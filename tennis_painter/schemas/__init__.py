from pydantic import BaseModel


class Point(BaseModel):
    x: int
    y: int


class Line(BaseModel):
    p1: Point
    p2: Point
