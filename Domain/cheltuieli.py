def creeaza_cheltuiala(nr_apartament: int, suma: float, data: str, tipul: str):
    '''
    Creeaza o cheltuiala in care sa fie specificata nr_apartament, suma, data(in format string: 'DD.MM.YYYY') si tipul
    care poate fi:cheltuiala, intretinere sau alte cheltuieli
    :param nr_apartament:Numarul apartaentului
    :param suma:Suma cheltuielii
    :param data:Data in care se face cheltuiala
    :param tipul:Tipul cheltuielii(va fi precizat, in format string)
    :return: Creeaza cheltuiala cu datele introduse
    '''
    return{
        'nr_ap':nr_apartament,
        'suma':suma,
        'data':data,
        'tip':tipul,
    }

def get_nr_ap(cheltuiala):
    '''
    Returneaza nr_ap al cheltuielii(se comporta ca un id)
    :param cheltuiala: O cheltuiala introdusa de utilizator
    :return: Nr apartamentului in care e trecut cheltuiala
    '''
    return cheltuiala['nr_ap']

def get_suma(cheltuiala):
    '''
    Returneaza suma cheltuielii
    :param cheltuiala: O cheltuiala introdusa de utilizator
    :return: Suma acesteia
    '''
    return cheltuiala['suma']

def get_data(cheltuiala):
    '''
    Returneaza data cheltuielii
    :param cheltuiala: O cheltuiala introdusa de utilizator
    :return: Data acesteia
    '''
    return cheltuiala['data']

def get_tipul(cheltuiala):
    '''
    Returneaza tipul cheltuielii(cum este)
    :param cheltuiala: O cheltuiala introdusa de utilizator
    :return: Tipul acesteia
    '''
    return cheltuiala['tip']

def get_str(cheltuiala):
    return f'Nr_apartamentului este {get_nr_ap(cheltuiala)}, cu suma {get_suma(cheltuiala)}, data {get_data(cheltuiala)} si tipul {get_tipul(cheltuiala)}'