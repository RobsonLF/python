@echo off
REM Cria o ambiente virtual chamado 'venv' (se ainda não existir)
if not exist venv (
    echo Criando ambiente virtual...
    python -m venv venv
)
REM Ativa o ambiente virtual
echo Ativando o ambiente virtual...
call venv\Scripts\activate.bat

echo Ambiente virtual pronto e ativado.
cmd /k