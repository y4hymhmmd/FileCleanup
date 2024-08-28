# File Cleanup Utility

## Description

A simple Python utility designed to clean up temporary files, system caches, and other unnecessary files from your Windows system. This script performs various cleanup tasks and provides a user-friendly interface to monitor progress.

## Features

- Deletes temporary files and system caches.
- Clears browser cache for Google Chrome and Mozilla Firefox.
- Removes log files, memory dumps, and other unnecessary files.
- Provides a progress bar to show cleanup progress.
- Displays a completion message with copyright information.

## Prerequisites

- Python 3.x installed on your system.
- `tkinter` library (included with Python).
- Administrative privileges to run the script.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/y4hymhmmd/FileCleanup
    ```

2. Navigate to the project directory:

    ```bash
    cd FileCleanup
    ```

3. Ensure you have Python installed and configured correctly.

## Usage

1. Run the script directly by double-clicking `FileCleanup.pyw` or execute it from the command line:

    ```bash
    python FileCleanup.pyw
    ```

2. The script will execute various cleanup commands and display a progress bar.

3. Once completed, a message box will appear indicating that the files have been cleaned and will show a copyright notice.

## Customization

- You can modify the list of commands in the `run_commands` function to suit your cleanup needs.
- To change the log file location, update the `write_log` function to specify a different path.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to the Python and Tkinter communities for their contributions and support.
- Special thanks to [Script by Cloudy](https://github.com/y4hymhmmd/) for the copyright design.

