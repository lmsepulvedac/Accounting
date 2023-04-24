import tkinter as tk
import matplotlib.pyplot as plt
import webbrowser


# Función para calcular las utilidades
def calcular_utilidad_bruta(ingresos, costos):
    utilidades = ingresos - costos
    return utilidades


def calcular_utilidad_operacional(gastos, utilidad_bruta):
    utilidades = utilidad_bruta - gastos
    return utilidades


# Función para actualizar el gráfico
def actualizar_grafico(ingresos, costos, gastos, impuestos):
    plt.clf()
    etiquetas = ['Ingresos', 'Costos', 'Gastos', 'Impuestos']
    valores = [ingresos, costos, gastos, impuestos]
    colores = ['green', 'red', 'blue', 'yellow']
    if ingresos != 0:
        plt.pie(valores, labels=etiquetas, colors=colores, autopct='%1.1f%%')
    plt.title('Estado de resultados')
    plt.show()


def calcular_gastos():
    arrendamientos = entrada_arrendamientos.get()
    servicios = entrada_servicios.get()
    nomina = entrada_nomina.get()
    otros = entrada_otros.get()
    vector_gastos = [arrendamientos, servicios, nomina, otros]
    try:
        vector_gastos = list(map(float, vector_gastos))
    except ValueError:
        vector_gastos = [0.0 for gasto in vector_gastos if gasto == ""]
    gastos = sum(vector_gastos)
    return gastos


def capturar_datos():
    # Obtener los valores de las entradas de texto
    ingresos = entrada_ingresos.get()
    costos = entrada_costos.get()
    gastos = calcular_gastos()
    try:
        ingresos = float(ingresos)
        costos = float(costos)
    except ValueError:
        if ingresos == "" and costos == "":
            entrada_ingresos.insert(0, 0)
            ingresos = 0
            entrada_costos.insert(0,

                                  0)
            costos = 0
        elif ingresos == "" and costos != "":
            entrada_ingresos.insert(0 ,0)
            ingresos = 0
            costos = float(costos)
        elif ingresos != "" and costos == "":
            ingresos = float(ingresos)
            entrada_costos.insert(0, 0)
            costos = 0
    return ingresos, costos, gastos


def operaciones(ingresos, costos, gastos):
    # Calcular las utilidades
    utilidad_bruta = calcular_utilidad_bruta(ingresos, costos)
    utilidad_operacional = calcular_utilidad_operacional(gastos, utilidad_bruta)
    texto_utilidades.set(f'$ {utilidad_operacional:.2f}')
    if utilidad_operacional < 0:
        impuestos = 0
    else:
        impuestos = 0.35*utilidad_operacional
    return impuestos, utilidad_bruta, utilidad_operacional


# Función para actualizar las utilidades
def actualizar_utilidades():
    # Calcular cantidades
    ingresos, costos, gastos = capturar_datos()
    impuestos, utilidad_bruta, utilidad_operacional = operaciones(ingresos, costos, gastos)
    # Actualizar el texto de las utilidades
    texto_utilidad_bruta.set(f'$ {utilidad_bruta:.2f}')
    texto_impuestos.set(f'$ {impuestos:.2f}')
    utilidad_periodo = utilidad_operacional - impuestos
    texto_utilidad_periodo.set(f'$ {utilidad_periodo:.2f}')
    # Actualizar el gráfico
    actualizar_grafico(ingresos, costos, gastos, impuestos)

def punto_equilibrio():
    # Obtener los valores de las entradas de texto
    valor_unitario = 6120
    ingresos, costos, gastos = capturar_datos()
    ingresos = 0.0
    impuestos, utilidad_bruta, utilidad_operacional = operaciones(ingresos, costos, gastos)
    unidades = (gastos + costos + impuestos)/valor_unitario
    texto_punto_equilibrio.set(f'{unidades} unidades')
    entrada_ingresos.delete(0, tk.END)
    entrada_ingresos.insert(0, unidades*valor_unitario)
    actualizar_utilidades()


def open_website(event):
    webbrowser.open("https://www.eafit.edu.co")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Los Sabrositos S.A.S')

# Cargar la imagen del logo de EAFIT
photo = tk.PhotoImage(file = 'eafit_logo.png')

# Agregar el logo a la ventana principal
logo_label = tk.Label(ventana, image=photo)
logo_label.pack()
logo_label.grid(row=20, column=4, columnspan=2)
logo_label.bind("<Button-1>", open_website)


#Definición de Columnas
columna_estado_resultados = 6
columna_presupuesto = 0
fila_presupuesto = 0

#Crear el presupuesto inicial
tk.Label(ventana, text='Propiedad, planta y equipo:', anchor='ne', font='Helvetica 12 bold').grid(row=0,
                                                                                                  column=columna_presupuesto,
                                                                                                  sticky='w')

tk.Label(ventana, text='Local propio:', anchor='ne').grid(row=fila_presupuesto+1, column=columna_presupuesto, sticky='w')
local_propio = tk.Entry(ventana)
local_propio.insert(0, 24000000)
local_propio.grid(row=fila_presupuesto+1, column=columna_presupuesto+1, sticky='w')

tk.Label(ventana, text='Local arrendado:', anchor='ne').grid(row=fila_presupuesto+2, column=columna_presupuesto, sticky='w')
local_arrendado = tk.Entry(ventana)
local_arrendado.grid(row=fila_presupuesto+2, column=columna_presupuesto+1, sticky='w')
local_arrendado.insert(0, 0)

tk.Label(ventana, text='Maquinaria:', anchor='ne').grid(row=fila_presupuesto+3, column=columna_presupuesto, sticky='w')
maquinaria = tk.Entry(ventana)
maquinaria.grid(row=fila_presupuesto+3, column=columna_presupuesto+1, sticky='w')
maquinaria.insert(0, 4740000)

tk.Label(ventana, text='Equipo de cómputo:', anchor='ne').grid(row=fila_presupuesto+4, column=columna_presupuesto, sticky='w')
muebles = tk.Entry(ventana)
muebles.grid(row=fila_presupuesto+4, column=columna_presupuesto+1, sticky='w')
muebles.insert(0, 5500000)

tk.Label(ventana, text='Equipos de oficina:', anchor='ne').grid(row=fila_presupuesto+5, column=columna_presupuesto, sticky='w')
equipos_oficina = tk.Entry(ventana)
equipos_oficina.grid(row=fila_presupuesto+5, column=columna_presupuesto+1, sticky='w')
equipos_oficina.insert(0, 5500000)

tk.Label(ventana, text='-------------------------------------------'
                       '--------------------------------------------'
                       '-----------------------------'
         , anchor='ne').grid(row=fila_presupuesto+6, column=columna_presupuesto, sticky='w', columnspan=5)
tk.Label(ventana, text='Insumos:', anchor='ne', font='Helvetica 12 bold').grid(row=fila_presupuesto+7,
                                                                               column=columna_presupuesto, sticky='w')

tk.Label(ventana, text='Rubro', anchor='ne').grid(row=fila_presupuesto+8, column=columna_presupuesto, sticky='w')
tk.Label(ventana, text='Cantidad', anchor='ne').grid(row=fila_presupuesto+8, column=columna_presupuesto+1, sticky='w')
tk.Label(ventana, text='Costo unitario [$]/Postre', anchor='ne').grid(row=fila_presupuesto+8, column=columna_presupuesto+4, sticky='w')

tk.Label(ventana, text='Crema de leche:', anchor='ne').grid(row=fila_presupuesto+9, column=columna_presupuesto, sticky='w')
crema_leche_cantidad = tk.Entry(ventana)
crema_leche_cantidad.grid(row=fila_presupuesto+9, column=columna_presupuesto+1, sticky='w')
crema_leche_cantidad.insert(0, 50)
tk.Label(ventana, text='gr', anchor='ne').grid(row=fila_presupuesto+9, column=columna_presupuesto+2, sticky='w')
crema_leche_valor = tk.Entry(ventana)
tk.Label(ventana, text=' ', anchor='ne').grid(row=fila_presupuesto+9, column=columna_presupuesto+3, sticky='w')
crema_leche_valor.grid(row=fila_presupuesto+9, column=columna_presupuesto+4, sticky='w')
crema_leche_valor.insert(0, 500)

tk.Label(ventana, text='Leche condensada:', anchor='ne').grid(row=fila_presupuesto+10, column=columna_presupuesto, sticky='w')
leche_condensada_cantidad = tk.Entry(ventana)
leche_condensada_cantidad.grid(row=fila_presupuesto+10, column=columna_presupuesto+1, sticky='w')
leche_condensada_cantidad.insert(0, 40)
tk.Label(ventana, text='gr', anchor='ne').grid(row=fila_presupuesto+10, column=columna_presupuesto+2, sticky='w')
leche_condensada_valor = tk.Entry(ventana)
tk.Label(ventana, text=' ', anchor='ne').grid(row=fila_presupuesto+10, column=columna_presupuesto+3, sticky='w')
leche_condensada_valor.grid(row=fila_presupuesto+10, column=columna_presupuesto+4, sticky='w')
leche_condensada_valor.insert(0, 600)

tk.Label(ventana, text='Leche:', anchor='ne').grid(row=fila_presupuesto+11, column=columna_presupuesto, sticky='w')
leche_cantidad = tk.Entry(ventana)
leche_cantidad.grid(row=fila_presupuesto+11, column=columna_presupuesto+1, sticky='w')
leche_cantidad.insert(0, 250)
tk.Label(ventana, text='ml', anchor='ne').grid(row=fila_presupuesto+11, column=columna_presupuesto+2, sticky='w')
leche_valor = tk.Entry(ventana)
tk.Label(ventana, text=' ', anchor='ne').grid(row=fila_presupuesto+11, column=columna_presupuesto+3, sticky='w')
leche_valor.grid(row=fila_presupuesto+11, column=columna_presupuesto+4, sticky='w')
leche_valor.insert(0, 750)

tk.Label(ventana, text='Gelatina sin sabor:', anchor='ne').grid(row=fila_presupuesto+12, column=columna_presupuesto, sticky='w')
gelatina_cantidad = tk.Entry(ventana)
gelatina_cantidad.grid(row=fila_presupuesto+12, column=columna_presupuesto+1, sticky='w')
gelatina_cantidad.insert(0, 7.5)
tk.Label(ventana, text='gr', anchor='ne').grid(row=fila_presupuesto+12, column=columna_presupuesto+2, sticky='w')
gelatina_valor = tk.Entry(ventana)
tk.Label(ventana, text=' ', anchor='ne').grid(row=fila_presupuesto+12, column=columna_presupuesto+3, sticky='w')
gelatina_valor.grid(row=fila_presupuesto+12, column=columna_presupuesto+4, sticky='w')
gelatina_valor.insert(0, 200)

tk.Label(ventana, text='Esencia de vainilla:', anchor='ne').grid(row=fila_presupuesto+13, column=columna_presupuesto, sticky='w')
esencia_cantidad = tk.Entry(ventana)
esencia_cantidad.grid(row=fila_presupuesto+13, column=columna_presupuesto+1, sticky='w')
esencia_cantidad.insert(0, 10)
tk.Label(ventana, text='ml', anchor='ne').grid(row=fila_presupuesto+13, column=columna_presupuesto+2, sticky='w')
esencia_valor = tk.Entry(ventana)
tk.Label(ventana, text=' ', anchor='ne').grid(row=fila_presupuesto+13, column=columna_presupuesto+3, sticky='w')
esencia_valor.grid(row=fila_presupuesto+13, column=columna_presupuesto+4, sticky='w')
esencia_valor.insert(0, 200)

tk.Label(ventana, text='Galletas (Oreo):', anchor='ne').grid(row=fila_presupuesto+14, column=columna_presupuesto, sticky='w')
galletas_cantidad = tk.Entry(ventana)
galletas_cantidad.grid(row=fila_presupuesto+14, column=columna_presupuesto+1, sticky='w')
galletas_cantidad.insert(0, 2)
tk.Label(ventana, text='pq', anchor='ne').grid(row=fila_presupuesto+14, column=columna_presupuesto+2, sticky='w')
galletas_valor = tk.Entry(ventana)
tk.Label(ventana, text=' ', anchor='ne').grid(row=fila_presupuesto+14, column=columna_presupuesto+3, sticky='w')
galletas_valor.grid(row=fila_presupuesto+14, column=columna_presupuesto+4, sticky='w')
galletas_valor.insert(0, 1400)

tk.Label(ventana, text='Empaques:', anchor='ne').grid(row=fila_presupuesto+15, column=columna_presupuesto, sticky='w')
empaques_cantidad = tk.Entry(ventana)
empaques_cantidad.grid(row=fila_presupuesto+15, column=columna_presupuesto+1, sticky='w')
empaques_cantidad.insert(0, 1)
tk.Label(ventana, text='pq', anchor='ne').grid(row=fila_presupuesto+15, column=columna_presupuesto+2, sticky='w')
empaques_valor = tk.Entry(ventana)
tk.Label(ventana, text=' ', anchor='ne').grid(row=fila_presupuesto+15, column=columna_presupuesto+3, sticky='w')
empaques_valor.grid(row=fila_presupuesto+15, column=columna_presupuesto+4, sticky='w')
empaques_valor.insert(0, 400)

tk.Label(ventana, text='Cucharas:', anchor='ne').grid(row=fila_presupuesto+16, column=columna_presupuesto, sticky='w')
cucharas_cantidad = tk.Entry(ventana)
cucharas_cantidad.grid(row=fila_presupuesto+16, column=columna_presupuesto+1, sticky='w')
cucharas_cantidad.insert(0, 1)
tk.Label(ventana, text='pq', anchor='ne').grid(row=fila_presupuesto+16, column=columna_presupuesto+2, sticky='w')
cucharas_valor = tk.Entry(ventana)
tk.Label(ventana, text=' ', anchor='ne').grid(row=fila_presupuesto+16, column=columna_presupuesto+3, sticky='w')
cucharas_valor.grid(row=fila_presupuesto+16, column=columna_presupuesto+4, sticky='w')
cucharas_valor.insert(0, 20)

tk.Label(ventana, text='Mantequilla:', anchor='ne').grid(row=fila_presupuesto+17, column=columna_presupuesto, sticky='w')
mantequilla_cantidad = tk.Entry(ventana)
mantequilla_cantidad.grid(row=fila_presupuesto+17, column=columna_presupuesto+1, sticky='w')
mantequilla_cantidad.insert(0, 30)
tk.Label(ventana, text='gr', anchor='ne').grid(row=fila_presupuesto+17, column=columna_presupuesto+2, sticky='w')
mantequilla_valor = tk.Entry(ventana)
tk.Label(ventana, text=' ', anchor='ne').grid(row=fila_presupuesto+17, column=columna_presupuesto+3, sticky='w')
mantequilla_valor.grid(row=fila_presupuesto+17, column=columna_presupuesto+4, sticky='w')
mantequilla_valor.insert(0, 500)

tk.Label(ventana, text='Queso crema:', anchor='ne').grid(row=fila_presupuesto+18, column=columna_presupuesto, sticky='w')
queso_cantidad = tk.Entry(ventana)
queso_cantidad.grid(row=fila_presupuesto+18, column=columna_presupuesto+1, sticky='w')
queso_cantidad.insert(0, 45)
tk.Label(ventana, text='gr', anchor='ne').grid(row=fila_presupuesto+18, column=columna_presupuesto+2, sticky='w')
queso_valor = tk.Entry(ventana)
tk.Label(ventana, text=' ', anchor='ne').grid(row=fila_presupuesto+18, column=columna_presupuesto+3, sticky='w')
queso_valor.grid(row=fila_presupuesto+18, column=columna_presupuesto+4, sticky='w')
queso_valor.insert(0, 900)

#Crear el estado de resultados
tk.Label(ventana, text='Estado de resultados:', anchor='n', font='Helvetica 12 bold').grid(row=0,
                                                                                           column=columna_estado_resultados,
                                                                                           sticky='w')
tk.Label(ventana, text='Ingresos:', anchor='ne').grid(row=1, column=columna_estado_resultados, sticky='w')
entrada_ingresos = tk.Entry(ventana)
entrada_ingresos.grid(row=1, column=columna_estado_resultados+1, sticky='w')

tk.Label(ventana, text='Costos:').grid(row=2, column=columna_estado_resultados, sticky='w')
entrada_costos = tk.Entry(ventana)
entrada_costos.grid(row=2, column=columna_estado_resultados+1, sticky='w')

tk.Label(ventana, text='Utilidad Bruta:').grid(row=3, column=columna_estado_resultados, sticky='w')
texto_utilidad_bruta = tk.StringVar()
texto_utilidad_bruta.set('$ 0.00')
tk.Label(ventana, textvariable=texto_utilidad_bruta).grid(row=3, column = columna_estado_resultados+1, sticky='w')

tk.Label(ventana, text='Arrendamientos:').grid(row=4, column=columna_estado_resultados, sticky='w')
entrada_arrendamientos = tk.Entry(ventana)
entrada_arrendamientos.grid(row=4, column=columna_estado_resultados+1, sticky='w')

tk.Label(ventana, text='Gastos de servicios públicos:').grid(row=5, column=columna_estado_resultados, sticky='w')
entrada_servicios = tk.Entry(ventana)
entrada_servicios.grid(row=5, column=columna_estado_resultados+1, sticky='w')

tk.Label(ventana, text='Gastos de nómina:').grid(row=6, column=columna_estado_resultados, sticky='w')
entrada_nomina = tk.Entry(ventana)
entrada_nomina.grid(row=6, column=columna_estado_resultados+1, sticky='w')

tk.Label(ventana, text='Otros gastos:').grid(row=7, column=columna_estado_resultados, sticky='w')
entrada_otros = tk.Entry(ventana)
entrada_otros.grid(row=7, column=columna_estado_resultados+1, sticky='w')

tk.Label(ventana, text='Utilidad Operacional:').grid(row=8, column=columna_estado_resultados, sticky='w')
texto_utilidades = tk.StringVar()
texto_utilidades.set('$ 0.00')
tk.Label(ventana, textvariable=texto_utilidades).grid(row=8, column=columna_estado_resultados+1, sticky='w')

tk.Label(ventana, text='Impuestos:').grid(row=9, column=columna_estado_resultados, sticky='w')
texto_impuestos = tk.StringVar()
texto_impuestos.set('$ 0.00')
tk.Label(ventana, textvariable=texto_impuestos).grid(row=9, column=columna_estado_resultados+1, sticky='w')

tk.Label(ventana, text='Utilidad o pérdida del periodo:').grid(row=10, column=columna_estado_resultados, sticky='w')
texto_utilidad_periodo = tk.StringVar()
texto_utilidad_periodo.set('$ 0.00')
tk.Label(ventana, textvariable=texto_utilidad_periodo).grid(row=10, column=columna_estado_resultados+1, sticky='w')

tk.Label(ventana, text='Punto de equilibrio:').grid(row=11, column=columna_estado_resultados, sticky='w')
texto_punto_equilibrio = tk.StringVar()
texto_punto_equilibrio.set('--- unidades')
tk.Label(ventana, textvariable=texto_punto_equilibrio).grid(row=11, column=columna_estado_resultados+1, sticky='w')

# Crear el botón de actualizar
boton_actualizar = tk.Button(ventana, text='Actualizar', command=actualizar_utilidades)
boton_actualizar.grid(row=12, column=columna_estado_resultados,)

boton_equilibrio = tk.Button(ventana, text='Punto de equilibrio', command=punto_equilibrio)
boton_equilibrio.grid(row=12, column=columna_estado_resultados+1)

# Mostrar el gráfico inicial
actualizar_grafico(0, 0, 0, 0)

# Ejecutar la aplicación
ventana.mainloop()
