import numpy as np
import pandas as pd

class DecisionTree:
    def __init__(self, max_depth=None, min_samples_split=2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.tree = None

    def fit(self, X:pd.DataFrame, y):
        dataset = X.copy()
        dataset['label'] = y
        self.tree = self._build_tree(dataset)

    def predict(self, X:pd.DataFrame):
        return X.apply(self._predict_row, axis=1)

    def _entropy(self, y):
        # Calcula a entropia dos rótulos
        unique_classes, class_counts = np.unique(y, return_counts=True)
        probabilities = class_counts / len(y)
        return -np.sum(probabilities * np.log2(probabilities))

    def _information_gain(self, left_y, right_y, parent_entropy):
        # Calcula o ganho de informação após uma divisão
        left_weight = len(left_y) / (len(left_y) + len(right_y))
        right_weight = len(right_y) / (len(left_y) + len(right_y))
        child_entropy = (left_weight * self._entropy(left_y) +
                         right_weight * self._entropy(right_y))
        return parent_entropy - child_entropy

    def _best_split(self, dataset):
        # Encontra a melhor divisão
        best_gain = 0
        best_feature = None
        best_split_value = None
        parent_entropy = self._entropy(dataset['label'])
        
        for feature in dataset.columns[:-1]:
            values = dataset[feature].unique()
            for value in values:
                left_split = dataset[dataset[feature] <= value]
                right_split = dataset[dataset[feature] > value]
                
                if len(left_split) == 0 or len(right_split) == 0:
                    continue
                
                gain = self._information_gain(left_split['label'], right_split['label'], parent_entropy)
                
                if gain > best_gain:
                    best_gain = gain
                    best_feature = feature
                    best_split_value = value
        
        return best_feature, best_split_value, best_gain

    def _build_tree(self, dataset, depth=0):
        # Função recursiva para construir a árvore de decisão
        X = dataset.drop(columns=['label'])
        y = dataset['label']
        
        # Critérios de parada
        if len(np.unique(y)) == 1:
            return np.unique(y)[0]  # Folha com uma única classe
        if len(X) < self.min_samples_split or (self.max_depth is not None and depth >= self.max_depth):
            return y.mode()[0]  # Folha com a classe majoritária
        
        # Melhor divisão
        best_feature, best_split_value, best_gain = self._best_split(dataset)
        
        if best_gain == 0:
            return y.mode()[0]  # Folha com a classe majoritária
        
        left_split = dataset[dataset[best_feature] <= best_split_value]
        right_split = dataset[dataset[best_feature] > best_split_value]
        
        # Nós filhos
        node = {
            'feature': best_feature,
            'value': best_split_value,
            'left': self._build_tree(left_split, depth + 1),
            'right': self._build_tree(right_split, depth + 1)
        }
        
        return node

    def _predict_row(self, row):
        node = self.tree
        while isinstance(node, dict):
            if row[node['feature']] <= node['value']:
                node = node['left']
            else:
                node = node['right']
        return node
