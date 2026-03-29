# Merge PDF Tool

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![GUI](https://img.shields.io/badge/GUI-Tkinter-yellowgreen)
![Function](https://img.shields.io/badge/Feature-PDF%20Merge-red)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A simple and user-friendly tool to merge multiple PDF files into a single document.


## Table of contents

- [Screenshots](#screenshots)
- [Features](#features)
- [Requirements (for developers)](#requirements-for-developers)
- [Installation & Setup (for developers)](#installation--setup-for-developers)
- [Quick start (for users)](#quick-start-for-users)
- [How to use](#how-to-use)
- [Context](#context)
- [License](#license)


## Screenshots
![The Merge PDF Tool](/screenshots/PDF_Merge_UI.png)


## Features
- Select PDF files
- Drag and drop files into the application window
- Reorder files before merging
- Remove individual files or clear the entire list
- Choose the output folder for the merged PDF
- Rename the final PDF file before saving
- Display helpful error messages for common issues:
  - At least two PDF files are required for merging
  - Only PDF files are supported
  - The selected output folder must exist
  - A file must be selected before it can be removed
- Built with Tkinter (a standard GUI library in Python)


## Requirements (for developers)
- **Programming Language:**
  Developed and tested with Python 3.11.  
  Download Python at: https://www.python.org/downloads/

- **Python Packages:**
  See [requirements.txt](requirements.txt) for all dependencies.

  
## Installation & Setup (for developers)
### 1. Download the project

**Option A: Clone via Git**
```bash
git clone https://github.com/vans-codelab/Merge-PDF-Tool
cd Merge-PDF-Tool
```

**Option B: Download ZIP from GitHub**  
Download ZIP from GitHub and extract it. Then navigate to the extracted folder with the following command:
```bash
cd <path-to-extracted-project-folder>   
```

### 2. Create a virtual environment and activate it
Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```
macOS/Linux:
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install required packages
```bash
pip install -r requirements.txt
```
### 4. Run the application
```bash
python main.py
```


## Quick start (for users)
1. Go to the "Releases" section of this repository and download the latest .zip file.
2. Unzip the downloaded ZIP file (Right-click on the downloaded file and select "Extract All").
3. Open the extracted folder.
4. Double-click "Merge-PDF-Tool.exe" to start the application. It may take a few seconds to launch.


## How to use
  - **Add files**   →  Click "Add File" or drag & drop PDFs into the field.
  - **Reorder**     →  Hold & drag a file to change its position.
  - **Remove**      →  Use "Remove" buttons to delete individual or all files.
  - **Choose**      →  Rename the output file and select the folder where it will be saved.
  - **Merge**       →  Click "Merge" to combine the files into a single document.


## Context
While I was looking for a PDF merging tool, I thought: Why not create my own? 

I wanted to build an offline tool, that is simple and user-friendly.
Designing and implementing the tool was both a fun and rewarding challenge. 
Especially integrating a drag-and-drop functionality and handling error cases were some of the more challenging tasks. 
Overcoming them added a lot of value to the overall project.

As a result, the project evolved into a practical offline tool that may also be useful for others who are looking for a simple way to merge PDF files locally.


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
