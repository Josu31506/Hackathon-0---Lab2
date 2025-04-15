def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def calculate():
    while True:
        operacion = input("Escribe la operación (ej: 2 + 2) o 'c' para limpiar: ").strip()
        if operacion.lower() == 'c':
            continue
        try:
            resultado = eval(operacion)
            print("Resultado:", resultado)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    calculate()
