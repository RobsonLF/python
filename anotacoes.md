# Anotações do curso de *Python*

# Índice
- [Instalação e Configuração](#instalacao)



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

  ## Gerenciamento de Pacotes

    ### Maneira Tradicional. Pip

      - Criando Ambiente Virtual
        - Seleciona o local onde será criado o ambiente virtual
        - python -m venv .venv



    ### Usando UV

<a id="">

## 


</a>