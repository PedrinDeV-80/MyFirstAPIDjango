from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.timezone import now
from .models import Cotacao
from .serializers import CotacaoSerializers
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets, generics


from cambio_facil.models import Pessoa, Cotacao
from cambio_facil.serializers import PessoaSerializer, CotacaoSerializers


class PessoaViewSet(viewsets.ModelViewSet):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    #permission_classes = [permissions.AllowAny]

    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    http_method_names = ['get', 'post', 'put', 'path','delete']

import yfinance as yf

def buscar_cotacoes_em_tempo_real():
    try:
        ticker_brl = yf.Ticker("USDBRL=X")
        info_brl = ticker_brl.info

        real_por_dolar = None
        if 'regularMarketPrice' in info_brl:
            real_por_dolar = float(info_brl['regularMarketPrice'])
        elif 'currentPrice' in info_brl:
            real_por_dolar = float(info_brl['currentPrice'])

        ticker_eur = yf.Ticker("EURUSD=X")
        info_eur = ticker_eur.info

        euro_por_dolar = None
        euro_por_dolar_raw = None
        if 'regularMarketPrice' in info_eur:
            euro_por_dolar_raw = float(info_eur['regularMarketPrice'])
        elif 'currentPrice' in info_eur:
            euro_por_dolar_raw = float(info_eur['currentPrice'])

        if euro_por_dolar_raw is not None and euro_por_dolar_raw != 0:
            euro_por_dolar = 1 / euro_por_dolar_raw


        if real_por_dolar is not None and euro_por_dolar is not None:
            return {
                "dolar": 1.0,
                "real": real_por_dolar,
                "euro": euro_por_dolar,
            }
        else:
            raise ValueError("Não foi possível obter todas as cotações necessárias com yfinance (dados ausentes ou inválidos).")

    except Exception as e:
        print(f"Erro ao buscar cotações com yfinance: {e}")
        return {
            "dolar": 1.0,
            "real": 5.00,
            "euro": 0.92,
        }

print(buscar_cotacoes_em_tempo_real())

class CotacaoViewSet(viewsets.ModelViewSet):
    queryset = Cotacao.objects.all()
    serializer_class = CotacaoSerializers
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def list(self, request, *args, **kwargs):

        try:

            cotacoes_atuais = buscar_cotacoes_em_tempo_real()

            return Response(cotacoes_atuais)

        except Exception as e:

            return Response({"erro": f"Não foi possível obter as cotações em tempo real: {e}"}, status=500)