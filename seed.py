from mnemonic import Mnemonic
from eth_account import Account

def generate_seed_phrase(strength=128):
    mnemo = Mnemonic("english")  # Используем английский язык для сид фразы
    seed_phrase = mnemo.generate(strength=strength)  # Генерируем сид фразу указанной длины
    return seed_phrase

# Пример использования:
seed_phrase = generate_seed_phrase()
Account.enable_unaudited_hdwallet_features()
acct = Account.from_mnemonic(seed_phrase)
address = acct.address  # Получаем адрес кошелька из аккаунта

print("Ваша сид фраза: ")
print(seed_phrase)
print(address)
