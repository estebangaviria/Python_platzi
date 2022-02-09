from datetime import datetime

## Decorador para convertir en Mayus 
def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura
@mayusculas
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'

## Decorador para conocer el tiempo de ejecicuón de una funcion:
## (*args, **kwargs) hace que no importe la cantidad de argumenos que ingrese a la función 
def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron "+ str(time_elapsed.total_seconds()) + " segundos")
    return wrapper


@execution_time
def random_func():
    # _ no interesa el valor que se está recorriendo
    for _ in range(1,10000000):
        pass


@execution_time
def suma(a: int, b:int) -> int:
    return a + b

@execution_time
def saludo(nombre = "Cesar"):
    print("hola" + nombre)

def run():
    #print(mensaje('Cesar'))
    random_func()
    suma(5,5)
    saludo()

    

if __name__ == '__main__':
    run()