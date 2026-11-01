# Anotações do curso de *Python*

# Índice

- [Instalação e Configuração](#instalacao)
- [Introdução](#introducao)

Python é uma linguagem de tipagem dinamica e forte

Javascript é uma linguagem de tipagem dinamica e fraca
<a id="instalacao"></a>

## Instalação e Configuração

- settings.json para terminal/powershell

  ```JSON
  {
      "workbench.iconTheme": "material-icon-theme",
      "git.autofetch": true,
      "explorer.compactFolders": false,
      "vscode-office.editorTheme": "Light",
      "vscode-office.codeMirrorTheme": "Github",
      "workbench.colorTheme": "Dracula Theme Soft",
      "code-runner.runInTerminal":true,
      "code-runner.clearPreviousOutput":true,
      "code-runner.ignoreSelection": true,
      "code-runner.executorMap": {
          "javascript": "node",
          "java": "cd $dir && javac $fileName && java $fileNameWithoutExt",
          "c": "cd $dir && gcc $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
          "zig": "zig run",
          "cpp": "cd $dir && g++ $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
          "objective-c": "cd $dir && gcc -framework Cocoa $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
          "php": "php",
          "python": "cls ; python -u",
          "perl": "perl",
          "perl6": "perl6",
          "ruby": "ruby",
          "go": "go run",
          "lua": "lua",
          "groovy": "groovy",
          "powershell": "powershell -ExecutionPolicy ByPass -File",
          "bat": "cmd /c",
          "shellscript": "bash",
          "fsharp": "fsi",
          "csharp": "scriptcs",
          "vbscript": "cscript //Nologo",
          "typescript": "ts-node",
          "coffeescript": "coffee",
          "scala": "scala",
          "swift": "swift",
          "julia": "julia",
          "crystal": "crystal",
          "ocaml": "ocaml",
          "r": "Rscript",
          "applescript": "osascript",
          "clojure": "lein exec",
          "haxe": "haxe --cwd $dirWithoutTrailingSlash --run $fileNameWithoutExt",
          "rust": "cd $dir && rustc $fileName && $dir$fileNameWithoutExt",
          "racket": "racket",
          "scheme": "csi -script",
          "ahk": "autohotkey",
          "autoit": "autoit3",
          "dart": "dart",
          "pascal": "cd $dir && fpc $fileName && $dir$fileNameWithoutExt",
          "d": "cd $dir && dmd $fileName && $dir$fileNameWithoutExt",
          "haskell": "runghc",
          "nim": "nim compile --verbosity:0 --hints:off --run",
          "lisp": "sbcl --script",
          "kit": "kitc --run",
          "v": "v run",
          "sass": "sass --style expanded",
          "scss": "scss --style expanded",
          "less": "cd $dir && lessc $fileName $fileNameWithoutExt.css",
          "FortranFreeForm": "cd $dir && gfortran $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
          "fortran-modern": "cd $dir && gfortran $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
          "fortran_fixed-form": "cd $dir && gfortran $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
          "fortran": "cd $dir && gfortran $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
          "sml": "cd $dir && sml $fileName",
          "mojo": "mojo run",
          "erlang": "escript",
          "spwn": "spwn build",
          "pkl": "cd $dir && pkl eval -f yaml $fileName -o $fileNameWithoutExt.yaml",
          "gleam": "gleam run -m $fileNameWithoutExt"
      }
  }
  ```
- settings.json para cmd
- ```JSON
  {
      "workbench.iconTheme": "material-icon-theme",
      "git.autofetch": true,
      "explorer.compactFolders": false,
      "vscode-office.editorTheme": "Light",
      "vscode-office.codeMirrorTheme": "Github",
      "workbench.colorTheme": "Dracula Theme Soft",
      "code-runner.runInTerminal":true,
      "code-runner.clearPreviousOutput":true,
      "code-runner.ignoreSelection": true,
      "code-runner.executorMap": {
          "javascript": "node",
          "java": "cd $dir && javac $fileName && java $fileNameWithoutExt",
          "c": "cd $dir && gcc $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
          "zig": "zig run",
          "cpp": "cd $dir && g++ $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
          "objective-c": "cd $dir && gcc -framework Cocoa $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
          "php": "php",
          "python": "cls && python -u",
          "perl": "perl",
          "perl6": "perl6",
          "ruby": "ruby",
          "go": "go run",
          "lua": "lua",
          "groovy": "groovy",
          "powershell": "powershell -ExecutionPolicy ByPass -File",
          "bat": "cmd /c",
          "shellscript": "bash",
          "fsharp": "fsi",
          "csharp": "scriptcs",
          "vbscript": "cscript //Nologo",
          "typescript": "ts-node",
          "coffeescript": "coffee",
          "scala": "scala",
          "swift": "swift",
          "julia": "julia",
          "crystal": "crystal",
          "ocaml": "ocaml",
          "r": "Rscript",
          "applescript": "osascript",
          "clojure": "lein exec",
          "haxe": "haxe --cwd $dirWithoutTrailingSlash --run $fileNameWithoutExt",
          "rust": "cd $dir && rustc $fileName && $dir$fileNameWithoutExt",
          "racket": "racket",
          "scheme": "csi -script",
          "ahk": "autohotkey",
          "autoit": "autoit3",
          "dart": "dart",
          "pascal": "cd $dir && fpc $fileName && $dir$fileNameWithoutExt",
          "d": "cd $dir && dmd $fileName && $dir$fileNameWithoutExt",
          "haskell": "runghc",
          "nim": "nim compile --verbosity:0 --hints:off --run",
          "lisp": "sbcl --script",
          "kit": "kitc --run",
          "v": "v run",
          "sass": "sass --style expanded",
          "scss": "scss --style expanded",
          "less": "cd $dir && lessc $fileName $fileNameWithoutExt.css",
          "FortranFreeForm": "cd $dir && gfortran $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
          "fortran-modern": "cd $dir && gfortran $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
          "fortran_fixed-form": "cd $dir && gfortran $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
          "fortran": "cd $dir && gfortran $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
          "sml": "cd $dir && sml $fileName",
          "mojo": "mojo run",
          "erlang": "escript",
          "spwn": "spwn build",
          "pkl": "cd $dir && pkl eval -f yaml $fileName -o $fileNameWithoutExt.yaml",
          "gleam": "gleam run -m $fileNameWithoutExt"
      }
  }
  ```
- Shortcuts - Atalhos

  Copy line Down
  alt+d

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
