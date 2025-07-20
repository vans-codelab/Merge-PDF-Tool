import os
import re
import pymupdf
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD

VERSION = "v1.0"
BUTTON_WIDTH = 13
FIELD_WIDTH = 80
# pdf icon from
# https://de.freepik.com/icon/pdf_13310078#fromView=search&page=1&position=73&uuid=9083c303-0ec3-4f6d-9cf6-9c6592339a35

# ---- PDF Functions ------------------------------------------------------
def add_file_to_listbox(file):
    """Makes sure that selected file is in PDF-Format to enable merge.\n
       - If file is a PDF, then file is added to listbox.\n
       - If file is not a PDF, then an error message is displayed to the user.
    """

    # If filename contains spaces, then { and } are automatically added -> Remove them from filename
    file = file.lstrip("{")
    file = file.rstrip("}")

    if file.endswith(".pdf"):
        # If file is a PDF -> Add to listbox
        listbox_pdf.insert(tk.END, file)
        return True
    else:
        # If file is NOT a PDF -> Error
        messagebox.showinfo(title="ERROR - No PDF", message="The selected file has to be a PDF.")
        return False


def dragndrop_to_listbox(file_data):
    """When user selects a single PDF-File or multiple PDF-Files at once,
    then the files are added to the listbox correctly"""

    # Get a list of PDF-Files (ignore other file formats) - Ensures that multiple files are added correctly
    matches = re.findall(r'\{([^{}]*?\.pdf)\}|\b([^\s{}]*?\.pdf)\b', file_data)
    pdfs = [m[0] or m[1] for m in matches]

    # Add PDF-File(s) to listbox
    for pdf in pdfs:
        add_file_to_listbox(pdf)


def select_file():
    """Enables user to select a PDF-File from the directory for merging."""
    filename = filedialog.askopenfilename()
    # If user selects "Select Folder" button in dialog (and not "Cancel" button, would lead to empty filename)
    if filename != "":
        add_file_to_listbox(filename)

def remove_selected_file():
    """Removes PDF-File that is selected by user."""
    selected_file_index = listbox_pdf.curselection()
    listbox_pdf.delete(selected_file_index)

def remove_all_files():
    """Removes all PDF-Files in the list"""
    listbox_pdf.delete(0, tk.END)

def select_folder():
    """Enables user to change the output folder where the merged file will be saved."""
    folder = filedialog.askdirectory(initialdir=current_dir)
    if folder != "":  # If user does not select "Cancel" button in dialog
        entry_save_to.delete(0, tk.END)
        entry_save_to.insert(0, folder)

def merge_pdfs():
    """Merges PDF-Files."""
    list_of_pdfs = listbox_pdf.get(0, tk.END)

    if len(list_of_pdfs) <= 1:
        messagebox.showinfo(title="ERROR: Cannot Merge",
                            message="Please select at least 2 PDF-Files to merge.")
    else:
        # Create an empty target file
        merged_files = pymupdf.open()

        # Insert all PDF-files to be merged
        for pdf in list_of_pdfs:
            file = pymupdf.open(pdf)
            merged_files.insert_pdf(file)
            file.close()

        # Check where to save the merged file
        folder_path = entry_save_to.get()
        file_name = entry_file_name.get()
        destination = f"{folder_path}\{file_name}"

        if file_name.strip(" ").endswith(".pdf"):
            try:
                # Merge PDF-files and save
                merged_files.save(destination)
                messagebox.showinfo(title="Merge Done.",
                                    message="Finished. Your merged file has been saved.")
            except pymupdf.mupdf.FzErrorSystem:
                messagebox.showinfo(title="ERROR: Folder Path",
                                    message="Cannot find folder.\n Please check folder path under 'Save to'.")
        else:
            messagebox.showinfo(title="ERROR: Output File Type",
                                message="Output File Name has to be .pdf")


# ---- Listbox events (User can move PDF-Files within Listbox via drag and drop) -----------------------------------
drag_file = {"index": None, "value": None}

def on_start_drag(event):
    """Get index (position) and value (file name) of dragged PDF-File."""
    global drag_file
    drag_file["index"] = listbox_pdf.nearest(event.y)
    drag_file["value"] = listbox_pdf.get(drag_file["index"])

def on_drop(event):
    """Moves the dragged file to the new position."""
    # Get new position
    drop_index = listbox_pdf.nearest(event.y)
    if drop_index != drag_file["index"]:
        # Remove file from old position
        listbox_pdf.delete(drag_file["index"])
        # Add file to new position
        listbox_pdf.insert(drop_index, drag_file["value"])


# ---- User Interface ------------------------------------------------------
window_dragndrop = TkinterDnD.Tk()
window_dragndrop.title("Merge PDF")
window_dragndrop.config(padx=50, pady=40)

# Image
canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
pdf_img = tk.PhotoImage(file="pdf_icon.png")
canvas.create_image(100, 90, image=pdf_img)
canvas.grid(column=0, row=0)

# PDFs field
label_pdfs = tk.Label(text="PDF-Files:")
label_pdfs.grid(column=0, row=1, sticky="w")

listbox_pdf = tk.Listbox(window_dragndrop, height=7, width=FIELD_WIDTH)  # Listbox + dragging and dropping files into listbox
listbox_pdf.drop_target_register(DND_FILES)
#listbox_pdf.dnd_bind('<<Drop>>', lambda event : add_file_to_listbox(event.data))
listbox_pdf.dnd_bind('<<Drop>>', lambda event : dragndrop_to_listbox(event.data))
listbox_pdf.grid(column=0, row=2, rowspan=3, sticky="w")

listbox_pdf.bind("<ButtonPress-1>", on_start_drag)  # Bind events to listbox, enables moving files within listbox
listbox_pdf.bind("<ButtonRelease-1>", on_drop)

scrollbar_vertical = tk.Scrollbar(orient="vertical", command=listbox_pdf.yview)  # Vertical Scrollbar for listbox
listbox_pdf.configure(yscrollcommand=scrollbar_vertical.set)
scrollbar_vertical.grid(column=1, row=2, rowspan=3, sticky="n,s")

scrollbar_horizontal = tk.Scrollbar(orient="horizontal", command=listbox_pdf.xview)  # Horizontal Scrollbar for listbox
listbox_pdf.configure(xscrollcommand=scrollbar_horizontal.set)
scrollbar_horizontal.grid(column=0, row=5, sticky="e,w")

button_select_file = tk.Button(width=BUTTON_WIDTH, text="Open PDF-File", command=select_file)
button_select_file.grid(column=2, row=2, sticky="w", padx=(10, 0))

button_remove_file = tk.Button(width=BUTTON_WIDTH, text="Remove File", command=remove_selected_file)
button_remove_file.grid(column=2, row=3, sticky="w", padx=(10, 0), pady=(10, 0))

button_remove_all = tk.Button(width=BUTTON_WIDTH, text="Remove All Files", command=remove_all_files)
button_remove_all.grid(column=2, row=4, sticky="w", padx=(10, 0))

# Save to
label_save_to = tk.Label(text="Save to (Folder Path):")
label_save_to.grid(column=0, row=6, sticky="w", pady=(20, 0))

current_dir = os.path.dirname(__file__)  # current directory where this python file is located
entry_save_to = tk.Entry(width=FIELD_WIDTH)
entry_save_to.insert(0, current_dir)
entry_save_to.grid(column=0, row=7, sticky="w")

button_select_folder = tk.Button(width=BUTTON_WIDTH, text="Open Folder", command=select_folder)
button_select_folder.grid(column=2, row=7, sticky="w", padx=(10, 0))

# Save as (file name)
label_save_as = tk.Label(text="Save as (File Name):")
label_save_as.grid(column=0, row=8, sticky="w", pady=(10, 0))

entry_file_name = tk.Entry(width=FIELD_WIDTH)
entry_file_name.insert(0, "merged.pdf")
entry_file_name.grid(column=0, row=9, sticky="w")

# Merge button
button_merge = tk.Button(text="Merge PDF", command=merge_pdfs, bg="#E5D9F2")
button_merge.config(padx=50, pady=15)
button_merge.grid(column=0, row=10, pady=(30, 0))

# Tool Version
label_version = tk.Label(text=VERSION, fg="grey")
label_version.grid(column=2, row=11, pady=(30, 0), sticky="e")

window_dragndrop.mainloop()
