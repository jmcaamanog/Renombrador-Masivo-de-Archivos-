"""
      ██╗███╗   ███╗ ██████╗
      ██║████╗ ████║██╔════╝
      ██║██╔████╔██║██║
 ██   ██║██║╚██╔╝██║██║    
 ╚█████╔╝██║ ╚═╝ ██║╚██████╗
  ╚════╝ ╚═╝     ╚═╝ ╚═════╝
"""
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os

class BulkRenamerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Renombrador Masivo V.01 by JMCG")
        self.root.geometry("900x600")
        self.root.minsize(700, 450)

        # --- Estilos y Colores ---
        light_bg_color = '#F0F0F0'
        self.root.configure(bg=light_bg_color)
        self.style = ttk.Style(self.root)
        self.style.theme_use("clam")

        self.style.configure("TFrame", background=light_bg_color)
        self.style.configure("TLabel", background=light_bg_color, font=('Helvetica', 10))
        self.style.configure("Header.TLabel", background=light_bg_color, font=('Helvetica', 14, 'bold'))
        self.style.configure("TNotebook", background=light_bg_color)
        self.style.configure("TNotebook.Tab", background=light_bg_color, padding=[10, 5], font=('Helvetica', 10))
        self.style.map("TNotebook.Tab", background=[("selected", light_bg_color)])
        self.style.configure("TButton", padding=6, font=('Helvetica', 10, 'bold'))
        self.style.configure("Treeview", rowheight=25)
        self.style.configure("Treeview.Heading", font=('Helvetica', 10, 'bold'))

        # --- Variables ---
        self.base_name = tk.StringVar(value="Nuevo_Nombre")
        self.start_number = tk.IntVar(value=1)
        self.separator = tk.StringVar(value="_")
        self.file_list = []

        # --- Pestañas ---
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)
        self.create_renamer_tab()
        self.create_about_tab()

    def create_renamer_tab(self):
        renamer_frame = ttk.Frame(self.notebook, padding="10", style="TFrame")
        self.notebook.add(renamer_frame, text='Renombrar Archivos')

        # --- Frame Superior (Controles de renombrado) ---
        controls_frame = ttk.Frame(renamer_frame, style="TFrame")
        controls_frame.pack(fill='x', pady=5, padx=5)
        
        # Columna 1: Texto Base
        ttk.Label(controls_frame, text="Texto Base:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        ttk.Entry(controls_frame, textvariable=self.base_name, width=30).grid(row=0, column=1, padx=5, pady=5, sticky='we')

        # Columna 2: Número Inicial
        ttk.Label(controls_frame, text="Número Inicial:").grid(row=0, column=2, padx=5, pady=5, sticky='w')
        ttk.Entry(controls_frame, textvariable=self.start_number, width=10).grid(row=0, column=3, padx=5, pady=5, sticky='w')

        # Columna 3: Separador
        ttk.Label(controls_frame, text="Separador:").grid(row=0, column=4, padx=5, pady=5, sticky='w')
        ttk.Combobox(controls_frame, textvariable=self.separator, values=['_', '-', ' ', '.'], width=5, state="readonly").grid(row=0, column=5, padx=5, pady=5, sticky='w')

        controls_frame.columnconfigure(1, weight=1)

        # --- Frame de Resultados (TreeView) ---
        results_frame = ttk.Frame(renamer_frame, style="TFrame")
        results_frame.pack(expand=True, fill='both', pady=10, padx=5)
        
        self.tree = ttk.Treeview(results_frame, columns=("Original", "New"), show="headings")
        self.tree.heading("Original", text="Nombre Original")
        self.tree.heading("New", text="Nuevo Nombre (Previsualización)")
        self.tree.pack(side='left', expand=True, fill='both')

        scrollbar = ttk.Scrollbar(results_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # --- Frame Inferior (Botones de acción) ---
        bottom_frame = ttk.Frame(renamer_frame, style="TFrame")
        bottom_frame.pack(fill='x', pady=5, padx=5)

        ttk.Button(bottom_frame, text="Añadir Archivos...", command=self.add_files).pack(side='left')
        
        self.apply_button = ttk.Button(bottom_frame, text="Aplicar Renombrado", command=self.apply_rename, state="disabled")
        self.apply_button.pack(side='right')
        
        self.preview_button = ttk.Button(bottom_frame, text="Previsualizar Cambios", command=self.preview_rename, state="disabled")
        self.preview_button.pack(side='right', padx=5)


    def create_about_tab(self):
        about_frame = ttk.Frame(self.notebook, padding="30", style="TFrame")
        self.notebook.add(about_frame, text='Acerca de')
        content_frame = ttk.Frame(about_frame, style="TFrame")
        content_frame.pack(expand=True)

        ttk.Label(content_frame, text="Renombrador Masivo v1.0 by JMCG", style="Header.TLabel").pack(pady=(0, 10))
        description_text = ("Esta herramienta permite renombrar múltiples archivos de forma rápida y segura.\n"
                            "Define un patrón con texto base, un número secuencial y un separador, y previsualiza los cambios antes de aplicarlos.")
        ttk.Label(content_frame, text=description_text, wraplength=500, justify='center', style="TLabel").pack(pady=10)
        ttk.Separator(content_frame, orient='horizontal').pack(fill='x', pady=20)
        
        info_texts = ["Versión: 1.0 by JMCG", "Más información: josecaamano.io", 
                      "Desarrollado por: Jose Manuel Caamaño González", "Copyright 2025 By Jose Manuel Caamaño",
                      "\n¡Gracias por usar este programa!"]
        for text in info_texts:
            ttk.Label(content_frame, text=text, style="TLabel").pack(pady=2)

    def add_files(self):
        """Abre un diálogo para seleccionar archivos y los añade a la lista."""
        filepaths = filedialog.askopenfilenames(
            title="Seleccionar archivos para renombrar",
            filetypes=(("Todos los archivos", "*.*"),)
        )
        if not filepaths:
            return

        self.file_list.extend(filepaths)
        self.update_treeview()
        self.preview_button.config(state="normal")

    def update_treeview(self):
        """Limpia y rellena la tabla con la lista de archivos actual."""
        self.tree.delete(*self.tree.get_children())
        for f in self.file_list:
            original_name = os.path.basename(f)
            self.tree.insert("", "end", values=(original_name, ""))

    def preview_rename(self):
        """Genera y muestra los nuevos nombres en la columna de previsualización."""
        try:
            start_num = self.start_number.get()
        except tk.TclError:
            messagebox.showerror("Error de Entrada", "El número inicial debe ser un entero.")
            return

        base_name_val = self.base_name.get()
        separator_val = self.separator.get()
        
        children = self.tree.get_children()
        for i, item_id in enumerate(children):
            original_path = self.file_list[i]
            file_extension = os.path.splitext(original_path)[1]
            # Formatear el número con ceros a la izquierda para un orden correcto (ej. 01, 02, ... 10)
            padding = len(str(len(children) + start_num -1))
            new_name = f"{base_name_val}{separator_val}{str(i + start_num).zfill(padding)}{file_extension}"
            
            # Actualiza el valor en la segunda columna del Treeview
            self.tree.set(item_id, column="New", value=new_name)
        
        self.apply_button.config(state="normal")

    def apply_rename(self):
        """Aplica el renombrado a los archivos."""
        if not messagebox.askyesno("Confirmar Renombrado",
                                   "¿Estás seguro de que quieres renombrar estos archivos de forma permanente?"):
            return

        renamed_count = 0
        errors = []
        
        children = self.tree.get_children()
        for i, item_id in enumerate(children):
            original_full_path = self.file_list[i]
            new_name = self.tree.item(item_id, "values")[1]

            if not new_name:
                errors.append(f"{os.path.basename(original_full_path)}: No se generó un nuevo nombre.")
                continue

            directory = os.path.dirname(original_full_path)
            new_full_path = os.path.join(directory, new_name)

            try:
                os.rename(original_full_path, new_full_path)
                renamed_count += 1
            except FileExistsError:
                errors.append(f"{new_name}: Ya existe un archivo con este nombre.")
            except OSError as e:
                errors.append(f"{os.path.basename(original_full_path)}: {e}")

        # Mensaje final
        if not errors:
            messagebox.showinfo("Éxito", f"Se han renombrado {renamed_count} archivos correctamente.")
        else:
            error_message = f"Proceso completado con {len(errors)} errores.\n\n" + "\n".join(errors)
            messagebox.showwarning("Proceso Completado con Errores", error_message)
        
        # Limpiar la lista después de renombrar
        self.file_list.clear()
        self.update_treeview()
        self.preview_button.config(state="disabled")
        self.apply_button.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = BulkRenamerApp(root)
    root.mainloop()
