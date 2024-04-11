from builder import *
import sys


def main():
    regexp = input("Введите регулярное выражение: ")

    nfda = create_nfda(regexp)
    nfda.show_automata(1)

    fda = convert_to_fda(nfda)
    fda.show_automata(2)

    mfda = minimize_fda(fda)
    mfda.show_automata(3)

    while(True):
        check = input("Введите строку для моделирования МКА (для выхода введите 'N'): ")
        if check == 'N' or check == 'n':
            exit()
        else:
            mfda.model_check(check)

main()