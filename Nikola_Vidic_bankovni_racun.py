import random
import datetime
import os


company_name = ""
company_street_and_number = ""
company_postal_code = ""
company_city = ""
company_tax_id = ""
company_manager = ""

account_number = ""
import datetime
import os
import random

account_balance = 0.0
transactions = []


def generate_account_number():
    """Funkcija generira i vraća broj računa.

    Broj računa treba biti u obliku BA-YYYY-MM-RRRRR, gdje je YYYY trenutna
    godina, MM trenutni mjesec, upisan na 2 mjesta, s 0 ispred ako je mjesec
    manji od 10, a RRRRR proizvoljno generirani broj od 1 do 99999, nadopunjen
    nulama do 5 znakova.

    Potrebno je uzeti trenutnu godinu i mjesec (ne hardkodirati), a broj
    generirati (mora biti drugačiji prilikom svakog pokretanja).

    Na primjer, BA-2023-03-00047.
    """
    year = datetime.datetime.now().strftime("%Y")
    month = datetime.datetime.now().strftime("%m")
    random_number = str(random.randint(1, 99999)).zfill(5)
    account_number = f"BA-{year}-{month}-{random_number}"
    return account_number


def generate_transaction(amount):
    """Funkcija generira transakciju zadanog iznosa.

    Transakcija mora sadržavati točan datum generiranja transakcije, vrijeme
    generiranja transakcije, broj računa (generiran je prilikom kreiranja
    računa) i iznos transakcije.

    Sami odlučite kako želite spremati podatke o pojedinoj transakciji.
    """
    transaction = {
        "date": datetime.datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.datetime.now().strftime("%H:%M:%S"),
        "account_number": generate_account_number(),
        "amount": amount
    }
    return transaction
def withdraw_screen():
    """Ekran koji omogućava podizanje novca s računa.

    Iznos koji se podiže mora biti pozitivan realni broj i ne smije biti veći od
    trenutnog stanja računa. Ako je iznos negativan (ili 0), potrebno je od
    korisnika zatražiti ponovni unos. Isto vrijedi i ako je iznos veći od
    trenutnog stanja računa.

    Potrebno je generirati i spremiti transakciju (iznos u transakciji mora biti
    negativan zbog podizanja novca) te ažurirati trenutno stanje računa.

    Nakon završetka, potrebno je od korisnika zatražiti da pritisne tipku ENTER
    i potom ga vratiti u glavni izbornik.
    """
    global account_balance

    amount = float(input("Unesite iznos € koji želite podići: "))
    while amount <= 0.0 or amount > account_balance:
        print("Iznos mora biti pozitivan i ne smije biti veći od trenutnog stanja računa! Molimo pokušajte ponovo...")
        amount = float(input("Unesite iznos € koji želite podići: "))

    transaction = generate_transaction(-amount)
    transactions.append(transaction)

    account_balance -= amount

    input("\nZa nastavak pritisnite ENTER...")
    main_menu()


def deposit_screen():
    """Ekran koji omogućava polog novca na račun.

    Iznos koji se polaže mora biti pozitivan realni broj. Ako je iznos negativan
    (ili 0), potrebno je od korisnika zatražiti ponovni unos.

    Potrebno je generirati i spremiti transakciju te ažurirati trenutno stanje
    računa.

    Nakon završetka, potrebno je od korisnika zatražiti da pritisne tipku ENTER
    i potom ga vratiti u glavni izbornik.
    """
    global account_balance

    amount = float(input("Unesite iznos € koji želite uplatiti: "))
    while amount <= 0.0:
        print("Iznos mora biti pozitivan!")
        amount = float(input("Unesite iznos: "))

    transaction = generate_transaction(amount)
    transactions.append(transaction)

    account_balance += amount

    input("\nZa nastavak pritisnite ENTER...")
    main_menu()


def view_transactions_screen():
    """Prikaz svih transakcija.

    Ekran treba ispisati redom sve transakcije (svaku u novi red). Za svaku
    transakciju je potrebno ispisati sve podatke koje ona sadrži, a to su
    broj računa, datum generiranja transakcije, vrijeme generiranja transakcije
    i iznos transakcije.

    Na početku ekrana je potrebno ispisati i ukupno trenutno stanje računa.

    Nakon završetka, potrebno je od korisnika zatražiti da pritisne tipku ENTER
    i potom ga vratiti u glavni izbornik.
    """
    global account_balance

    print(f"\nUkupno stanje računa: €{account_balance:.2f}\n")
    for transaction in transactions:
        print(f"Broj računa: {transaction['account_number']}")
        print(f"Datum: {transaction['date']}")
        print(f"Vrijeme: {transaction['time']}")
        print(f"Iznos: €{transaction['amount']:.2f}\n")

    input("\nZa nastavak pritisnite ENTER...")
    main_menu()


def balance_screen():
    """Prikaz ukupnog stanja računa.

    Potrebno je ispisati broj računa, trenutni datum i vrijeme te ukupno
    trenutno stanje računa.

    Nakon završetka, potrebno je od korisnika zatražiti da pritisne tipku ENTER
    i potom ga vratiti u glavni izbornik.
    """
    global account_balance

    print(f"\nBroj računa: {generate_account_number()}")
    print(f"Datum: {datetime.datetime.now().strftime('%Y-%m-%d')}")
    print(f"Vrijeme: {datetime.datetime.now().strftime('%H:%M:%S')}")
    print(f"Ukupno stanje računa: € {account_balance:.2f}\n")

    input("\nZa nastavak pritisnite ENTER...")
    main_menu()


def main_menu():
    os.system("cls" if os.name == "nt" else "clear")

    print("*" * 65)
    print("PyBANK ALGEBRA\n")
    print("GLAVNI IZBORNIK\n")

    print("(1) Prikaz stanja računa")
    print("(2) Prikaz prometa po računu")
    print("(3) Polog novca na račun")
    print("(4) Podizanje novca s računa")

    print("\n(0) Izlaz")

    choice = int(input("\nAkcija: "))
    while choice < 0 or choice > 4:
        print("Molim odaberite samo broj ispred željene akcije!")
        choice = int(input("Akcija: "))

    if choice == 1:
        balance_screen()
    elif choice == 2:
        view_transactions_screen()
    elif choice == 3:
        deposit_screen()
    elif choice == 4:
        withdraw_screen()
    elif choice == 0:
        exit()


def open_account():
    os.system("cls" if os.name == "nt" else "clear")

    print("*" * 65)
    print("PyBANK ALGEBRA\n")
    print("KREIRANJE RAČUNA\n")
    print("Podaci o vlasniku računa\n")

    global account_balance

    company_name = input("Naziv: ")
    while not company_name.isalpha():
        print("Naziv tvrtke mora sadržavati samo slova.")
        company_name = input("Naziv: ")

    company_street_and_number = input("Ulica i broj: ")

    company_postal_code = input("Poštanski broj (5 znamenki): ")
    while not company_postal_code.isdigit() or len(company_postal_code) != 5:
        print("Poštanski broj mora sadržavati samo 5 znamenki.")
        company_postal_code = input("Poštanski broj (5 znamenki): ")

    company_city = input("Grad: ")
    while not company_city.isalpha():
        print("Grad mora sadržavati samo slova.")
        company_city = input("Grad: ")

    company_tax_id = input("OIB: ")
    # .isdigit() vraća True ako su sve znamenke u stringu brojke
    while len(company_tax_id) != 11 or not company_tax_id.isdigit():
        print("OIB mora imati točno 11 brojki. Molim ponovite unos.")
        company_tax_id = input("OIB: ")

    company_manager = input("Ime i prezime vlasnika: ")
    while not all(name.isalpha() or name.isspace() for name in company_manager.split()):
        print("Ime i prezime vlasnika moraju sadržavati samo slova.")
        company_manager = input("Ime i prezime vlasnika: ")

    input("\nZa nastavak pritisnite ENTER...")

    account_balance = float(input("Iznos € koji želite položiti na račun: "))
    while account_balance <= 0.0:
        print("Iznos mora biti pozitivan!")
        account_balance = float(input("Unesite iznos: "))

    transaction = generate_transaction(account_balance)
    transactions.append(transaction)

    input("\nZa nastavak pritisnite ENTER...")


open_account()

while True:
    main_menu()
