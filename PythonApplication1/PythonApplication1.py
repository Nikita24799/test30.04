import operator 
from random import randint
import names
import numpy as np 
 
class Allowance: #обьявляем класс 
    def __init__(self, num_applicants): #это конструктор для класса. 
        self.applicants = {names.get_first_name(): randint(0, 100) for _ in range(num_applicants)}
 
    def menu(self): #функция меню
        print("\n1 - Узнать список поступивших в вуз людей",
              "\n2 - Отобразить в алфавитном порядке список людей и их баллы",
              "\n3 - Найти n людей с худшими результатами",
              "\n4 - Найти средний балл поступивших",
              "\n5 - Выход")
        inpt = int(input("Выберите вариант: "))
 
        if inpt == 1:
            print(self.list_applicants(5))
        elif inpt == 2:
            print(self.sort_people_and_scores())
        elif inpt == 3:
            print(self.find_worst_results_people(5))
        elif inpt == 4:
            print(self.find_avg_score())
        elif inpt == 5:
            exit()
 
    def list_applicants(self, num_applicants): #функция сделана, чтобы узнать список поступивших в вуз людей
        return sorted(self.applicants.items(), key=operator.itemgetter(1))[len(self.applicants) - num_applicants:] 
 
    def sort_people_and_scores(self): #функция для сортировки людей в алфавитном порядке список людей и их баллы
        return sorted(self.applicants.items(), key=operator.itemgetter(0))
 
    def find_worst_results_people(self, num_worst_results): #находим людей с худшими результатами
        sorted_tuples = sorted(self.applicants.items(), key=operator.itemgetter(1))[:num_worst_results] #key=operator.itegmetter(1) функция , которая захватывает первый элемент из объекта типа списка
        return {k: v for k, v in sorted_tuples} #сортировка людей по худшиму результату
 
    def find_avg_score(self): #нахождение среднего балла для поступивших 
        return np.mean([i for i in self.applicants.values()]) #вычисляем среднее значение балла для поступивших
    
    while True:
        main.menu()
