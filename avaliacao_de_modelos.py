import numpy as np
import pandas as pd

def confusion_matrix(y_true, y_pred, labels=None):
    """
    Calcula a matriz de confusão para os rótulos verdadeiros e preditos.

    Parâmetros:
    y_true: array-like de rótulos verdadeiros.
    y_pred: array-like de rótulos preditos.
    labels: array-like dos rótulos únicos (opcional). Se não fornecido, será inferido a partir de y_true.

    Retorna:
    Uma matriz de confusão (DataFrame).
    """
    if labels is None:
        labels = np.unique(y_true)
    
    # Inicializa a matriz de confusão com zeros
    matrix : pd.DataFrame = pd.DataFrame(np.zeros((len(labels), len(labels)), dtype=int), index=labels, columns=labels)
    
    # Preenche a matriz com as contagens
    for true_label, predicted_label in zip(y_true, y_pred):
        matrix.at[true_label, predicted_label] += 1
    
    return matrix
def accuracy(conf_matrix)->float:
    """
    Calcula a acurácia a partir da matriz de confusão.
    
    Parâmetros:
    conf_matrix: DataFrame (ou array) representando a matriz de confusão.
    
    Retorna:
    Acurácia (float).
    """
    total_correct = np.trace(conf_matrix)  # Soma dos elementos da diagonal principal (acertos)
    total_samples = conf_matrix.sum().sum()  # Soma de todos os elementos da matriz (total de amostras)
    return total_correct / total_samples
def precision(conf_matrix: pd.DataFrame)->dict:
    """
    Calcula a precisão para cada classe a partir da matriz de confusão.
    
    Parâmetros:
    conf_matrix: DataFrame (ou array) representando a matriz de confusão.
    
    Retorna:
    Um dicionário com a precisão de cada classe.
    """
    precisions = {}
    for label in conf_matrix.columns:
        true_positive = conf_matrix.at[label, label]  # Verdadeiros positivos (diagonal)
        predicted_positive = conf_matrix[label].sum()  # Soma da coluna (todos os preditos como essa classe)
        precisions[label] = true_positive / predicted_positive if predicted_positive > 0 else 0
    return precisions
def recall(conf_matrix:pd.DataFrame)->dict:
    """
    Calcula o recall para cada classe a partir da matriz de confusão.
    
    Parâmetros:
    conf_matrix: DataFrame (ou array) representando a matriz de confusão.
    
    Retorna:
    Um dicionário com o recall de cada classe.
    """
    recalls = {}
    for label in conf_matrix.index:
        true_positive = conf_matrix.at[label, label]  # Verdadeiros positivos (diagonal)
        actual_positive = conf_matrix.loc[label].sum()  # Soma da linha (todos os reais dessa classe)
        recalls[label] = true_positive / actual_positive if actual_positive > 0 else 0
    return recalls
def f1_score(conf_matrix:pd.DataFrame)->dict:
    """
    Calcula o F1 Score para cada classe a partir da matriz de confusão.
    
    Parâmetros:
    conf_matrix: DataFrame (ou array) representando a matriz de confusão.
    
    Retorna:
    Um dicionário com o F1 Score de cada classe.
    """
    precisions = precision(conf_matrix)  # Calcula precisão
    recalls = recall(conf_matrix)  # Calcula recall
    f1_scores = {}

    for label in conf_matrix.index:
        p = precisions[label]
        r = recalls[label]
        if (p + r) > 0:
            f1_scores[label] = 2 * (p * r) / (p + r)
        else:
            f1_scores[label] = 0  # Evita divisão por zero quando p + r = 0

    return f1_scores
