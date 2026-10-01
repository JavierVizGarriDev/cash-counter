from tkinter import *


def main():

    def ventana_principal():
        aplicacion = Tk()  # Crear objeto ventana
        aplicacion.resizable(False, False)  # No redimensionable
        aplicacion.title('Denominaciones')  # Titulo
        aplicacion.config(bg="alice blue")  # Background

        return aplicacion

    def tabla_denominaciones():

        # Reemplazar elementos de una lista por su indice
        def replace(indice=0, lista=[], sustituto=0):
            lista.pop(indice)
            lista.insert(indice, sustituto)

        # Crear Label
        def etiquetas(ancho, columna, texto, columnspan=1):
            etiqueta = Label(aplicacion,
                             font=('Verdana', 15, 'bold'),
                             text=texto,
                             width=ancho)
            etiqueta.grid(row=cont, column=columna, columnspan=columnspan)
            return etiqueta

        # Crear Entry
        def entradas(ancho, columna, estado=NORMAL, columnspan=1):
            visor = Entry(aplicacion,
                          bg='lightgreen',
                          font=('Verdana', 15, 'bold'),
                          state=estado,
                          width=ancho)
            visor.grid(row=cont, column=columna, columnspan=columnspan)
            return visor

        # Crear boton:
        def boton(ancho, texto, fila=0, columna=0, columnspan=1):
            boton_resultado = Button(aplicacion,
                                     text=texto,
                                     font=('Verdana', 15, 'bold'),
                                     width=ancho)
            boton_resultado.grid(row=fila, column=columna, columnspan=columnspan)
            return boton_resultado

        # Usando la funcion replace, reemplaza los valores de la tabla de valores por los que esten en el Entry corresp
        def replace_table(denominaciones):
            cont = 0
            for denominacion in range(len(denominaciones) - 1):
                replace(indice=cont, lista=valor_den, sustituto=entradas_datos[cont].get())
                cont += 1

            return valor_den

        def calcular(valores):
            denominaciones = [1000, 500, 200, 100, 50, 20, 10, 5, 3, 1]
            cont = 0
            resultado_parcial = []

            for valor in valores:
                if valor == '':
                    resultado_parcial.append(0)
                    cont += 1
                else:
                    resultado_parcial.append(int(valor) * denominaciones[cont])
                    cont += 1

            return resultado_parcial

        def reemplazar_valores(resultado_parcial):
            cont = 0
            resultado_total = 0
            for resultado in resultado_parcial:
                resultado_total += resultado

                texto = StringVar(value=str(resultado))
                entrada_result_parc[cont].config(textvariable=texto)
                cont += 1

            texto_total = StringVar(value=str(resultado_total))
            total.config(textvariable=texto_total)

        # Variables
        denominaciones = ['1000', '500', '200', '100', '50', '20', '10', '5', '3', '1', 'TOTAL']
        valor_den = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        entradas_datos = []
        entrada_result_parc = []
        cont = 0

        # Loop que genera la tabla.
        for visores in range(len(denominaciones)):

            # Crea todas las filas excepto la ultima
            if denominaciones[cont] != 'TOTAL':

                # Columna 0: Etiquetas con las denominaciones y el texto 'TOTAL' en la ultima fila
                etiquetas(5, 0, denominaciones[cont])

                # Columna 1: Signo de multiplicacion 'x'
                etiquetas(4, 1, 'x')

                # Columna 2: Entrada de datos
                ent_obj = entradas(7, 2)
                entradas_datos.append(ent_obj)

                # Columna 3: Signo de igualdad '='
                etiquetas(3, 3, '=')

                # Columna 4: Resultado parcial
                ent_obj = entradas(7, 4, DISABLED)
                texto = StringVar(value='0')
                ent_obj.config(textvariable=texto)
                entrada_result_parc.append(ent_obj)

            else:
                etiquetas(9, 0, 'Total', columnspan=2)
                texto_total = StringVar(value='0')
                total = entradas(18, 2, DISABLED, 4)
                total.config(textvariable=texto_total)

            cont += 1

        bot_calc = boton(27, 'Calcular', 11, columnspan=5)

        bot_calc.config(command=lambda: reemplazar_valores(calcular(replace_table(denominaciones))))
        replace_table(denominaciones)

    # Funciones centrales del programa
    aplicacion = ventana_principal()
    tabla_denominaciones()
    mainloop()


main()
