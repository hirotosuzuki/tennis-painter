import copy

import plotly.graph_objects as go

from tennis_painter.schemas import Line, Point


def draw_point(
    self,
    x: list[float],
    y: list[float],
    name: str,
    fill: bool = True,
    color: str = "crimson",
):
    opacity = 1 if fill else 0.4
    result = "IN" if fill else "OUT"
    self.fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            marker=dict(color=color, size=9),
            mode="markers",
            opacity=opacity,
            name=name,
        )
    )


def draw_point(fig_raw: go.Figure, point: Point, color: str = "black", opacity: float = 1) -> go.Figure:
    fig = copy.deepcopy(fig_raw)
    trace = go.Scatter(
        x=point.x,
        y=point.y,
        marker=dict(color=color, size=9),
        mode="markers",
        opacity=opacity,
    )
    fig.add_trace(trace)
    return fig


def draw_line(fig: go.Figure, line: Line, dash: str = "solid", color: str = "black", width: int = 2):
    fig.add_shape(
        dict(
            type="line",
            line=dict(dash=dash),
            x0=line.p1.x,
            y0=line.p1.y,
            x1=line.p2.x,
            y1=line.p2.y,
            xref="x",
            yref="y",
            line_color=color,
            line_width=width,
        )
    )
    return fig


def draw_rectangle(fig: go.Figure):
    pass


def draw_court(fig: go.Figure):
    pass
