# Definindo uma matriz de confusão arbitrária
VP = 50  # Verdadeiros Positivos
VN = 30  # Verdadeiros Negativos
FP = 10  # Falsos Positivos
FN = 5   # Falsos Negativos

# Função para calcular a acurácia
def calcular_acuracia(vp, vn, fp, fn):
    return (vp + vn) / (vp + vn + fp + fn)

# Função para calcular a sensibilidade (recall)
def calcular_sensibilidade(vp, fn):
    return vp / (vp + fn)

# Função para calcular a especificidade
def calcular_especificidade(vn, fp):
    return vn / (vn + fp)

# Função para calcular a precisão
def calcular_precisao(vp, fp):
    return vp / (vp + fp)

# Função para calcular o F-score
def calcular_f_score(precisao, sensibilidade):
    return 2 * (precisao * sensibilidade) / (precisao + sensibilidade)

# Calculando as métricas
acuracia = calcular_acuracia(VP, VN, FP, FN)
sensibilidade = calcular_sensibilidade(VP, FN)
especificidade = calcular_especificidade(VN, FP)
precisao = calcular_precisao(VP, FP)
f_score = calcular_f_score(precisao, sensibilidade)

# Exibindo os resultados
print(f"Acurácia: {acuracia:.2f}")
print(f"Sensibilidade (Recall): {sensibilidade:.2f}")
print(f"Especificidade: {especificidade:.2f}")
print(f"Precisão: {precisao:.2f}")
print(f"F-score: {f_score:.2f}")