# Requirements

If you have any pip requirements that need to be installed in the container then create a file called `requirements.txt` in this directory and add our requirements in a standard manor.
The requirements will be installed when the container is built via `pip install -r requirements.txt`.

Generally speaking this is not necessary as any dependencies set in the `pyproject.toml` file will be installed automatically by Poetry. This if for those edge cases that may occur in your projects.
