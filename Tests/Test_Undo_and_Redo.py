from Domain.cheltuieli import creeaza_cheltuiala
from Logic.Undo_and_Redo import do_undo, do_redo
from Logic.crud import adaugare
from Tests.Test_Crud import get_info


def test_undo_and_redo():
    lst_cheltuieli = get_info()
    params = creeaza_cheltuiala(7, 3, 3, '11.11.1111', 'canal')
    undo_list = []
    redo_list = []
    new_lst_cheltuieli = adaugare(lst_cheltuieli, *params, undo_list, redo_list)#undo = lista initiala, fara al 7-a cheltuiala
    new_lst_cheltuieli = do_undo(undo_list, redo_list, new_lst_cheltuieli)
    assert new_lst_cheltuieli == lst_cheltuieli
    new_lst_cheltuieli = do_undo(undo_list, redo_list, new_lst_cheltuieli) #undo_list = None => nu se intampla nimic
    assert new_lst_cheltuieli == None
    new_lst_cheltuieli = do_redo(undo_list, redo_list, new_lst_cheltuieli)
    assert len(new_lst_cheltuieli) == len(lst_cheltuieli) + 1
    new_lst_cheltuieli = do_undo(undo_list, redo_list, new_lst_cheltuieli)