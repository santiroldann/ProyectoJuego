from django.test import TestCase

from .models import Juego
# Create your tests here.

class JuegoTest(TestCase):
    
    def setUp(self):
        Juego.objects.create(juego="COD", grupo=1)
        
    def test_juego_nombre(self):
            juego = Juego.objects.get(grupo=1)
            self.assertEqual(juego.juego, "COD")      
            
    def test_juego_creado(self):
            juego = Juego.objects.get(grupo=1)
            self.assertNotEquals(juego, None)


    