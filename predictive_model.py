import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Dados de exemplo (deveriam ser extraídos de um banco de dados em produção)
data = {
    'id': range(1, 101),
    'value': [i*10 for i in range(1, 101)],
    'timestamp': pd.date_range(start='1/1/2024', periods=100)
}

df = pd.DataFrame(data)

# Separando em dados de treino e teste
X = df[['id']]
y = df['value']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinando um modelo simples
model = LinearRegression()
model.fit(X_train, y_train)

# Previsão e avaliação
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

print(f'Erro quadrático médio: {mse}')
