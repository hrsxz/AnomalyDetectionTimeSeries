from typing import Dict, List

import plotly.graph_objs as go


def plot_3d_scatter(
    x: List[float],
    y: List[float],
    z: List[float],
    color_list: List[str],
    hover_text: List[str],
    title: str = "Title",
    xaxis_title: str = "1st Component",
    yaxis_title: str = "2nd Component",
    zaxis_title: str = "3rd Component",
    camera_pos: Dict[str, float] = None,
    width: int = 700,
    height: int = 350,
) -> None:
    """This function plot the data in 3d scatter format.

    Args:
        x (list): data for x axis
        y (list): data for y axis
        z (list): data for z axis
        color_list (list): list with the color for each point
        hover_text (list): list with the text to be shown when hovering over a point
        title (str): title of the plot
        xaxis_title (str): title of the x axis
        yaxis_title (str): title of the y axis
        zaxis_title (str): title of the z axis
        camera_pos (dict): position of the camera
        width (int): width of the plot
        height (int): height of the plot
    """
    fig = go.Figure()

    trace = go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode="markers",
        marker={
            "size": 5,
            "color": color_list,
            "colorscale": "Viridis",
            "opacity": 0.8,
        },
        text=hover_text,
        hoverinfo="text",
    )

    fig.add_traces([trace])

    if camera_pos is None:
        camera_pos = {"x": 0.2, "y": 0.4, "z": 0.5}

    fig.update_layout(
        title=title,
        width=width,
        height=height,
        scene={
            "xaxis_title": xaxis_title,
            "yaxis_title": yaxis_title,
            "zaxis_title": zaxis_title,
            "camera": {
                "eye": camera_pos,
                "center": {"x": 0, "y": 0, "z": 0},
            },
        },
    )

    fig.show()
