# Getting Started with MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

## Get started with MkDocs

1. Install mkdocs by running the following command in your terminal:

    ```bash
    pip install mkdocs
    pip install "mkdocstrings[python]"
    pip install mkdocs-material
    ```

2. create a new mkdocs using the exist project, excute the following command in your project root directory:

    ```bash
    mkdocs new .
    ```

    After this command, a new mkdocs.yml and docs/index.md will be created.

3. Use the following command to start the live-reloading docs server, and this page will be available at <http://127.0.0.1:8000/>

    ```bash
    mkdocs serve
    ```

## Documnents for build python project documents with mkdocs

<https://realpython.com/python-project-documentation-with-mkdocs/#step-5-build-your-documentation-with-mkdocs>
