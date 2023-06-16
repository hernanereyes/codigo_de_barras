import csv


def validar_codigo_barra(codigo_barra):
    if len(codigo_barra) <= 30 and codigo_barra.isdigit():
        return True
    else:
        return False

def exportar_a_csv(datos, nombre_archivo):
    
    with open(nombre_archivo, 'w', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        for fila in datos:
            writer.writerow(fila)
        
    print(f"Los datos han sido exportados a {nombre_archivo} exitosamente.")


datos = []

datos.append(["Código de empresa", "Número de padrón","Fecha de 1er Vencimiento", "Importe", "Digito verificador"])

       
for i in range(5):
    codigo = input("Ingrese el código de barra de longitud 30: ")
    if validar_codigo_barra(codigo):
        numero_str = str(codigo)
 
        primeros3 = numero_str[:3]
        siguientes10 = numero_str[3:13]
        siguientes8 = numero_str[13:21]
        siguientesnro8 = int(numero_str[21:29])
        ultimodigito = numero_str[29:30]
        importe = siguientesnro8 / 100
                
        descripcion_codigo = [primeros3, siguientes10, siguientes8, importe, ultimodigito]        
        datos.append(descripcion_codigo)
               
        print("Código de barra válido.")
        print(f"Código de empresa: {primeros3}")
        print(f"Número padrón: {siguientes10}")
        print(f"Fecha 1er Vencimiento: {siguientes8}")
        print(f"Importe: {importe}")
        print(f"Dígito Verificador: {ultimodigito}")

    else:
        print("Código de barra inválido. Intente nuevamente.")
        
print(datos)
    
exportar_a_csv(datos, "Script_cod.csv")


