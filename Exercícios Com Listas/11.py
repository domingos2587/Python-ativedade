def intercalar_vetores(vetor1, vetor2, vetor3):
    resultado = []
    for index in range(10):
        resultado.append(vetor1[index])
        resultado.append(vetor2[index])
        resultado.append(vetor3[index])
    return resultado


if __name__ == '__main__':
    vetor1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    vetor2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    vetor3 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    resultado = intercalar_vetores(vetor1, vetor2, vetor3)
    print(resultado)
