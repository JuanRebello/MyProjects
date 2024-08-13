import sys
import os   
from cx_Freeze import setup, Executable



# escondendo o console 

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

# saída de arquivos

configuracao = Executable(
    script='app.py',
    base = base
)
# Configurar o cxfreeze(detalhes do programa)
setup(
    name = 'Login e Registro de usuário',
    version = '1.0',
    description = 'Sistema de login e Resgistro',
    author = 'Juan Rebello',
    options ={'build_exe': {'include_msvcr': True}},
    executables = [configuracao]
)