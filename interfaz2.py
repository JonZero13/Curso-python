import tkinter as tk
from tkinter import ttk

class Curso:
    def __init__(self, nombre, profesor, horario):
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes = []
        self.horario = horario

    def mostrar_info(self):
        info = f"Curso: {self.nombre}\n"
        info += self.profesor.mostrar_info()
        info += self.horario.mostrar_info()
        for estudiante in self.estudiantes:
            info += estudiante.mostrar_info()
        return info

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        estudiante.cursos.append(self)
        return f"Estudiante {estudiante.nombre} {estudiante.apellido} agregado al curso {self.nombre}\n"

class Profesor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.asignaturas = []

    def mostrar_info(self):
        return f"Profesor: {self.nombre} {self.apellido}\n"

class Estudiante:
    def __init__(self, nombre, apellido, id_estudiante):
        self.nombre = nombre
        self.apellido = apellido
        self.id_estudiante = id_estudiante
        self.cursos = []

    def mostrar_info(self):
        return f"Estudiante: {self.nombre} {self.apellido}, ID: {self.id_estudiante}\n"

class Horario:
    def __init__(self, dia, hora_inicio, hora_fin):
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def mostrar_info(self):
        return f"Horario: {self.dia}, {self.hora_inicio} - {self.hora_fin}\n"

class GestionCursos:
    def __init__(self, root):
        self.cursos = []
        self.profesores = []
        self.estudiantes = []

        
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True)

        
        self.curso_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.curso_tab, text="Cursos")

        self.curso_frame = tk.LabelFrame(self.curso_tab, text="Agregar Curso", padx=10, pady=10)
        self.curso_frame.pack(fill="x", padx=10, pady=10)

        self.curso_nombre_entry = self.crear_entrada(self.curso_frame, "Nombre del Curso:", 0, 0)
        self.profesor_nombre_entry = self.crear_entrada(self.curso_frame, "Nombre del Profesor:", 1, 0)
        self.profesor_apellido_entry = self.crear_entrada(self.curso_frame, "Apellido del Profesor:", 2, 0)
        self.horario_dia_entry = self.crear_entrada(self.curso_frame, "Día del Horario:", 3, 0)
        self.horario_inicio_entry = self.crear_entrada(self.curso_frame, "Hora de Inicio:", 4, 0)
        self.horario_fin_entry = self.crear_entrada(self.curso_frame, "Hora de Fin:", 5, 0)

        self.agregar_curso_button = tk.Button(self.curso_frame, text="Agregar Curso", command=self.agregar_curso)
        self.agregar_curso_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        
        self.estudiante_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.estudiante_tab, text="Estudiantes")

        self.estudiante_frame = tk.LabelFrame(self.estudiante_tab, text="Agregar Estudiante", padx=10, pady=10)
        self.estudiante_frame.pack(fill="x", padx=10, pady=10)

        self.estudiante_nombre_entry = self.crear_entrada(self.estudiante_frame, "Nombre del Estudiante:", 0, 0)
        self.estudiante_apellido_entry = self.crear_entrada(self.estudiante_frame, "Apellido del Estudiante:", 1, 0)
        self.estudiante_id_entry = self.crear_entrada(self.estudiante_frame, "ID del Estudiante:", 2, 0)

        self.agregar_estudiante_button = tk.Button(self.estudiante_frame, text="Agregar Estudiante", command=self.agregar_estudiante)
        self.agregar_estudiante_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

   
        self.info_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.info_tab, text="Información")

        self.info_text = tk.Text(self.info_tab, height=20, width=50)
        self.info_text.pack(fill="both", expand=True, padx=10, pady=10)

    
        self.mostrar_info_button = tk.Button(self.info_tab, text="Mostrar Información", command=self.mostrar_informacion)
        self.mostrar_info_button.pack(pady=5)

    def crear_entrada(self, parent, texto, fila, columna):
        label = tk.Label(parent, text=texto)
        label.grid(row=fila, column=columna, sticky="w", padx=5, pady=5)
        entry = tk.Entry(parent)
        entry.grid(row=fila, column=columna+1, sticky="w", padx=5, pady=5)
        return entry

    def agregar_curso(self):
        nombre_curso = self.curso_nombre_entry.get()
        nombre_profesor = self.profesor_nombre_entry.get()
        apellido_profesor = self.profesor_apellido_entry.get()
        dia_horario = self.horario_dia_entry.get()
        hora_inicio = self.horario_inicio_entry.get()
        hora_fin = self.horario_fin_entry.get()

        profesor = Profesor(nombre_profesor, apellido_profesor)
        self.profesores.append(profesor)

        horario = Horario(dia_horario, hora_inicio, hora_fin)
        
        curso = Curso(nombre_curso, profesor, horario)
        self.cursos.append(curso)

        for entry in [self.curso_nombre_entry, self.profesor_nombre_entry, self.profesor_apellido_entry, self.horario_dia_entry, self.horario_inicio_entry, self.horario_fin_entry]:
            entry.delete(0, tk.END)

        self.info_text.insert(tk.END, f"Curso {nombre_curso} agregado.\n")

    def agregar_estudiante(self):
        nombre_estudiante = self.estudiante_nombre_entry.get()
        apellido_estudiante = self.estudiante_apellido_entry.get()
        id_estudiante = self.estudiante_id_entry.get()

        estudiante = Estudiante(nombre_estudiante, apellido_estudiante, id_estudiante)
        self.estudiantes.append(estudiante)

        for entry in [self.estudiante_nombre_entry, self.estudiante_apellido_entry, self.estudiante_id_entry]:
            entry.delete(0, tk.END)

        self.info_text.insert(tk.END, f"Estudiante {nombre_estudiante} {apellido_estudiante} agregado.\n")

    def mostrar_informacion(self):
        self.info_text.delete('1.0', tk.END)
        for curso in self.cursos:
            self.info_text.insert(tk.END, curso.mostrar_info() + "\n")
        for estudiante in self.estudiantes:
            self.info_text.insert(tk.END, estudiante.mostrar_info() + "\n")
        for profesor in self.profesores:
            self.info_text.insert(tk.END, profesor.mostrar_info() + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gestión de Cursos")
    root.geometry("800x600")
    gestion_cursos = GestionCursos(root)
    root.mainloop()
