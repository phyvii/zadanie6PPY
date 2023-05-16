
class Element:
    def __init__(self, data=None, nextE=None):
        self.data = data
        self.nextE = nextE


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


class Student:
    def __init__(self, email, imie, nazwisko, oceny_projektu, oceny_list, oceny_prace_domowe, status=''):
        self.email = email
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny_projektu = oceny_projektu
        self.oceny_list = oceny_list
        self.oceny_prace_domowe = oceny_prace_domowe
        self.status = status


class MySortedList:
    def __init__(self):
        self.lista = MyLinkedList()

    def insert(self, student):
        element = Element(student)
        if self.lista.head is None:
            self.lista.head = element
            self.lista.tail = element
        else:
            current = self.lista.head
            previous = None
            while current is not None and current.data.nazwisko < student.nazwisko:
                previous = current
                current = current.nextE
            if previous is None:
                element.nextE = self.lista.head
                self.lista.head = element
            else:
                previous.nextE = element
                element.nextE = current
                current = element
            if current.nextE is None:
                self.lista.tail = current
        self.lista.size += 1

    def remove(self, email):
        current = self.lista.head
        previous = None
        while current is not None and current.data.email != email:
            previous = current
            current = current.nextE
        if current is None:
            return
        if previous is None:
            self.lista.head = current.nextE
        else:
            previous.nextE = current.nextE
        if current.nextE is None:
            self.lista.tail = previous
        self.lista.size -= 1

    def display(self):
        current = self.lista.head
        while current is not None:
            print(current.data.email)
            current = current.nextE


class Lista:
    def __init__(self):
        self.students = MySortedList()

    def wyswietl_studentow(self):
        current = self.students.lista.head
        while current is not None:
            student = current.data
            print(f"Email: {student.email}")
            print(f"Imię: {student.imie}")
            print(f"Nazwisko: {student.nazwisko}")
            print(f"Oceny projektu: {student.oceny_projektu}")
            print(f"Oceny list: {student.oceny_list}")
            print(f"Oceny prac domowych: {student.oceny_prace_domowe}")
            print(f"Status: {student.status}")
            print("-----------------------------")
            current = current.nextE

    def wystaw_oceny(self):
        current = self.students.lista.head
        while current is not None:
            student = current.data
            if student.status != 'GRADED' and student.status != 'MAILED':
                oceny_prace_domowe = student.oceny_prace_domowe

                if len(oceny_prace_domowe) == 6:
                    srednia_prace_domowe = sum(oceny_prace_domowe) / len(oceny_prace_domowe)
                    if srednia_prace_domowe >= 80:
                        student.oceny_projektu = [40]
                        student.oceny_list = [20, 20, 20]
                    elif srednia_prace_domowe >= 70:
                        student.oceny_projektu = [40]
                        student.oceny_list = [20, 20]
                    elif srednia_prace_domowe >= 60:
                        student.oceny_projektu = [40]
                        student.oceny_list = [20]
                student.status = 'GRADED'
            current = current.nextE

    def dodaj_studenta(self, email, imie, nazwisko, oceny_projektu, oceny_list, oceny_prace_domowe):
        student = Student(email, imie, nazwisko, oceny_projektu, oceny_list, oceny_prace_domowe)
        self.students.insert(student)
        print('Dodano nowego studenta.')

    def usun_studenta(self, email):
        self.students.remove(email)
        print('Usunięto studenta.')

    def wyslij_email(self, email, imie, nazwisko, ocena, nowy_status=''):

        print(f'Wysłano email z oceną do {email}.')
        if nowy_status:
            student = self.znajdz_studenta(email)
            if student:
                student.status = nowy_status

    def znajdz_studenta(self, email):
        current = self.students.lista.head
        while current is not None:
            if current.data.email == email:
                return current.data
            current = current.nextE
        return None

    def wyslij_emaile(self, statusy):
        current = self.students.lista.head
        while current is not None:
            student = current.data
            if student.status in statusy:
                ocena = student.oceny_projektu[0]
                self.wyslij_email(student.email, student.imie, student.nazwisko, ocena, student.status)
                student.status = 'MAILED'
            current = current.nextE


def main():
    lista = Lista()

    student1 = Student("none@gmail.com", "ann", "annovsky", [-1], [-1, -1, -1], [-1, -1, -1, -1, -1, -1])
    student2 = Student("test@gmail.com", "alice", "novak", [40], [20, 20, 20], [100, 100, 100, 100, 100, 5])
    student3 = Student("test2@gmail.com", "bob", "bobowsky", [40], [20, 20, 20], [100, 100, 100, 100, 100, 5])
    student4 = Student("test3@gmail.com", "chris", "czajkowsky", [-1], [20, 20, -1], [100, 100, 100, 100, 100, -1])
    student5 = Student("test4@gmail.com", "Derek", "Derkowsky", [-1], [20, 20, -1], [100, 100, 100, 100, 100, -1])

    lista.dodaj_studenta(student1.email, student1.imie, student1.nazwisko, student1.oceny_projektu,
                              student1.oceny_list, student1.oceny_prace_domowe)
    lista.dodaj_studenta(student2.email, student2.imie, student2.nazwisko, student2.oceny_projektu,
                              student2.oceny_list, student2.oceny_prace_domowe)
    lista.dodaj_studenta(student3.email, student3.imie, student3.nazwisko, student3.oceny_projektu,
                              student3.oceny_list, student3.oceny_prace_domowe)
    lista.dodaj_studenta(student4.email, student4.imie, student4.nazwisko, student4.oceny_projektu,
                              student4.oceny_list, student4.oceny_prace_domowe)
    lista.dodaj_studenta(student5.email, student5.imie, student5.nazwisko, student5.oceny_projektu,
                              student5.oceny_list, student5.oceny_prace_domowe)

    while True:
        print('\n====MENU====')
        print('1. Wystaw oceny')
        print('2. Dodaj studenta')
        print('3. Usuń studenta')
        print('4. Wyślij emaile')
        print('5. Zakończ program')
        print('6. Wyświetlić studentów')
        wybor = input('Wybierz opcję: ')

        if wybor == '1':
            lista.wystaw_oceny()
            print('Oceny zostały wystawione.')

        elif wybor == '2':
            email = input('Podaj email studenta: ')
            imie = input('Podaj imię studenta: ')
            nazwisko = input('Podaj nazwisko studenta: ')
            oceny_projektu = [40]
            oceny_list = [20, 20, 20]
            oceny_prace_domowe = [100, 100, 100, 100, 100, 100]
            lista.dodaj_studenta(email, imie, nazwisko, oceny_projektu, oceny_list, oceny_prace_domowe)

        elif wybor == '3':
            email = input('Podaj email studenta do usunięcia: ')
            lista.usun_studenta(email)

        elif wybor == '4':
            statusy = input('Podaj statusy (oddzielone przecinkami) dla których chcesz wysłać emaile: ')
            statusy = [status.strip() for status in statusy.split(',')]
            lista.wyslij_emaile(statusy)
            print('Emaile zostały wysłane.')

        elif wybor == '5':
            break
        elif wybor == '6':
            lista.wyswietl_studentow()

        else:
            print('Nieprawidłowywybór.Spróbuj ponownie.')


main()
