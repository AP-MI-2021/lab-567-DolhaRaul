from Domain.cheltuieli import creeaza_cheltuiala, get_str, get_nr_ap, get_suma, get_data, get_tipul
from Logic.crud import adaugare, read, modif, stergere


def show_menu():
    print('1.CRUD')
    print('2.Stergerea tuturor cheltuielilor pentru un apartament dat')
    print('x.Oprire')


def handle_add(lst_cheltuieli):
    nr_ap = int(input('Introduceti numarul apartamentului aici: '))
    suma = int(input('Introduceti suma cheltuielii aici: '))
    data = input('Introduceti data in care s - a emis cheltuiala in format DD.MM.YYYY aici: ')
    tip = input('Introduceti tipul cheltuielii aici: ')
    new_cheltuiala = creeaza_cheltuiala(nr_ap, suma, data, tip)
    lst_cheltuieli = adaugare(lst_cheltuieli, nr_ap, suma, data, tip)
    return lst_cheltuieli

def handle_show_all(lst_cheltuieli):
    for cheltuiala in lst_cheltuieli:
        print(get_str(cheltuiala))


def handle_show_details(lst_cheltuieli):
    nr_ap = int(input('Introduceti aici Numarul cheltuielii despre care vrem sa aflam detalii: '))
    cheltuiala = read(lst_cheltuieli, nr_ap)
    if cheltuiala:#exista aceasta cheltuiala, nu am introdus ceva ce nu exista
        print(f'Nr_apartament:{get_nr_ap(cheltuiala)}')
        print(f'Suma:{get_suma(cheltuiala)}')
        print(f'Data:{get_data(cheltuiala)}')
        print(f'Tip:{get_tipul(cheltuiala)}')
    else:
        print('Nu exista o asmenea cheltuiala, este gresita!')


def handle_modif(lst_cheltuieli):
    nr_ap = int(input('Dati numarul apartamentului al cheltuielii care se actualizeaza: '))
    suma = int(input('Dati aici noua suma a cheltuielii: '))
    data = input('Dati aici noua data a cheltuielii: ')
    tip = input('Dati aici noul tip al cheltuielii: ')
    new_cheltuiala = creeaza_cheltuiala(nr_ap, suma, data, tip)
    return modif(lst_cheltuieli, new_cheltuiala)


def handle_delete(lst_cheltuieli):
    nr_ap = int(input('Dati aici numele cheltuielii care doriti sa se modifice: '))
    lst_cheltuieli = stergere(lst_cheltuieli, nr_ap)
    print("S-a sters cu succes cheltuiala!")
    return lst_cheltuieli

def handle_crud(lst_cheltuieli):
    while True:
        print('1.Creeaza')
        print('2.Modifica')
        print('3.Sterge')
        print('a.Afiseaza_cheltuieli')
        print('d.Afiseaza_detalii_cheltuiela')
        print('b.Revenire')
        optiune = input('Introduceti optiunea dorita aici: ')
        if optiune == '1':
            lst_cheltuieli = handle_add(lst_cheltuieli)
        elif optiune == '2':
            lst_cheltuieli = handle_modif(lst_cheltuieli)
        elif optiune == '3':
            lst_cheltuieli = handle_delete(lst_cheltuieli)
        elif optiune == 'a':
            handle_show_all(lst_cheltuieli)
        elif optiune == 'd':
            handle_show_details(lst_cheltuieli)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida')
    return lst_cheltuieli

def run_ui(lst_cheltuieli):
    while True:
        show_menu()
        optiune = input('Introduceti optiunea dorita aici: ')
        if optiune == '1':
            lst_cheltuieli = handle_crud(lst_cheltuieli)
        elif optiune == 'x':
            break
    return lst_cheltuieli