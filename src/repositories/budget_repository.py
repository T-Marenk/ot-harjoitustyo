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

    def find_all(
            self
    ):
        """Hakee tiedostosta kaikki menot
        
        Returns:
            Palauttaa kaikki menot ja tulot
        """


        return self._read()

    def _read(
            self
    ):
        expences = []

        self._file_exists()

        with open(self._file_path) as file:
            for row in file:
                row = row.replace('\n', "")
                p = row.split(';')

                expence_id = p[0]
                expence_description = p[1]
                expence_amount = p[2]

                expences.append(
                        Expence(expence_description, expence_amount, expence_id)
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
        
        with open(self._file_path, 'w') as file:
            for expence in expences:
                line = f'{expence.expence_id};{expence.expence};{expence.amount}'

                file.write(line+'\n')

budget_repository = BudgetRepository(BUDGET_FILE_PATH)
