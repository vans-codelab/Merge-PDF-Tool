# Merge PDF Tool
A simple and user-friendly tool to merge multiple PDF files into a single document.
<br><br>

### How it Works
1. Click the **Open PDF-File** button or simply drag and drop PDF files into the window. 
2. *(Optional)* Change the default output path or rename the final PDF-file. 
3. Click **Merge PDF** to merge all selected PDFs into one file - done! 
<br><br>

### Screenshots
![The Merge PDF Tool](/screenshots/PDF_Merge_UI.PNG)

### Features
- Add PDF-Files via the **Open PDF-File** button.
- Or drag and drop files into the window. 
- Reorder files via drag and drop.
- Remove one or all files in the list
- Choose a custom output folder.
- Rename the final PDF file.
- Helpful error messages:
  - Merging requires at least two PDF files.
  - Only PDF files are supported.
  - Output folder must exist.
  - Output file name must end with `.pdf`
- Built with Tkinter (standard GUI library in Python)
<br><br>

### Requirements
- **Programming Language:**
  Developed and tested with Python 3.11.  
  Download Python at: https://www.python.org/downloads/

- **Python Packages:**
  See [requirements.txt](requirements.txt) for all dependencies.
<br><br>

### Usage
1. **Download Files:**
   
   Click on the green "Code" button on GitHub and download the repository as a ZIP file.  
   Extract the folder and make sure all Python files are in the same folder
   
2. **Open the Project Folder**
   
   Open the command prompt (CMD, Terminal, or PowerShell) and navigate to the folder where the files were extracted.  

   Example:

       cd "C:\Merge_PDF\"

4. *(Optional, but recommended)*
   
   **Create a Virtual Environment**
   To avoid conflicts with other Python packages on the system, is is recommended to use a virtual environment.

   
   On windows:
  
       python -m venv venv
       venv\Scripts\activate  # On Windows

    On macOS/Linux:
       
       python -m venv venv
       source venv/bin/activate  # On macOS/Linux

3. **Install Required Packages**
   
   Make sure Python is installed.
   `pip` comes bundled with Python, so it should be possible to install all required packages by running:

       pip install -r requirements.txt

5. **Run the Program:**
   
   Run **main.py** to start the program:
  
       python main.py

### Context
While I was looking for a PDF merging tool, I thought: Why not create my own? 
I wanted to build a simple and user-friendly tool that allows users to customize the output — such as the file name, file order, or the save location.
Designing and implementing the tool was both a fun and rewarding challenge. 
Especially integrating a drag-and-drop functionality and handling error cases were some of the more challenging tasks. 
Overcoming them added a lot of value to the overall project.

I'm happy with how the tool turned out and hope it’s helpful to others as well!
<br><br>

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
