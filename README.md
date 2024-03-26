
# searchpypi

**searchpypi** is a Python script that allows you to search for Python packages on the Python Package Index (PyPI) and open the search results in your default web browser.

## Usage

To search for a Python package, run the script from the terminal followed by the package name:

```bash
searchpypi <package_name>
```

Replace `<package_name>` with the name of the Python package you want to search for.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your_username/searchpypi.git
```

2. Navigate to the directory containing the script:

```bash
cd searchpypi
```

3. Make the script executable:

```bash
chmod +x searchpypi.py
```

4. Optionally, create a symbolic link to make the script executable from anywhere in the terminal:

```bash
ln -s /path/to/searchpypi.py /usr/local/bin/searchpypi
```

Replace `/path/to/searchpypi.py` with the full path to your **searchpypi.py** script.

## Setup

Before using the script, ensure that you have Python installed on your system. You can download and install Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

## Creating a Symbolic Link

To make the script executable from anywhere in the terminal, you can create a symbolic link to the script. Here's how to do it:

1. Open a terminal.

2. Navigate to the directory containing the **searchpypi.py** script.

3. Run the following command to create a symbolic link:

```bash
ln -s /path/to/searchpypi.py /usr/local/bin/searchpypi
```

Replace `/path/to/searchpypi.py` with the full path to your **searchpypi.py** script.

4. Ensure that both the script file and the symbolic link have execute permissions. You can do this by running the following commands:

```bash
chmod +x /path/to/searchpypi.py
chmod +x /usr/local/bin/searchpypi
```

5. Once the symbolic link is created and permissions are set, you can run the script from anywhere in the terminal using the `searchpypi` command.
