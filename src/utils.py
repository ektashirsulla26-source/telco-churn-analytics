# utils.py

from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_auc_score
)
import matplotlib.pyplot as plt
from sklearn.metrics import RocCurveDisplay


def evaluate_model(model, X_test, y_test):
    """
    Evaluate classification model performance.
    Prints classification report and ROC-AUC score.
    """
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    print("Classification Report:\n")
    print(classification_report(y_test, y_pred))

    print("ROC-AUC Score:", roc_auc_score(y_test, y_prob))


def plot_roc_curve(model, X_test, y_test):
    """
    Plot ROC Curve for classification model.
    """
    RocCurveDisplay.from_estimator(model, X_test, y_test)
    plt.title("ROC Curve")
    plt.show()