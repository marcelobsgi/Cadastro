
import flet as ft
import time
from flet import *

def main(page):

    dict_values = {
        'beneficiario': '',
        'carteira': '',
        'UF': '',
        'medicamento_1': '',
        'cod_tuss_1':'',
        'qtd_1':'',
        'medicamento_2': '',
        'cod_tuss_2': '',
        'qtd_2': '',
        'nome_medico': '',
        'crm': '',
        'uf': '',
        'data_prescricao': '',
    }

    def salvar(e):
        dict_values['beneficiario'] = contratante.value
        dict_values['carteira'] = medida_judicial.value
        dict_values['uf'] = outra_parte.value
        dict_values['medicamento_1'] = prolabore.value
        dict_values['cod_tuss_1'] = exito.value
        dict_values['qtd_1'] = foro.value
        dict_values['medicamento_2'] = data.value 
        dict_values['cod_tuss_2'] = data.value
        dict_values['qtd_2'] = data.value
        dict_values['nome_medico'] = data.value
        dict_values['crm'] = data.value
        dict_values['uf_crm'] = data.value
        dict_values['data_prescricao'] = data.value


        for val in dict_values.values():
            if not val:
                page.banner.open=True
                page.update()
                return
            
        print('Já é possivel gerar o contrato')
        print(dict_values)

    def fecha_banner (e):
        page.banner.open=False
        page.update()

#____Banner___Popup__
    page.banner = Banner(
        bgcolor=colors.AMBER_100,
        leading=Icon(
            icons.DANGEROUS_SHARP,
            color=colors.RED_400,
            size=40
        ),
        content=Text('Todos os campos são de preenchimento obrigatório.'),
        actions=[
            TextButton(
                'Ok',
                on_click=fecha_banner
            )
        ]
    )

    titulo = Text(value='Cadastro do Cliente', size=20, weight='bold')
    beneficiario = TextField(label='Nome do Beneficiário', autofocus=True)
    carteira = TextField(label='Catrteira')
    UF = TextField(label='UF')
    medicamento_1 = TextField(label='Medicamento 1')
    cod_tuss_1 = TextField(label='TUSS 1')
    qtd_1 = TextField(label='Quantidade 1')
    medicamento_2 = TextField(label='Medicamento 2')
    cod_tuss_2 = TextField(label='Quantidade 2')
    qtd_2 = TextField(label='Quantidade 2')
    nome_medico = TextField(label='Nome do Médico')
    crm = TextField(label='CRM')
    uf_crm = TextField(label='UF do Médico')
    data_prescricao = TextField(label='Data da Prescrição')

    
    btn_salvar = FilledButton(text='Salvar', on_click= salvar)



    page.add(Row(controls = [titulo]),
        Row(controls=[beneficiario,carteira,UF]),
        Row(controls=[medicamento_1,cod_tuss_1,qtd_1]),
        Row(controls=[medicamento_2,cod_tuss_2,qtd_2]),
        Row(controls=[nome_medico,crm,uf_crm,data_prescricao]),
        Row(controls=[btn_salvar])
    )

ft.app(target=main)
#ft.app(target=main, view=ft.WEB_BROWSER, port=8000)
