from pathlib import Path
from config import BUDGET_FILE_PATH
from entities.expence import Expence


class BudgetRepository:
    """Luokka, joka vastaa sovelluksen yhteydestä budjetti tietoihin
    """

    def __init__(
            self,
            file_path
    ):
        """Luokan konstrukti.

        Args:
            file_path: tiedosto, johon tiedot tallennetaan
        """

        self._file_path = file_path

    def _file_exists(
            self
    ):
        """Varmistaa, että tiedosto on olemassa
        """

        Path(self._file_path).touch()

    def add_expence(
            self,
            expence
    ):
        """Lisää tiedostoon menon

        Args:
            expence: menoa tai tuloa kuvaava olio
        Returns:
            menot ja tulot
        """

        expences = self.find_all()

        expences.append(expence)
        self._write(expences)

        return expences

    def delete_expence(
            self,
            e_id
    ):
        """Poistaa menon/tulon tiedostosta

        Args:
            e_id: Menon/tulon id
        """

        expences = self._read()
        expences_copy = expences

        for expence in expences_copy:
            if expence.expence_id == e_id:
                expences.remove(expence)
                break

        self._write(expences)

    def find_all(
            self
    ):
        """Hakee tiedostosta kaikki menot

        Returns:
            Palauttaa kaikki menot ja tulot
        """

        return self._read()

    def delete_all(
            self
    ):
        """Poistaa kaikki menot ja tulot
        """

        self._write([])

    def _read(
            self
    ):
        """Tiedostosta lukeva osa

        Returns:
            Menot ja tulot, jotka ovat tiedostossa
        """

        expences = []

        self._file_exists()

        with open(self._file_path, 'r', encoding='utf-8') as file:
            for row in file:
                row = row.replace('\n', "")
                parts = row.split(';')

                expence_id = parts[0]
                expence = parts[1]
                expence_amount = parts[2]
                expence_description = parts[3]
                username = parts[4]
                date = parts[5]

                expences.append(
                    Expence(expence, expence_amount,
                            expence_description, username, date, expence_id)
                )

        return expences

    def _write(
            self,
            expences
    ):
        """Tiedostoon kirjoittava osa

        Args:
            expences: menot ja tulot jotka kirjoitetaan tiedostoon
        """

        self._file_exists()

        with open(self._file_path, 'w', encoding='utf-8') as file:
            for expence in expences:
                line1 = f'{expence.expence_id};{expence.expence};{expence.amount};'
                line2 = f'{expence.description};{expence.username};{expence.date}'

                file.write(line1+line2+'\n')


budget_repository = BudgetRepository(BUDGET_FILE_PATH)
