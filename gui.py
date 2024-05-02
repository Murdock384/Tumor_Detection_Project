import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
root = tk.Tk()
root.title("AI Project")
root.state("zoomed")
def load_ct_scan():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
    if file_path:
        try:
            # Load the image using Pillow
            image = Image.open(file_path)

            # Resize image to fit canvas
            image = image.resize((300, 300))

            # Convert image to a format compatible with Tkinter
            photo = ImageTk.PhotoImage(image)

            # Update the canvas with the loaded image
            image_area.create_image(150, 150, anchor=tk.CENTER, image=photo)
            image_area.image = photo  # Keep a reference to avoid garbage collection
        except (IOError, OSError) as e:
            print(f"Error loading image: {e}")

def process_ct_scan():
    pass


# Header Frame
header_frame = tk.Frame(root)
header_frame.pack(fill=tk.X, pady=10)

header_label = tk.Label(header_frame, text="Brain Tumor Detection - David, Akhil, Tsitsi", font=("Arial", 18, "bold"))
header_label.pack()

# Create Frames for different sections
ct_frame = tk.Frame(root)
details_frame = tk.Frame(root)

# Create Labels for image and details sections
image_label = tk.Label(ct_frame, text="Loaded Image")
processed_image_label = tk.Label(ct_frame, text="Processed Image")
details_label = tk.Label(details_frame, text="Result Details")

# Create Square Area for Image (just a placeholder)
image_area = tk.Canvas(ct_frame, width=400, height=400, bg="white")
processed_image_area = tk.Canvas(ct_frame, width=400, height=400, bg="white")

# Create Buttons for loading and processing CT scans
load_button = tk.Button(ct_frame, text="Load CT Scan", command=load_ct_scan)
process_button = tk.Button(ct_frame, text="Process CT Scan", command=process_ct_scan)

# Pack Labels into first row of CT Frame
image_label.grid(row=0, column=0, padx=(10,0), pady=5)
processed_image_label.grid(row=0, column=1,padx=(0,10), pady=5)

# Pack Canvases into second row of CT Frame
image_area.grid(row=1, column=0, padx=40, pady=40)
processed_image_area.grid(row=1, column=1, padx=40, pady=40)

# Pack Buttons into third row of CT Frame
load_button.grid(row=2, column=0, padx=(10,0), pady=5)
process_button.grid(row=2, column=1, padx=(0,10), pady=5)

# Create Table for Result Details
result_tree = ttk.Treeview(details_frame, columns=("Type of Tumor", "Accuracy", "Detection Result"))
result_tree.heading("#0", text="Type of Tumor")
result_tree.heading("#1", text="Accuracy")
result_tree.heading("#2", text="Detection Result")
result_tree.heading("#3", text="Result Statistics")

# # Pack Result Details Table into Details Frame
# details_label.pack(side="top")
# result_tree.pack(side="top", padx=10, pady=10)

# Pack Result Details Table into Details Frame
result_tree.pack(fill="x", padx=10, pady=10, side="bottom")

# Pack Frames into root window
ct_frame.pack(padx=10, pady=10)
details_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Centering the window
root.eval('tk::PlaceWindow . center')

root.mainloop()

