import tkinter as tk
from tkinter import filedialog

def save_to_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                text_content = text_widget.get("1.0", "end-1c")
                file.write(text_content)
            status_label.config(text=f"Arquivo salvo: {file_path}")
        except Exception as e:
            status_label.config(text=f"Erro ao salvar o arquivo...: {str(e)}")

root = tk.Tk()
root.title("Text Editor")

text_widget = tk.Text(root, wrap=tk.WORD)
text_widget.pack(padx=20, pady=20, fill="both", expand=True)

save_button = tk.Button(root, text="Salvar", command=save_to_file)
save_button.pack(pady=10)

status_label = tk.Label(root, text="", padx=20, pady=10)
status_label.pack()

root.mainloop()