from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Caso de prueba para emocion alegria
        result_1 = emotion_detector('I am glad this happened.')
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        # Caso de prueba para emocion enojo
        result_2 = emotion_detector('I am really angry about this')
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        # Caso de prueba para emocion desagrado
        result_3 = emotion_detector('I feel disgusted just hearing about this.')
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        # Caso de prueba para emocion tristeza
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        # Caso de prueba para emocion miedo
        result_5 = emotion_detector('I am very afraid that this will happen.')
        self.assertEqual(result_5['dominant_emotion'], 'fear')

unittest.main()
