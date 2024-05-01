import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("AI Project")

def load_ct_scan():
    file_path = filedialog.askopenfilename()



tk.Label(root, text="Detected Results:").grid(row=0)
tk.Label(root, text="Type of Tumor:").grid(row=1)
tk.Label(root, text="Accuracy:").grid(row=2)
tk.Label(root, text="Cancer Detected / Cancer not Detected:").grid(row=3)
tk.Label(root, text="Results Statistics:").grid(row=4)

result_var = tk.StringVar()
type_var = tk.StringVar()
accuracy_var = tk.StringVar()
cancer_var = tk.StringVar()
stats_var = tk.StringVar()

tk.Entry(root, textvariable=result_var).grid(row=0, column=1)
tk.Entry(root, textvariable=type_var).grid(row=1, column=1)
tk.Entry(root, textvariable=accuracy_var).grid(row=2, column=1)
tk.Entry(root, textvariable=cancer_var).grid(row=3, column=1)
tk.Entry(root, textvariable=stats_var).grid(row=4, column=1)
def process_ct_scan():
    pass

tk.Button(root, text="Process CT Scan", command=process_ct_scan).grid(row=5, columnspan=2)
root.mainloop()