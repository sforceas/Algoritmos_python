from bokeh.plotting import figure, output_file, show #figure permite generar la imagen, output_file nos permite exportar a formatos como html, show crea un "servidor interno" para poder visualizar el html en el navegador.

if __name__=='__main__':
    output_file('graficado_simple.html')
    fig = figure()

    total_val = int(input('Cuantos valores quieres graficar?'))
    x_vals = list(range(total_val)) #genera una lista rango iniciando en 0
    y_vals = [] #inicializamos la lista

    for x  in x_vals: #loop
        val = int(input(f'Valor Y para la X {x}'))
        y_vals.append(val) #añade al final de la lista el valor
    
    fig.line(x_vals, y_vals,line_width=10)
    show(fig)
