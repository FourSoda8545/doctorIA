# Importamos las librerías necesarias de Flask
from flask import Flask, render_template, request

# Inicializamos la aplicación Flask
app = Flask(__name__)

# Diccionario básico de síntomas y diagnósticos para pruebas
diagnoses = {
    "fiebre": "Puede ser una infección viral o bacteriana. Descansa y toma muchos líquidos.",
    "tos": "Podría ser un resfriado común o una infección respiratoria. Si persiste, consulta a un médico.",
    "dolor de cabeza": "Podría ser una migraña o tensión. Descansa y mantente hidratado.",
    "dolor de garganta": "Puede ser una posible irritación de garganta o infección auricular. Toma un desinflamatorio como Dualgos cada 8 horas y descanso de 1 día",
    "me duele el pene": "Posiblemtente tengas sida, podrías considerar cortartelo hijo de tu puta madre",
    
    # Añadir más diagnósticos aquí
}

# Definimos la ruta principal que muestra la página de inicio
@app.route('/')
def home():
    # Renderiza el archivo HTML 'index.html' cuando se accede a la ruta principal
    return render_template('index.html')

# Definimos la ruta para manejar el formulario de diagnóstico
@app.route('/diagnose', methods=['POST'])
def diagnose():
    
    # Obtenemos los síntomas y alergias del formulario enviado por el usuario
    symptoms = request.form.get('symptoms').lower()
    allergies = request.form.get('allergies').lower()
    
    # Buscamos el diagnóstico correspondiente en el diccionario
    diagnosis = diagnoses.get(symptoms, "No se encontró un diagnóstico para los síntomas proporcionados.")
    
    # Renderizamos el archivo HTML 'index.html' con el diagnóstico incluido
    return render_template('index.html', diagnosis=diagnosis)

# Punto de entrada de la aplicación
if __name__ == '__main__':
    # Ejecutamos la aplicación en modo de depuración
    app.run(debug=True)
