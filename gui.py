# import tkinter as tk
# from tkinter import ttk ,filedialog
# root = tk.Tk()
# root.title("AI Project")
#
# def load_ct_scan():
#     file_path = filedialog.askopenfilename()
#
# def process_ct_scan():
#     pass
#
#
# # Create Frames for different sections
# image_frame = tk.Frame(root)
# results_frame = tk.Frame(root)
# details_frame = tk.Frame(root)
#
# # Create Labels for different sections
# image_label = tk.Label(image_frame, text="Loaded Image")
# results_label = tk.Label(results_frame, text="Results")
# details_label = tk.Label(details_frame, text="Result Details")
#
# # Create Buttons for loading and processing CT scans
# load_button = tk.Button(image_frame, text="Load CT Scan", command=load_ct_scan)
# process_button = tk.Button(results_frame, text="Process CT Scan", command=process_ct_scan)
#
# # Create Table for Result Details (you might need a different library for this)
# # Example with Tkinter's Treeview:
# result_tree = tk.ttk.Treeview(details_frame, columns=("Type of Tumor", "Accuracy", "Detection Result"))
# result_tree.heading("#0", text="Type of Tumor")
# result_tree.heading("#1", text="Accuracy")
# result_tree.heading("#2", text="Detection Result")
#
# # Pack Frames
# image_frame.pack(side="top", padx=10, pady=10)
# results_frame.pack(side="top", padx=10, pady=10)
# details_frame.pack(side="top", padx=10, pady=10)
#
# # Pack Labels
# image_label.pack(side="top")
# results_label.pack(side="top")
# details_label.pack(side="top")
#
# # Pack Buttons
# load_button.pack(side="top")
# process_button.pack(side="top")
#
# # Pack Result Details Table
# result_tree.pack(side="top", padx=10, pady=10)
#
# root.mainloop()


# import tkinter as tk
# from tkinter import ttk, filedialog
#
# root = tk.Tk()
# root.title("AI Project")
#
# def load_ct_scan():
#     file_path = filedialog.askopenfilename()
#
# def process_ct_scan():
#     pass
#
# # Create Frames for different sections
# left_frame = tk.Frame(root)
# right_frame = tk.Frame(root)
#
# # Create Frames for image and details sections
# image_frame = tk.Frame(left_frame)
# details_frame = tk.Frame(right_frame)
#
# # Create Labels for image and details sections
# image_label = tk.Label(image_frame, text="Loaded Image")
# details_label = tk.Label(details_frame, text="Processed Details")
#
# # Create Buttons for loading and processing CT scans
# load_button = tk.Button(image_frame, text="Load CT Scan", command=load_ct_scan)
# process_button = tk.Button(details_frame, text="Process CT Scan", command=process_ct_scan)
#
# # Create Square Area for Image (just a placeholder)
# image_area = tk.Canvas(image_frame, width=200, height=200, bg="white")
#
# # Pack Image Area into Image Frame
# image_area.pack(side="top", padx=10, pady=10)
#
# # Pack Labels and Buttons into respective Frames
# image_label.pack(side="top")
# load_button.pack(side="top")
#
# details_label.pack(side="top")
# process_button.pack(side="top")
#
# # Create Square Area for Processed Details (just a placeholder)
# details_area = tk.Canvas(details_frame, width=200, height=200, bg="white")
#
# # Pack Square Area for Processed Details into Details Frame
# details_area.pack(side="top", padx=10, pady=10)
#
# # Create Table for Result Details
# result_tree = ttk.Treeview(details_frame, columns=("Type of Tumor", "Accuracy", "Detection Result"))
# result_tree.heading("#0", text="Type of Tumor")
# result_tree.heading("#1", text="Accuracy")
# result_tree.heading("#2", text="Detection Result")
#
# # Pack Result Details Table into Details Frame
# result_tree.pack(side="top", padx=10, pady=10)
#
# # Pack Frames into left and right Frames
# image_frame.pack(side="left", padx=10, pady=10)
# details_frame.pack(side="left", padx=10, pady=10)
#
# # Pack left and right Frames into root window
# left_frame.pack(side="left", padx=10, pady=10)
# right_frame.pack(side="left", padx=10, pady=10)
#
# root.mainloop()


import tkinter as tk
from tkinter import ttk, filedialog

root = tk.Tk()
root.title("AI Project")

def load_ct_scan():
    file_path = filedialog.askopenfilename()

def process_ct_scan():
    pass

# Create Frames for different sections
left_frame = tk.Frame(root)
right_frame = tk.Frame(root)

# Create sub-frames for image and details sections
image_subframe = tk.Frame(left_frame)
details_subframe = tk.Frame(right_frame)

# Create Labels for image and details sections
image_label = tk.Label(image_subframe, text="Loaded Image")
details_label = tk.Label(details_subframe, text="Processed Details")

# Create Buttons for loading and processing CT scans
load_button = tk.Button(image_subframe, text="Load CT Scan", command=load_ct_scan)
process_button = tk.Button(details_subframe, text="Process CT Scan", command=process_ct_scan)

# Create Square Area for Image (just a placeholder)
image_area = tk.Canvas(image_subframe, width=200, height=200, bg="white")

# Pack Image Area into Image Frame
image_area.pack(side="left", padx=10, pady=10)

# Pack Labels and Buttons into respective sub-frames
image_label.pack(side="left")
load_button.pack(side="left")

details_label.pack(side="left")
process_button.pack(side="left")

# Create Square Area for Processed Details (just a placeholder)
details_area = tk.Canvas(details_subframe, width=200, height=200, bg="white")

# Pack Square Area for Processed Details into Details Frame
details_area.pack(side="left", padx=10, pady=10)

# Create Table for Result Details
result_tree = ttk.Treeview(details_subframe, columns=("Type of Tumor", "Accuracy", "Detection Result"))
result_tree.heading("#0", text="Type of Tumor")
result_tree.heading("#1", text="Accuracy")
result_tree.heading("#2", text="Detection Result")

# Pack Result Details Table into Details Frame
result_tree.pack(side="top", padx=10, pady=10)

# Pack sub-frames into left and right Frames
image_subframe.pack(side="top", padx=10, pady=10)
details_subframe.pack(side="top", padx=10, pady=10)

# Pack left and right Frames into root window
left_frame.pack(side="left", padx=10, pady=10)
right_frame.pack(side="left", padx=10, pady=10)

root.mainloop()
