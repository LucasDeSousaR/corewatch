from django.shortcuts import render
from .models_mongo import Lpar, History
from collections import defaultdict
from django.utils.timezone import localtime, make_aware
from datetime import datetime

def index(request):
    # Busca todas as LPARs do banco
    lpars = Lpar.objects.all()
    return render(request, 'dashboard/index.html', {'lpars': lpars})

def lpar_list(request):
    lpars = Lpar.objects.all()
    return render(request, 'dashboard/lpar_list.html', {'lpars': lpars})


def lpar_detail(request, lpar_id):
    # Busca a LPAR usando o campo correto (idLpar)
    lpar = Lpar.objects(idLpar=lpar_id).first()
    if not lpar:
        return render(request, 'dashboard/not_found.html', status=404)

    # Busca o histórico relacionado a essa LPAR, ordenado por data
    historicos = History.objects(idLpar=lpar).order_by('timestamp')

    # Prepara os dados para os gráficos
    timestamps = [h.timestamp.strftime('%d/%m %H:%M') for h in historicos]
    cpu_data = [h.uso_cpu for h in historicos]
    msu_data = [h.uso_msu for h in historicos]
    smf_data = [h.valor_smf for h in historicos]

    return render(request, 'dashboard/detail.html', {
        'lpar': lpar,
        'timestamps': timestamps,
        'cpu_data': cpu_data,
        'msu_data': msu_data,
        'smf_data': smf_data,
    })

def lpar_chart(request, lpar_id):
    lpar = Lpar.objects(idLpar=lpar_id).first()
    if not lpar:
        return render(request, 'dashboard/not_found.html', status=404)

    historicos = History.objects(idLpar=lpar).order_by('timestamp')

    # Agrupar por dia
    data_agrupada = defaultdict(lambda: {'uso_cpu': 0, 'uso_msu': 0, 'valor_smf': 0, 'count': 0})
    for h in historicos:
        aware_timestamp = make_aware(h.timestamp)
        data_str = localtime(aware_timestamp).strftime('%Y-%m-%d')
        data_agrupada[data_str]['uso_cpu'] += h.uso_cpu
        data_agrupada[data_str]['uso_msu'] += h.uso_msu
        data_agrupada[data_str]['valor_smf'] += h.valor_smf or 0  # Garantir que valor_smf não seja None
        data_agrupada[data_str]['count'] += 1

    # Calcular média por dia
    dias = sorted(data_agrupada.keys())
    uso_cpu = [round(data_agrupada[d]['uso_cpu'] / data_agrupada[d]['count'], 2) for d in dias]
    uso_msu = [round(data_agrupada[d]['uso_msu'] / data_agrupada[d]['count'], 2) for d in dias]
    valor_smf = [round(data_agrupada[d]['valor_smf'] / data_agrupada[d]['count'], 2) for d in dias]

    return render(request, 'dashboard/lpar_chart.html', {
        'lpar': lpar,
        'dias': dias,
        'uso_cpu': uso_cpu,
        'uso_msu': uso_msu,
        'valor_smf': valor_smf,
    })
