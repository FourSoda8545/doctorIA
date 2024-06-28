from flask import Flask, render_template, request

app = Flask(__name__)

# Diccionario básico de síntomas y diagnósticos para pruebas
diagnoses = {
    "fiebre": "Puede ser una infección viral o bacteriana. Descansa y toma muchos líquidos.",
    "tos": "Podría ser un resfriado común o una infección respiratoria. Si persiste, consulta a un médico.",
    "dolor de cabeza": "Podría ser una migraña o tensión. Descansa y mantente hidratado.",
    # Añadir más diagnósticos aquí
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diagnose', methods=['POST'])
def diagnose():
    symptoms = request.form.get('symptoms').lower()
    allergies = request.form.get('allergies').lower()
    diagnosis = diagnoses.get(symptoms, "No se encontró un diagnóstico para los síntomas proporcionados.")
    return render_template('index.html', diagnosis=diagnosis)

if __name__ == '__main__':
    app.run(debug=True)
