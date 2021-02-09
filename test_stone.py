import unittest
import numpy as np
from desafio_stone import split_bill

class TestSplitBill(unittest.TestCase):

    def test_emptyList(self):
        self.assertEqual(split_bill([], []), 'Lista de itens vazia')

    def test_emptyemail(self):
        self.assertEqual(split_bill([['leite', 4, 5]], []), 'Lista de e-mails vazia')

    def test_float(self):
        self.assertEqual(split_bill([['leite', 4.3, 5.4]], ['email1']), "Inserido float number, por favor verifique seu input")   

    def test_longlist(self):
        email = ['email1','email2', 'email3', 'email4', 'email5']
        itens = np.random.randint(0, 100000, (500000,3)).tolist() #test for long list
        self.assertTrue(split_bill(itens, email))
        
    def test_switch(self):
        email = ['email1','email2', 'email3', 'email4', 'email5']
        itens = [['iogurte', 100, 5], ['chocolate', 200, 10], ['leite', 20, 40], 
        ['feijão', 5, 100], ['arroz', 3, 150], ['carne', 1500, 20]]
        with self.assertRaises(IndexError):
            split_bill(email, itens)

    def test_normal(self):
        email = ['email1','email2', 'email3', 'email4', 'email5']
        itens = [['iogurte', 100, 5], ['chocolate', 200, 10], ['leite', 20, 40], 
        ['feijão', 5, 100], ['arroz', 3, 150], ['carne', 1500, 20]]
        self.assertEqual(split_bill(itens, email), {'email1': 6850, 'email2': 6850, 'email3': 6850, 'email4': 6850, 'email5': 6850})

    def test_reminder(self):
        email = ['email1','email2', 'email3', 'email4', 'email5', 'email6']
        itens = [['iogurte', 100, 5], ['chocolate', 200, 10], ['leite', 20, 40], 
        ['feijão', 5, 100], ['arroz', 3, 150], ['carne', 1500, 20]]
        sum = 0
        dict_email = split_bill(itens, email) # did this way becaus split_bill shuffle email when the reminder is != 0
        for email in dict_email:
            sum += dict_email[email]
        self.assertEqual(sum, 34250)
              
          

if __name__ == '__main__':
    unittest.main()