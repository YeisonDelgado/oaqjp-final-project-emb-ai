from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detect():
    # Obtener texto de la solicitud
    text_to_analyze = request.args.get('textToAnalyze')

    # Llamar a la función de detección de emociones
    result = emotion_detector(text_to_analyze)
    print(result)

    # Verifica si el label es None, lo que indica un error o entrada no válida
    if result['dominant_emotion'] is None:
        return "¡Texto inválido! ¡Por favor, inténtalo de nuevo!."
    else:
        # Extraer emociones
        anger = result['anger']
        disgust = result['disgust']
        fear = result['fear']
        joy = result['joy']
        sadness = result['sadness']
        dominant = result['dominant_emotion']

        # Formatear la respuesta como se pidió
        response_text = (
            f"Para la declaración dada, la respuesta del sistema es "
            f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
            f"'joy': {joy} y 'sadness': {sadness}. "
            f"La emoción dominante es {dominant}."
            )
        return response_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)
