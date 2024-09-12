from sklearn.model_selection import train_test_split
import pandas as pd
import pickle

# Replace 'your_dataset.csv' with the path to your dataset file
df = pd.read_csv('Cellphone.csv')

# Assuming your dataset is in a DataFrame called df
X = df[['Sale', 'weight', 'battery']]
y = df['Price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

pickle_out=open("classifier.pkl","wb")
pickle.dump(model,pickle_out)
pickle_out.close()



