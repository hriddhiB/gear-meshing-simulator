import plotly.graph_objects as go


def plot_gears(x1,y1,teeth1,x2,y2,teeth2):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(x=x1,y=y1,mode="lines",name="Gear 1")
    )

    fig.add_trace(
        go.Scatter(x=x2,y=y2,mode="lines",name="Gear 2")
    )

    for tooth in teeth1:

        fig.add_trace(
            go.Scatter(
                x=tooth[0],
                y=tooth[1],
                fill="toself",
                mode="lines",
                showlegend=False
            )
        )

    for tooth in teeth2:

        fig.add_trace(
            go.Scatter(
                x=tooth[0],
                y=tooth[1],
                fill="toself",
                mode="lines",
                showlegend=False
            )
        )

    fig.update_layout(
        width=700,
        height=700,
        xaxis=dict(scaleanchor="y"),
        title="Gear Meshing Simulation",
        showlegend=True
    )

    return fig