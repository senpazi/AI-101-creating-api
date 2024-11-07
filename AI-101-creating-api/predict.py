

def predict():
    # Get JSON data from the request
    data = request.get_json()

    # Extract features from the JSON data
    sepal_length = data['SepalLengthCm']
    sepal_width = data['SepalWidthCm']
    petal_length = data['PetalLengthCm']
    petal_width = data['PetalWidthCm']
    
    # Format input for the model
    input_features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    # Make a prediction
    predicted_class = model.predict(input_features)
    predicted_species = label_encoder.inverse_transform(predicted_class)

    # Return the result as JSON
    return jsonify({'Predicted Species': predicted_species[0]})