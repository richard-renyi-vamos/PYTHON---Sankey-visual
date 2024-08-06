import tkinter as tk
from tkinter import simpledialog, messagebox
import plotly.graph_objects as go
import plotly.io as pio

# Function to generate the Sankey diagram
def create_sankey(nodes, links):
    fig = go.Figure(go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=nodes
        ),
        link=dict(
            source=links["source"],
            target=links["target"],
            value=links["value"]
        )
    ))

    fig.update_layout(title_text="Customizable Sankey Diagram", font_size=10)
    pio.show(fig)

# Function to get user input and generate the Sankey diagram
def generate_diagram():
    try:
        num_nodes = int(simpledialog.askstring("Input", "Enter the number of nodes:"))
        nodes = [simpledialog.askstring("Input", f"Enter name for node {i}:") for i in range(num_nodes)]
        
        num_links = int(simpledialog.askstring("Input", "Enter the number of links:"))
        links = {"source": [], "target": [], "value": []}
        
        for i in range(num_links):
            source = int(simpledialog.askstring("Input", f"Enter source node index for link {i}:"))
            target = int(simpledialog.askstring("Input", f"Enter target node index for link {i}:"))
            value = int(simpledialog.askstring("Input", f"Enter value for link {i}:"))
            links["source"].append(source)
            links["target"].append(target)
            links["value"].append(value)
        
        create_sankey(nodes, links)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main application window
root = tk.Tk()
root.title("Sankey Diagram Generator")

# Add a button to trigger the diagram generation
generate_button = tk.Button(root, text="Generate Sankey Diagram", command=generate_diagram)
generate_button.pack(pady=20)

# Run the GUI event loop
root.mainloop()
