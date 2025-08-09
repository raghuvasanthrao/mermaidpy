import os
from .chart import MermaidChart

def save_chart(chart: MermaidChart, filename: str):
    """
    Save Mermaid chart code to a file (.mmd).

    Parameters:
    chart (MermaidChart): The chart instance.
    filename (str): Output file path.
    """
    if not filename.endswith(".mmd"):
        filename += ".mmd"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(chart.render())


def render_to_html(chart: MermaidChart, filename: str):
    """
    Save Mermaid chart as a standalone HTML file for preview.

    Parameters:
    chart (MermaidChart): The chart instance.
    filename (str): Output HTML file path.
    """
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Mermaid Chart</title>
        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ startOnLoad: true }});
        </script>
    </head>
    <body>
        <div class="mermaid">
{chart.render()}
        </div>
    </body>
    </html>
    """

    if not filename.endswith(".html"):
        filename += ".html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_template)


def branch(chart: MermaidChart, from_node: str, branches: list):
    """
    Create branches from a given node, optionally with nested branches.

    Parameters:
    chart (MermaidChart): The chart instance.
    from_node (str): Starting node ID.
    branches (list): List of tuples in format:
                     (node_id, label, [sub_branches])
                     sub_branches is optional.
    Example:
    branch(chart, "A", [
        ("B", "Path 1", [
            ("B1", "Path 1A"),
            ("B2", "Path 1B")
        ]),
        ("C", "Path 2")
    ])
    """
    for branch_item in branches:
        if len(branch_item) >= 2:
            node_id, label = branch_item[0], branch_item[1]
            chart.add_node(node_id, label)
            chart.add_edge(from_node, node_id)
            if len(branch_item) == 3 and isinstance(branch_item[2], list):
                branch(chart, node_id, branch_item[2])
