import joblib


def load_model(filename="model.pkl"):
    return joblib.load(filename)


def load_feature_and_target_names(filename="feature_target_names.pkl"):
    with open(filename, "rb") as f:
        feature_names, target_names = joblib.load(f)

    return feature_names, target_names


def predict(model, target_names, data: dict) -> str:
    features = [
        [
            data["sepal_length"],
            data["sepal_width"],
            data["petal_length"],
            data["petal_width"],
        ]
    ]
    prediction = model.predict(features)
    return str(target_names[prediction[0]])
