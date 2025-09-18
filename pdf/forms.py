from django import forms

IDIOMAS_10 = [
    ('pt', 'Português'),
    ('en', 'Inglês'),
    ('fr', 'Francês'),
    ('es', 'Espanhol'),
    ('de', 'Alemão'),
    ('it', 'Italiano'),
    ('nl', 'Holandês'),
    ('sv', 'Sueco'),
    ('no', 'Norueguês'),
    ('da', 'Dinamarquês'),
    ('zh-CN', 'Chinês (Simplificado)'),
    ('zh-TW', 'Chinês (Tradicional)'),
    ('ja', 'Japonês'),
    ('ko', 'Coreano'),
    ('hi', 'Hindi'),
    ('th', 'Tailandês'),
    ('ar', 'Árabe'),
]

class UploadPDFForm(forms.Form):
    arquivo = forms.FileField(label='Selecione o PDF')
    # Alterar para usar IDIOMAS_10
    idioma_destino = forms.ChoiceField(label='Idioma de destino', choices=IDIOMAS_10)
