GoatelasPDFTranslator
1- Nome e Descrição

GoatelasPDFTranslator
Aplicação web em Django que permite ao utilizador carregar um ficheiro PDF, detetar o idioma e traduzir o conteúdo para outro idioma, gerando um novo PDF traduzido.
Interface simples, moderna e responsiva, construída com TailwindCSS.

2- Funcionalidades Principais

Upload de ficheiros PDF até 10 MB.

Deteção automática do idioma original.

Tradução para vários idiomas suportados:
en, pt, es, fr, de, it, ja, zh-CN, zh-TW, ko, hi, th, ar.

Barra de progresso durante a tradução.

Download automático do PDF traduzido.

Layout moderno, responsivo e intuitivo.

3- Tecnologias Utilizadas

Backend: Django 5.x, Python 3.11

Frontend: TailwindCSS, HTML5, JavaScript

Tradução: biblioteca própria (translator.py) com API de tradução (ex.: Google, DeepL, Azure)

PDF: FPDF para gerar PDFs traduzidos

Outros: threading (processos paralelos), uuid (nomes únicos de ficheiros)

4- Estrutura do Projeto (simplificada)
goatelaspdftranslator/
├─ templates/
│  └─ index.html        # Interface principal
├─ static/
│  ├─ css/style.css
│  └─ js/script.js
├─ services/
│  ├─ detector.py       # extrair_texto_pdf, detectar_idioma_pdf
│  └─ translator.py     # traduzir_texto
├─ forms.py             # Formulário de upload
├─ views.py             # Lógica das requisições
├─ urls.py
└─ settings.py

5- Instalação e Configuração
Clonar o repositório
git clone https://github.com/Nelsonfernando2111/GOATELAS_PDF_TRANSLATOR.git
cd GoatelasPdfTranslator

Criar e ativar um ambiente virtual
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate

Instalar dependências
pip install -r requirements.txt

Configurar variáveis de ambiente

Chaves de API de tradução (no .env ou settings.py)

Pasta para guardar uploads/ficheiros traduzidos (MEDIA_ROOT)

Executar migrações e servidor
python manage.py migrate
python manage.py runserver


Acede via: http://127.0.0.1:8000

6- Como Usar

Acede à página inicial.

Carrega o PDF (arrastar ou clicar).

Escolhe o idioma de destino.

Clica em Traduzir PDF.

Aguarda a barra de progresso e descarrega o ficheiro traduzido.

7- Personalização do Template

O ficheiro index.html:

Usa {% load static %} para integrar CSS/JS.

Inclui Tailwind via CDN.

Contém:

Área de upload com drag & drop

Dropdown com idiomas suportados

Barra de progresso

Footer com Política de Privacidade e Termos

Podes alterar cores, fontes ou textos diretamente no template ou no ficheiro style.css.

8- Contribuição

Fazer fork do repositório.

Criar uma branch:

git checkout -b feature/nova-funcionalidade


Submeter pull request após testes.

9- Licença

© 2025 Nelson Murubi — Todos os direitos reservados.
(Opcional: define uma licença aberta, como MIT ou GPL, se preferires)