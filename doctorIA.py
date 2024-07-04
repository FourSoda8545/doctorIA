# Importamos las librerías necesarias de Flask
from flask import Flask, request
from flask import render_template as rt 

# Inicializamos la aplicación Flask
app = Flask(__name__)

# Diccionario básico de síntomas y diagnósticos para pruebas
diagnoses = {
    "fiebre": "Puede ser una infección viral o bacteriana. Descansa y toma muchos líquidos.",
    "tos": "Podría ser un resfriado común o una infección respiratoria. Si persiste, consulta a un médico.",
    "dolor de cabeza": "Podría ser una migraña o tensión. Descansa y mantente hidratado.",
    "dolor de garganta": "Puede ser una posible irritación de garganta o infección auricular. Toma un desinflamatorio como Dualgos cada 8 horas y descanso de 1 día",
    "": "",
    
    # Añadir más diagnósticos aquí
}

# Definimos la ruta principal que muestra la página de inicio
@app.route('/')
def home():
    # Convertimos el archivo HTML 'index.html' a visual
    return rt('index.html')

# Definimos la ruta para manejar el formulario de diagnóstico
@app.route('/diagnose', methods=['POST'])
def diagnose():
    
    # Obtenemos los síntomas y alergias del formulario enviado por el usuario
    sintomas = request.form.get('sintomas').lower()
    alergias = request.form.get('alergias').lower()
    
    # Buscamos el diagnóstico correspondiente en el diccionario
    diagnosis = diagnoses.get(sintomas, "No se encontró un diagnóstico para los síntomas proporcionados.")
    
    # Renderizamos el archivo HTML 'index.html' con el diagnóstico incluido
    return rt('index.html', diagnosis=diagnosis)

# Punto de entrada de la aplicación
if __name__ == '__main__':
    # Ejecutamos la aplicación en modo de depuración
    app.run(debug=True)
