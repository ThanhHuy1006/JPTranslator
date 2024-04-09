from flask import Flask, request, render_template
from googletrans import Translator
import nltk
nltk.download('punkt') 

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate')
def translate():
    text = request.args.get('text', '')
    
    # Phân tách từ
    tokens = nltk.word_tokenize(text)
    parsed_text = ' '.join(tokens)
    
    # Dịch văn bản đã được phân tách từ
    translated_text = translator.translate(parsed_text, src='vi', dest='ja').text
    
    return translated_text

if __name__ == '__main__':
    app.debug = False  # Ẩn cảnh báo "This is a development server"
    app.run(host='0.0.0.0', port=5000)
