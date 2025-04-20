from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

# Cargar preguntas desde un archivo JSON
with open('questions.json') as f:
    questions = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/get_question', methods=['GET'])
def get_question():
    # Aquí podrías implementar lógica para seleccionar una pregunta aleatoria
    question = questions[0]  # Solo como ejemplo
    return jsonify(question)

if __name__ == '__main__':
    app.run(debug=True)