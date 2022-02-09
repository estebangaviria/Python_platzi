


def make_repeater_of(n):
    def print_all(string):
        assert type(string) == str, "Solo se aceptan cadenas"
        return string*n
    return print_all

def make_division_by(divisor: int):
    def division_of(dividendo: int):
        return dividendo / divisor
    return division_of

def make_division_by_(n):
    return lambda x: x/n





def run():

    times10 = make_repeater_of(10)
    print(times10('Esteban '))

    dividir_by_2 = make_division_by(2)
    print(dividir_by_2(10))

    dividir_by_3 = make_division_by_(3)
    print(dividir_by_3(18))

if __name__ == '__main__':
    run()