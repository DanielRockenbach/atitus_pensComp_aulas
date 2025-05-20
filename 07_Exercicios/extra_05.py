def status_aluno(notas): # Extra 05  
    notas_validas = [nota for nota in notas if nota is not None]

<<<<<<< HEAD
    if not notas_validas:
        return False
=======
def test():
    assert status_aluno([10, 10, 10, 10])
    assert status_aluno([10, None, 10, 10])
>>>>>>> 043c61666b61699165f87a4d2a78813f467719c2

<<<<<<< HEAD
    media = sum(notas_validas) / len(notas_validas)
=======
    assert not status_aluno([10, 5, None, 5])
    assert not status_aluno([5, 5, 5, 5])
    assert not status_aluno([0, 0, 0, 0])
>>>>>>> 043c61666b61699165f87a4d2a78813f467719c2

<<<<<<< HEAD
    return media >= 7

def test():
    assert status_aluno([10, 10, 10, 10])
    assert status_aluno([10, None, 10, 10])
    assert not status_aluno([10, 5, None, 5])
    assert not status_aluno([5, 5, 5, 5])
    assert not status_aluno([0, 0, 0, 0])

=======
>>>>>>> 043c61666b61699165f87a4d2a78813f467719c2