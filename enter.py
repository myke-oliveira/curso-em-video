def enter(f, msn):
    while True:
        try:
            return f(input(msn))
        except ValueError:
            print('Valor digitado inválido')