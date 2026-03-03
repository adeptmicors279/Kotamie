import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox


class ProjectCreator:

    def __init__(self, root):
        self.root = root
        self.root.title("Kotamie Project Creator")
        self.root.geometry("480x320")
        self.root.resizable(False, False)

        self.setup_style()
        self.build_ui()

    def setup_style(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("TLabel", font=("Segoe UI", 11))
        style.configure("TButton", font=("Segoe UI", 11), padding=6)
        style.configure("TEntry", padding=5)
        style.configure("TCombobox", padding=5)

    def build_ui(self):

        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill="both", expand=True)

        title = ttk.Label(
            main_frame,
            text="Create New Project",
            font=("Segoe UI", 18, "bold")
        )
        title.grid(row=0, column=0, columnspan=3, pady=(0, 20))

        # 项目名称
        ttk.Label(main_frame, text="Project Name:").grid(row=1, column=0, sticky="w")
        self.name_var = tk.StringVar()
        name_entry = ttk.Entry(main_frame, textvariable=self.name_var, width=30)
        name_entry.grid(row=1, column=1, columnspan=2, pady=5, sticky="ew")

        # 保存路径
        ttk.Label(main_frame, text="Location:").grid(row=2, column=0, sticky="w")
        self.path_var = tk.StringVar(value=os.getcwd())
        path_entry = ttk.Entry(main_frame, textvariable=self.path_var, width=30)
        path_entry.grid(row=2, column=1, pady=5, sticky="ew")

        browse_btn = ttk.Button(
            main_frame,
            text="Browse",
            command=self.browse_path
        )
        browse_btn.grid(row=2, column=2, padx=5)

        # 项目类型
        ttk.Label(main_frame, text="Project Type:").grid(row=3, column=0, sticky="w")
        self.type_var = tk.StringVar()
        type_box = ttk.Combobox(
            main_frame,
            textvariable=self.type_var,
            values=["Visual Novel"],
            state="readonly"
        )
        type_box.current(0)
        type_box.grid(row=3, column=1, columnspan=2, pady=5, sticky="ew")

        # 创建按钮
        create_btn = ttk.Button(
            main_frame,
            text="Create Project",
            command=self.create_project
        )
        create_btn.grid(row=4, column=0, columnspan=3, pady=25)

        # 状态
        self.status_label = ttk.Label(main_frame, text="")
        self.status_label.grid(row=5, column=0, columnspan=3)

        main_frame.columnconfigure(1, weight=1)

    def browse_path(self):
        path = filedialog.askdirectory()
        if path:
            self.path_var.set(path)

    def create_project(self):
        name = self.name_var.get().strip()
        base_path = self.path_var.get().strip()
        #project_type = self.type_var.get() 待定

        if not name:
            messagebox.showerror("Error", "Project name cannot be empty.")
            return

        final_path = os.path.join(base_path, name)

        if os.path.exists(final_path):
            messagebox.showerror("Error", "Folder already exists.")
            return

        try:
            import shutil
            # 复制整个模板目录
            shutil.copytree("template", final_path)
            messagebox.showinfo("Success", f"Project created at:\n{final_path}")
            self.status_label.config(text="Project created successfully!")

        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = ProjectCreator(root)
    root.mainloop()
