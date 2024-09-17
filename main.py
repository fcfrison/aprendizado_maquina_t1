import pandas as pd
from decision_tree import DecisionTree
from avaliacao_de_modelos import *
def imprime_dict(dict_instance:dict, metrica:str)->None:
    print(f"métrica: {metrica}")
    for key,value in dict_instance.items():
        print(f"rótulo: {key}, pontuação: {value}")
    return
def pre_processing_titanic(df:pd.DataFrame)->pd.DataFrame:
    df = df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)
    # Handle missing values
    df['Age'].fillna(df['Age'].median(), inplace=True)
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
    df['Fare'].fillna(df['Fare'].median(), inplace=True)
    # Feature engineering
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
    return df
def main()->None:
    df : pd.DataFrame = pd.read_csv("titanic.csv")
    tree : DecisionTree = DecisionTree(max_depth=5)
    # Remove unnecessary columns
    df = pre_processing_titanic(df)
    # Prepare features and target
    X = df.drop('Survived', axis=1)
    y = df['Survived']
    tree.fit(X,y)
    predictions = tree.predict(X)
    print(predictions)
    conf_matrix_df : pd.DataFrame = confusion_matrix(y,predictions)
    accuracy_value : float = accuracy(conf_matrix=conf_matrix_df)
    recall_dict : dict = recall(conf_matrix=conf_matrix_df)
    precision_dict :dict = precision(conf_matrix=conf_matrix_df)
    f1_score_dict : dict = f1_score(conf_matrix=conf_matrix_df)
    print(f"matriz de confusão: {conf_matrix_df}")
    print(f"acurácia: {accuracy_value}")
    imprime_dict(recall_dict,"recall")
    imprime_dict(precision_dict,"precision")
    imprime_dict(f1_score_dict,"f1 score")
if __name__=='__main__':
    main()
