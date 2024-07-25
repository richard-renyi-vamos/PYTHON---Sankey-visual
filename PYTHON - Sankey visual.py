import plotly.graph_objects as go

# Define the nodes and their labels
nodes = {
    'labels': ["Source A", "Source B", "Source C", "Target X", "Target Y", "Target Z"],
    'color': ["blue", "blue", "blue", "green", "green", "green"]
}

# Define the links between the nodes
links = {
    'source': [0, 1, 0, 2, 2, 2],  # Indices of the source nodes
    'target': [3, 3, 4, 4, 5, 5],  # Indices of the target nodes
    'value':  [8, 4, 2, 8, 4, 2]   # Values of the links
}

# Create the Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=nodes['labels'],
        color=nodes['color']
    ),
    link=dict(
        source=links['source'],
        target=links['target'],
        value=links['value']
    )
)])

# Update layout for better visuals
fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)

# Show the diagram
fig.show()
