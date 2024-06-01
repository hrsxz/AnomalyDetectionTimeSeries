要将 Jupyter Notebook （`.ipynb` 文件）转换为 HTML 文件，你可以使用 `nbconvert` 工具，这是一个非常流行且强大的工具，用于转换 Jupyter 笔记本。以下是如何使用 `nbconvert` 将 Jupyter Notebook 转换为 HTML 的步骤：

### 安装 nbconvert
首先，确保你已经安装了 `nbconvert`。如果未安装，你可以通过 pip 安装它：

```bash
pip install nbconvert
```

### 使用 nbconvert 命令行工具
一旦安装了 `nbconvert`，你可以直接从命令行使用它来将 Notebook 转换为 HTML。打开命令行工具，然后使用以下命令：

```bash
jupyter nbconvert --to html /path/to/your/Notebook.ipynb
```

这里的 `/path/to/your/Notebook.ipynb` 是你的 Jupyter Notebook 文件的路径。这条命令会在相同的目录下生成一个 HTML 文件，文件名与 Notebook 相同。

### 在 Python 脚本中使用 nbconvert
如果你希望在 Python 脚本中进行这种转换，你可以使用 `nbconvert` 的 Python API 来实现。这对于自动化任务特别有用。下面是一个示例脚本，展示了如何在 Python 中执行这个转换：

```python
# 导入 nbconvert 的相关模块
from nbconvert import HTMLExporter
import nbformat
from pathlib import Path

def convert_notebook_to_html(notebook_path, output_path):
    # 读取 Notebook 文件
    notebook_path = Path(notebook_path)
    notebook = nbformat.read(notebook_path, as_version=4)

    # 创建一个 HTML 导出器
    html_exporter = HTMLExporter()
    html_exporter.template_name = 'classic'

    # 导出 HTML
    (body, resources) = html_exporter.from_notebook_node(notebook)

    # 将 HTML 写入文件
    output_path = Path(output_path)
    output_path.write_text(body, encoding='utf-8')
    print(f"HTML has been saved to {output_path}")

# 使用示例
convert_notebook_to_html('/path/to/your/Notebook.ipynb', '/path/to/output/Notebook.html')
```

这段代码首先读取指定路径的 Notebook 文件，然后使用 `nbconvert` 的 `HTMLExporter` 来生成 HTML 内容，并将其保存到指定的输出路径。

### 注意
确保路径是正确的，并且 Python 环境中安装了必要的包，如 `nbformat` 和 `nbconvert`。如果有任何包缺失，可以使用 `pip` 安装它们。

通过以上方法，你可以轻松地将 Jupyter Notebook 转换成 HTML 文件，无论是通过命令行还是通过编程方式。这对于分享、发布或存档 Notebook 的内容非常有用。
