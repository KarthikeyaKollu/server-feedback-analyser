from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
from flask import Flask, request, jsonify
from flask_cors import CORS
import io
from data import callModel
app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/process_text', methods=['POST'])
def process_text():
    if request.method == 'POST':
       
        title=request.form.get('query', '')
        
        # Process the text data using your model
        print(title)
        processed_data = callModel(title)
        
        
        
        # Return the processed data as a JSON response
        return jsonify({'message': processed_data})
    
 

@app.route('/process_image', methods=['POST'])
def process_image_endpoint():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image_file = request.files['image']
    image_text = request.form.get('imageText', '')  # Get text data from form
    
    image_data = io.BytesIO(image_file.read())  

    text_response = process_image(image_data, image_text)
    return jsonify({'message': text_response})



def process_image(image_data, image_text):
    image = Image.open(image_data)
    # Perform image processing
    processed_image = gemini_pro_vision(image,image_text)
    
    # Combine image processing result with text
    combined_result = f"{processed_image}"
    
    return combined_result











if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

