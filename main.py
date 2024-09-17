import pandas as pd
from decision_tree import DecisionTree
def main()->None:
    df : pd.DataFrame = pd.read_csv("titanic.csv")
    tree : DecisionTree = DecisionTree(max_depth=5)
    # Remove unnecessary columns
    df = df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)
    # Handle missing values
    df['Age'].fillna(df['Age'].median(), inplace=True)
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
    df['Fare'].fillna(df['Fare'].median(), inplace=True)
    # Feature engineering
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
    # Prepare features and target
    X = df.drop('Survived', axis=1)
    y = df['Survived']
    tree.fit(X,y)
    predictions = tree.predict(X)
    print(predictions)
    """
    aplicação dos algoritmos criados pelo ChatGPT em um conjunto de
    dados e avaliação de seus resultados com matriz de confusão, acurácia, recall, precisão e f1-score. Sugestões de datasets para teste: Iris,
    Penguins, Titanic, Census Income
    """
    #TODO: verificar como dividir o dataset em teste e treino
    #TODO: verificar como realizar as medições
if __name__=='__main__':
    main()