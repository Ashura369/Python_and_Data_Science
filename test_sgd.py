from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import r2_score
import warnings

# Suppress warnings to check clean output first, but catch ConvergenceWarning if possible
from sklearn.exceptions import ConvergenceWarning
warnings.filterwarnings("always", category=ConvergenceWarning)

X,y = load_diabetes(return_X_y=True)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=4)

# making prediction using SGDRegressor
# User's parameters: penalty='l2', max_iter=500, eta0=0.1, learning_rate='constant', alpha=0.001
reg = SGDRegressor(penalty='l2', max_iter=500, eta0=0.1, learning_rate='constant', alpha=0.001, random_state=42) 

reg.fit(X_train,y_train)
y_pred = reg.predict(X_test)

print("R2 score : ",r2_score(y_test,y_pred))
# print(reg.coef_)
# print(reg.intercept_)
