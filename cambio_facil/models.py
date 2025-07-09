from django.db import models

# Create your models here.
class Pessoa(models.Model):
    idade = models.IntegerField()
    altura = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    peso = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    nome= models.CharField(max_length=50)
class Cotacao(models.Model):
    data = models.DateField(auto_now_add=True)  # registra a data automaticamente
    real = models.DecimalField(max_digits=10, decimal_places=5, default=1.0)  # BRL como base
    euro = models.DecimalField(max_digits=10, decimal_places=5)
    dolar = models.DecimalField(max_digits=10, decimal_places=5)

    def __str__(self):
        return f"Cotação em {self.data}: EUR {self.euro}, USD {self.dolar}"