class MermaidChart:
    """
    A helper class to build Mermaid.js diagrams in Python.
    """

    def __init__(self, chart_type="flowchart", direction="TD"):
        """
        Initialize a Mermaid chart.

        Parameters:
        chart_type (str): Type of Mermaid diagram ('flowchart', 'sequenceDiagram', etc.)
        direction (str): Direction for flowcharts ('TD', 'LR', 'BT', 'RL')
        """
        self.chart_type = chart_type
        self.direction = direction
        self.lines = []

    def add_node(self, node_id, label=None, shape="[]"):
        """
        Add a node to the chart.

        Parameters:
        node_id (str): Unique node identifier (e.g., "A")
        label (str): Optional label for the node
        shape (str): Mermaid shape notation ('[]', '()', '{}', '(())', '[[ ]]', etc.)
        """
        if label:
            # Extract opening and closing parts from the shape, e.g., "()", "[]", "{}"
            if len(shape) >= 2 and shape[0] in "([{<" and shape[-1] in ")]}>":
                open_char, close_char = shape[0], shape[-1]
                self.lines.append(f'{node_id}{open_char}{label}{close_char}')
            else:
                # Fallback to square brackets if shape format is invalid
                self.lines.append(f'{node_id}[{label}]')
        else:
            self.lines.append(f'{node_id}')


    def add_edge(self, from_id, to_id, text=None):
        """
        Add an edge between two nodes.

        Parameters:
        from_id (str): Starting node ID
        to_id (str): Ending node ID
        text (str): Optional edge label
        """
        if text:
            self.lines.append(f"{from_id} -->|{text}| {to_id}")
        else:
            self.lines.append(f"{from_id} --> {to_id}")

    def render(self):
        """
        Generate the Mermaid chart string.
        """
        output = []
        if self.chart_type == "flowchart":
            output.append(f"flowchart {self.direction}")
        else:
            output.append(self.chart_type)
        output.extend(self.lines)
        return "\n".join(output)
