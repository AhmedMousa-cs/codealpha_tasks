import os
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image
import cv2
from keras.models import load_model
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
from tensorflow.keras.preprocessing.image import load_img, img_to_array

app = Flask(__name__)

# Create uploads folder if it doesn't exist
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model = load_model('model.h5')
print('Model loaded. Check http://127.0.0.1:5000/')

labels = ['Healthy', 'Powdery', 'Rust']


def getResult(image_path):
    img = load_img(image_path, target_size=(225, 225))  # Changed to 225x225
    x = img_to_array(img)
    x = x.astype('float32') / 255.
    x = np.expand_dims(x, axis=0)
    predictions = model.predict(x)[0]
    return predictions


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        try:
            # Check if file is in request
            if 'file' not in request.files:
                return jsonify({'error': 'No file provided'}), 400

            f = request.files['file']

            # Check if file is selected
            if f.filename == '':
                return jsonify({'error': 'No file selected'}), 400

            # Save file
            basepath = os.path.dirname(__file__)
            file_path = os.path.join(
                basepath, 'uploads', secure_filename(f.filename))
            f.save(file_path)

            # Get predictions
            predictions = getResult(file_path)
            predicted_label = labels[np.argmax(predictions)]

            # Clean up - delete uploaded file after prediction
            try:
                os.remove(file_path)
            except:
                pass

            return str(predicted_label)

        except Exception as e:
            print(f"Error during prediction: {str(e)}")
            return jsonify({'error': str(e)}), 500

    return None


if __name__ == '__main__':
    app.run(debug=True)