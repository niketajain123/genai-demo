import config
from flask import Flask, request, jsonify, render_template
from llm_service import query_llm
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt')
    temperature = data.get('temperature', 0.7)
    top_p = data.get('top_p', 0.9)
    top_k = data.get('top_k', 50)

    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    try:
        response = query_llm(prompt, temperature, top_p, top_k)
        return jsonify({'response': response})
    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True,port=5000,host="0.0.0.0")
