import os
import re
from collections import Counter

def analise_temporal_logons():
    diretorio = os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(diretorio, "seguranca.log")
    
    horas_logons = []
    
    with open(caminho, 'r', encoding='utf-8') as f:
        for linha in f:
            if "4624" in linha:
                # O Regex abaixo procura o padrão de hora HH:MM:SS
                match_hora = re.search(r"(\d{2}):\d{2}:\d{2}", linha)
                if match_hora:
                    # Pegamos apenas a hora (ex: "22") para agrupar
                    hora = match_hora.group(1)
                    horas_logons.append(f"{hora}h")

    contagem_tempo = Counter(horas_logons)
    
    print("-" * 35)
    print("⏰ MAPA DE CALOR: LOGONS POR HORA")
    print("-" * 35)
    
    # Ordenar pelas horas do dia (00h até 23h)
    for hora in sorted(contagem_tempo.keys()):
        qtd = contagem_tempo[hora]
        # Criamos uma barra visual para facilitar a leitura
        barra = "█" * (qtd // 20) # Cada '█' representa 20 logons
        print(f"{hora}: {qtd:>4} acessos {barra}")
    
    print("-" * 35)
    print("Dica: Picos de acesso em horários que você não estava")
    print("usando o PC podem indicar processos automáticos ou")
    print("atividades suspeitas.")

if __name__ == "__main__":
    analise_temporal_logons()