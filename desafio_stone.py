import numpy as np
from random import shuffle

def split_bill(itens_list, persons_list):
    """
    This function helps split the shop list bill.

    Arguments:

    itens_list -- A list of lists itens with item, qty, price/qty 
    eg.: [[item1, qty1, price1/qty1], [item_1, qty_1, price_1/qty_1], ...., [item_n, qty_n, price_n/qty_n]]
    person_list -- List containing e-mail, the bill is gonna by divide equally by e-mail
    eg.: [email_1, email_2, ..., email_n]

    Return:

    dict_valeu_per_person --  A python dict where the keys is the e-mail (person_list) and the value is the split bill
    """
    try:
        if not itens_list[0] or not persons_list:
            if not itens_list[0]:
                print("Lista de itens vazia")
            elif not persons_list:
                print("Lista de e-mails vazia")
        else:
            array_itens_list = np.array(itens_list) #turn in a np.ndarray where each row is a different item
            values = array_itens_list[:,1: ].astype(int) 
            sum_itens = np.sum(np.prod(values, axis=1)) #vectorazation

            L = len(persons_list) #how many e-mail exists
            dict_valeu_per_person = {} #final answer
            if sum_itens%L == 0:
                value_per_person = sum_itens/L
                for email in b:
                    dict_valeu_per_person[email] = int(value_per_person)
            else:
                reminder = sum_itens%L
                reminder_ = reminder #to make sure I'm gonna split the reminder correctly
                if (sum_itens - reminder)%L == 0:
                    value_per_person = (sum_itens - reminder)/L
                    shuffle(b)
                    for email in b:
                        dict_valeu_per_person[email] = int(value_per_person) + int(1 if reminder_ > 0 else 0)
                        reminder_ -= 1
                else:
                    print("(Soma do itens - resto) % quantidade de pessoas: {}".format((sum_itens - reminder)%L))
    except Exception as e:
        print(e)

    
    return dict_valeu_per_person