
def ean(code: str) -> int:
    """
    Berechnet die Prüfziffer für eine europäische Artikelnummer
    """
    if len(code) != 12:
        return -1
    pruefsumme = 0
    for index, digit in enumerate(code):
        factor = 1 if index%2==0 else 3
        pruefsumme += int(digit)*factor
    return 10-pruefsumme % 10

def isbn(code: str) -> int:
    """
    """
    return ean(code)

def ahv(code: str) -> int:
    """
    struktur: Ländercode Personenidentifikationsnummer Prüfziffer
                3 9 1
    Schweiz: 756
    """
    return ean(code)

def laendercode(land: str)-> str:
    """
    """
    encoded_value =""
    for letter in land.upper():
        encoded_value += str(ord(letter)-55)
    return encoded_value

def iban(land: str, bankleitzahl: str, kontonummer: str)-> int:
    """
    """
    land = laendercode(land)+"00"
    bban = kontonummer + bankleitzahl
    testnummer = int(bban + land)
    return 98-testnummer%97

def luhn(code: str) -> int:
    sum = 0
    parity = len(code) % 2
    for index, digit in enumerate(int(x) for x in code):
        if index % 2 == parity:
            digit *= 2
            if digit > 9:
                digit -= 9
        sum += digit
    return sum % 10

def postkonto(code: str) -> int:
    carry_list = [0,9,4,6,8,2,7,1,3,5]
    fullcode =  code
    carry = 0
    for letter in fullcode:
        dummy = (carry + int(letter)) %10
        carry = carry_list[dummy]
    return (10-carry)%10


def main():
    pass

if __name__ == "__main__":
    main()
