def horoscopo(mes):
    if mes <= 0 or mes > 12:
        return None
    if mes <= 3:
        return "Python"
    if mes <= 6:
        return "Java"
    if mes <= 9:
        return "PHP"
    else:
        return "TypeScript"

def test():
    assert horoscopo(1) == "Python"
    assert horoscopo(2) == "Python"
    assert horoscopo(3) == "Python"
    
    assert horoscopo(4) == "Java"
    assert horoscopo(5) == "Java"
    assert horoscopo(6) == "Java"
    
    assert horoscopo(7) == "PHP"
    assert horoscopo(8) == "PHP"
    assert horoscopo(9) == "PHP"
    
    assert horoscopo(10) == "TypeScript"
    assert horoscopo(11) == "TypeScript"
    assert horoscopo(12) == "TypeScript"
    
    assert horoscopo(-1) is None
    assert horoscopo(0) is None
    assert horoscopo(13) is None
    
print(horoscopo(10))
print(horoscopo(-1))
print(horoscopo(0))
