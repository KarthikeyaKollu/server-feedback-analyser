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
    
 












if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

