# Anotações do curso de *Python*

# Índice
- [Instalação e Configuração](#instalacao)
- [Introdução](#introducao)



<a id="instalacao"></a>

## Instalação e Configuração
  - settings.json
    ```
      {
      "gitlens.ai.model": "vscode",
      "gitlens.ai.vscode.model": "copilot:gpt-4.1",
      "explorer.compactFolders": false,
      "diffEditor.codeLens": true,
      "code-runner.runInTerminal": true,
      "code-runner.clearPreviousOutput": true,
      "code-runner.executorMap": {
          "javascript": "node",
          "java": "cd $dir && javac $fileName && java $fileNameWithoutExt",
          "c": "cd $dir && gcc $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
          "php": "php",
          "python": "clear ; python -u",
      },
      "code-runner.ignoreSelection": false,
      "workbench.colorTheme": "OM Theme (Default Dracula Italic)",
      "workbench.iconTheme": "material-icon-theme",
      "python.defaultInterpreterPath": "python"
      }
    ```
  - Shortcuts - Atalhos

    Copy line Down <br>
    Shift+Alt+seta pra baixo

<a id="introducao"></a>

## Introdução

  ### Comentários em Python
    - Comentários em python: 
      - `#`;
      - Comentário simples, uma única linha.
    - Docstring: 
      - Possibilita multicomentario;
      - """ """. A Docstring é lida pelo interpretador, porém não é executada.

  ### Função Print
    - A função print já tem alguns padrões para exibição da saída na tela
      - Apresenta espaços entre argumentos não nomeados
      - Apresenta quebra de linha por função
    - É possivel alterar o separador
      - print(12, 34, sep='-')
        - 12-34
      - print(12, 34, sep='*')  
        - 12*34  
    - Argumentos de quebra de linha
      - print(12, 34, sep='-', end='##')
      - print(56, 78, sep='*')  
        - 12-34##56*78

  ### Tipos de dados
    - Python possui uma Dinâmica e Forte
      - Tipagem Dinâmica - Detecta o tipo do dado sem a necessidade de declaração prévia. 
      - Tipagem Forte    - 
  
  ### String
[Arquivo Aula2.py](/curso-udemy/secao3/aula2.py)

    - Aspas simples
      - print('Robson "Luis"')
    - Aspas duplas
      - print("Robson 'Luis'")
    - Escape
      - print("Robson \"Luis\"")
    - r
      - print(r"Robson \"Luis\"")

  ### Int e Float



<a id=""></a>

## 


