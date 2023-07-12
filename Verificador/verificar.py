def verifica(self):
    if not isinstance(self, int):
        raise TypeError("Escolha uma das opções numéricas disponíveis!\n")
    elif 1 < self > 4:
        raise ValueError("Escolha uma das opções disponíveis!\n")