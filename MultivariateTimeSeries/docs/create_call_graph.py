"""This scripts generate the call graph of the source code by using the
code2flow tool.
"""

import constants
from utils import utils

# 假设 'path_to_markdown' 可以是文件或文件夹
# path_to_markdown = (constants.project_root_path /
#                     "notebook/time-series-gan-with-pytorch.ipynb")
print(constants.project_root_path)
path_to_markdown = constants.project_root_path / "notebook"
target_folder = constants.project_root_path / "docs/html"
converter = utils.get_notebook_converter(
    path_to_markdown,
    target_folder,
    additional_pdf=True
)
converter.convert()
