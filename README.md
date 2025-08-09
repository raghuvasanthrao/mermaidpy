Alright — I’ll update your **README.md** so it:

* Explains **`.mmd` files**
* Includes the **`utils.py`** helper functions (`save_chart`, `render_to_html`, `branch`)
* Shows **examples for branching and nested branching** using `branch()`
* Mentions that `.mmd` files can be previewed in editors and docs tools

---

## **Updated README.md**

````markdown
# MermaidPy

MermaidPy is a Python library that makes it easy to generate [Mermaid.js](https://mermaid.js.org/) diagrams directly from Python.

With MermaidPy, you can create:
- Flowcharts (TD, LR, BT, RL)
- Branching flowcharts (decision trees)
- Nested branches (branch of a branch)
- Sequence diagrams (basic support)
- Class diagrams (coming soon)

Mermaid.js allows you to render these diagrams in Markdown, documentation tools, and web pages.

---

## 📦 Installation

### From PyPI
```bash
pip install mermaidpy
````

### From GitHub

```bash
pip install git+https://github.com/yourusername/mermaidpy.git
```

---

## 📂 What is `.mmd`?

A `.mmd` file is a **plain text file** containing Mermaid diagram syntax.
Example: `flowchart TD` followed by your nodes and edges.

Example `example_chart.mmd`:

```
flowchart TD
A[Start]
B[Process]
C[End]
A --> B
B --> C
```

You can:

* Open it in [Mermaid Live Editor](https://mermaid.live/)
* Use it in GitHub Markdown
* Embed it in static site generators (MkDocs, Docusaurus, etc.)
* Preview it in editors like VS Code (with Mermaid plugin)

---

## 🚀 Quick Start

```python
from mermaidpy.chart import MermaidChart

chart = MermaidChart(chart_type="flowchart", direction="TD")
chart.add_node("A", "Start")
chart.add_node("B", "Process")
chart.add_node("C", "End")
chart.add_edge("A", "B", "step 1")
chart.add_edge("B", "C", "step 2")

print(chart.render())
```

**Output Mermaid code:**

```
flowchart TD
A[Start]
B[Process]
C[End]
A -->|step 1| B
B -->|step 2| C
```

---

## 🛠 Using Utility Functions

The `utils.py` file includes:

* `save_chart(chart, filename)` → Saves Mermaid code to `.mmd`
* `render_to_html(chart, filename)` → Creates a previewable HTML file
* `branch(chart, from_node, branches)` → Creates branches and nested branches

---

### 1️⃣ Save a Chart as `.mmd`

```python
from mermaidpy.chart import MermaidChart
from mermaidpy.utils import save_chart

chart = MermaidChart("flowchart", "LR")
chart.add_node("A", "Start")
chart.add_node("B", "Do Work")
chart.add_edge("A", "B")

save_chart(chart, "my_chart")  # Saves as my_chart.mmd
```

---

### 2️⃣ Render to HTML for Preview

```python
from mermaidpy.utils import render_to_html

render_to_html(chart, "my_chart")  # Saves as my_chart.html
# Open in browser to view
```

---

### 3️⃣ Branching Flowchart (Decision Tree)

```python
from mermaidpy.chart import MermaidChart
from mermaidpy.utils import branch

chart = MermaidChart("flowchart", "TD")
chart.add_node("A", "Start")

branch(chart, "A", [
    ("B", "Option 1"),
    ("C", "Option 2")
])

print(chart.render())
```

**Output:**

```
flowchart TD
A[Start]
B[Option 1]
C[Option 2]
A --> B
A --> C
```

---

### 4️⃣ Nested Branches (Branch of a Branch)

```python
chart = MermaidChart("flowchart", "TD")
chart.add_node("A", "Start")

branch(chart, "A", [
    ("B", "Path 1", [
        ("B1", "Path 1A"),
        ("B2", "Path 1B")
    ]),
    ("C", "Path 2")
])

print(chart.render())
```

**Output:**

```
flowchart TD
A[Start]
B[Path 1]
B1[Path 1A]
B2[Path 1B]
C[Path 2]
A --> B
B --> B1
B --> B2
A --> C
```

---

## 💡 Tips

* MermaidPy **generates code** — rendering is done by Mermaid.js in browsers or Markdown processors.
* Save `.mmd` files to reuse diagrams in docs.
* Use `render_to_html()` for instant browser preview.

---

## 📜 License

This project is licensed under the MIT License.

---

## 🤝 Contributing

1. Fork the repo
2. Create a new branch: `git checkout -b feature-name`
3. Make changes and commit: `git commit -m 'Added new feature'`
4. Push to branch: `git push origin feature-name`
5. Open a Pull Request

```

---

I’ve now included:
- `.mmd` explanation
- Utility functions section
- Example of **branch** and **nested branch**
- Saving & HTML preview instructions

If you want, I can also add **Mermaid Live Editor integration** so that `render_to_html()` automatically opens the preview in your default browser after saving. That would make it even smoother for testing.  

Do you want me to add that?
```
