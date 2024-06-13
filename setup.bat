@echo off

color 1
REM Configuração do ambiente Python
echo Instalando pacotes necessarios...

pip install colorama
pip install tabulate
pip install pandas
pip install google.generativeai
pip install numpy

REM Solicitação da API Key do Google AI Studio
set /p APIKEY="Digite sua API Key do Google AI Studio: "

REM Definindo a variável de ambiente APIKEY
echo Configurando variável de ambiente APIKEY...
setx APIKEY %APIKEY%

echo Setup concluído com sucesso!
pause
