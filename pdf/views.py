from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .forms import UploadPDFForm
from .services.detector import extrair_texto_pdf, detectar_idioma_pdf
from .services.translator import traduzir_texto
from fpdf import FPDF
import os
import uuid
import time
import threading

PROGRESS = {}


def index(request):
    """Renderiza a página inicial."""
    form = UploadPDFForm()
    return render(request, "index.html", {"form": form})


def processar_pdf_thread(nome_arquivo, caminho_original, idioma_destino):
    texto_original = extrair_texto_pdf(caminho_original)
    idioma_origem, _ = detectar_idioma_pdf(caminho_original)

    linhas = texto_original.splitlines()
    texto_limpo = "\n".join(l.strip() for l in linhas)

    texto_limpo = " ".join(l.strip() for l in linhas if l.strip())

    try:
        traduzido = traduzir_texto(texto_limpo, idioma_origem, idioma_destino)
    except Exception as e:
        traduzido = f"[ERRO DE TRADUÇÃO: {e}]"

    traduzido = traduzido.replace("\r", " ").replace("\n", " ")
    traduzido = traduzido.encode("utf-8", "ignore").decode("utf-8", "ignore")


    caminho_fonte = os.path.join(settings.BASE_DIR, "static", "fonts", "NotoSans-Regular.ttf")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.add_font("NotoSans", "", caminho_fonte, uni=True)

    pdf.set_font("NotoSans", size=12)
    pdf.multi_cell(0, 8, traduzido, align="J")

    caminho_traduzido = os.path.join(settings.MEDIA_ROOT, f"traduzido_{nome_arquivo}")
    pdf.output(caminho_traduzido, "F")

    PROGRESS[f"{nome_arquivo}_link"] = f"/download_pdf/traduzido_{nome_arquivo}/"
    PROGRESS[nome_arquivo] = 100

def upload_pdf_ajax(request):
    """Recebe o PDF via AJAX e dispara o processamento."""
    if request.method == "POST" and request.FILES.get("arquivo"):
        arquivo = request.FILES["arquivo"]
        idioma_destino = request.POST.get("idioma_destino", "pt")

        nome_arquivo = f"{uuid.uuid4().hex}_{arquivo.name.replace(' ', '_')}"
        caminho_original = os.path.join(settings.MEDIA_ROOT, nome_arquivo)

        with open(caminho_original, "wb+") as destino:
            for chunk in arquivo.chunks():
                destino.write(chunk)

        PROGRESS[nome_arquivo] = 0
        PROGRESS[f"{nome_arquivo}_link"] = None

        threading.Thread(
            target=processar_pdf_thread,
            args=(nome_arquivo, caminho_original, idioma_destino),
            daemon=True,
        ).start()

        return JsonResponse({"status": "ok", "filename": nome_arquivo})

    return JsonResponse({"status": "error", "message": "Arquivo não enviado"})


def progresso_pdf(request, filename):
    """Retorna o progresso e o link de download."""
    return JsonResponse({
        "progresso": PROGRESS.get(filename, 0),
        "download_link": PROGRESS.get(f"{filename}_link"),
    })


def apagar_arquivos_apos_delay(caminhos, delay=60):
    """Apaga os arquivos após um delay em segundos."""
    time.sleep(delay)
    for caminho in caminhos:
        if os.path.exists(caminho):
            try:
                os.remove(caminho)
                print(f"Arquivo {caminho} apagado.")
            except Exception as e:
                print(f"Erro ao apagar {caminho}: {e}")


def download_pdf(request, filename):
    """Permite baixar o PDF traduzido e agenda exclusão dos ficheiros."""
    caminho_traduzido = os.path.join(settings.MEDIA_ROOT, filename)
    caminho_original = os.path.join(settings.MEDIA_ROOT, filename.replace("traduzido_", ""))

    if os.path.exists(caminho_traduzido):
        with open(caminho_traduzido, "rb") as f:
            resp = HttpResponse(f.read(), content_type="application/pdf")
            resp["Content-Disposition"] = f'attachment; filename="{filename}"'

        threading.Thread(
            target=apagar_arquivos_apos_delay,
            args=([caminho_traduzido, caminho_original], 60),
            daemon=True,
        ).start()

        return resp

    return JsonResponse({"status": "error", "message": "Arquivo não encontrado"})


def privacidade(request):
    """Página de política de privacidade."""
    return render(request, "privacidade.html")


def termos(request):
    """Página de Termos de Uso."""
    return render(request, "termos.html")
