from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from pathlib import Path
import mlflow.sklearn
import bentoml
if __name__ == "__main__":
    iris = load_iris()
    X_train = iris.data[:, :4]
    Y_train = iris.target

    model_uri = Path("models", "IrisClf")
    model = KNeighborsClassifier()
    model.fit(X_train, Y_train)
    mlflow.sklearn.save_model(model, model_uri.resolve())
    bentoml.mlflow.import_model("iris", model_uri)