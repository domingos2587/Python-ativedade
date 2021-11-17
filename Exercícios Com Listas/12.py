def calcular_altura_media(dados_alunos):
    somatorio_altura = 0
    for idade, altura in dados_alunos:
        somatorio_altura += altura
    altura_media = somatorio_altura / len(dados_alunos)
    return altura_media


def contar_alunos_abaixo_da_altura_media(dados_alunos, altura_media, idade_minima):
    alunos_abaixo_da_media = []
    for idade, altura in dados_alunos:
        if idade >= idade_minima and altura < altura_media:
            alunos_abaixo_da_media.append((idade, altura))
    quantidade = len(alunos_abaixo_da_media)
    return quantidade


if __name__ == '__main__':
    dados_alunos = [
        # (idade, altura)
        (10, 1.35), (10, 1.20), (10, 1.28), (10, 1.22), (10, 1.23),
        (11, 1.35), (11, 1.38), (11, 1.29), (11, 1.50), (11, 1.10),
        (12, 1.35), (12, 1.38), (12, 1.29), (12, 1.50), (12, 1.10),
        (13, 1.35), (13, 1.38), (13, 1.29), (13, 1.50), (13, 1.10),
        (14, 1.35), (14, 1.38), (14, 1.29), (14, 1.50), (14, 1.10),
        (15, 1.60), (15, 1.65), (15, 1.52), (15, 1.70), (15, 1.84),
    ]
    altura_media = calcular_altura_media(dados_alunos)
    count = contar_alunos_abaixo_da_altura_media(dados_alunos, altura_media, idade_minima=14)
    print(count)
