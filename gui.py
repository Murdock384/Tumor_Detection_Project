import tkinter as tk
from tkinter import ttk, filedialog

root = tk.Tk()
root.title("AI Project")

def load_ct_scan():
    file_path = filedialog.askopenfilename()

def process_ct_scan():
    pass

# Create Frames for different sections
ct_frame = tk.Frame(root)
details_frame = tk.Frame(root)

# Create Labels for image and details sections
image_label = tk.Label(ct_frame ,text="Loaded Image")
details_label = tk.Label(details_frame, text="Result Details")

# Create Buttons for loading and processing CT scans
load_button = tk.Button(ct_frame, text="Load CT Scan", command=load_ct_scan)
process_button = tk.Button(ct_frame, text="Process CT Scan", command=process_ct_scan)

# Create Square Area for Image (just a placeholder)
image_area = tk.Canvas(ct_frame, width=200, height=200, bg="white")
processed_image_area = tk.Canvas(ct_frame, width=200, height=200, bg="white")

# Pack Image Area into CT Frame side by side
image_area.pack(side="left", padx=10, pady=10)
processed_image_area.pack(side="right", padx=10, pady=10)

# Pack Labels and Buttons into CT Frame
image_label.pack(side="top")
load_button.pack(side="left")
process_button.pack(side="left")



# Create Table for Result Details
result_tree = ttk.Treeview(details_frame, columns=("Type of Tumor", "Accuracy", "Detection Result"))
result_tree.heading("#0", text="Type of Tumor")
result_tree.heading("#1", text="Accuracy")
result_tree.heading("#2", text="Detection Result")

# Pack Result Details Table into Details Frame
result_tree.pack(side="top", padx=10, pady=10)

# Pack Frames into root window
ct_frame.pack(side="top", padx=10, pady=10)
details_frame.pack(side="top", padx=10, pady=10)

root.mainloop()


