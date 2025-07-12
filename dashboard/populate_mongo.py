from mongoengine import connect
from dashboard.models_mongo import Lpar, Resource, History, Alert, Dashboard
from datetime import datetime, timedelta
import random

# Conectar ao MongoDB
connect(db='corewatch_db', host='localhost', port=27017)

# Lista de letras gregas para nomear as LPARs
greek_letters = [
    'Alfa', 'Beta', 'Gama', 'Delta', 'Épsilon', 'Zeta',
    'Eta', 'Theta', 'Iota', 'Kappa', 'Lambda', 'Mi',
    'Ni', 'Xi', 'Omicron', 'Pi', 'Rô', 'Sigma', 'Tau',
    'Upsilon', 'Phi', 'Chi', 'Psi', 'Ômega'
]

# Limpa os dados existentes
Lpar.objects.delete()
Resource.objects.delete()
History.objects.delete()
Alert.objects.delete()
Dashboard.objects.delete()

# Cria LPARs
lpars = []
for i, name in enumerate(greek_letters):
    lpar = Lpar(
        idLpar=i + 1,
        nameLpar=name,
        account=f"account_{i}",
        ip=f"192.168.1.{i+10}",
        luname=f"LU_{i}",
        lparEnv="Prod" if i % 2 == 0 else "Dev"
    ).save()
    lpars.append(lpar)

    # Cria Resources para cada LPAR
    for j in range(2):  # 2 recursos por LPAR
        Resource(
            idResource=(i + 1) * 10 + j,
            idLpar=lpar,
            nameResource=f"Resource_{j}",
            value=round(random.uniform(20.0, 90.0), 2),
            resourceDescription="Uso de CPU" if j == 0 else "Uso de MSU"
        ).save()

    # Cria Históricos
    for d in range(50):  # 3 dias anteriores
        History(
            idHistory=(i + 1) * 100 + d,
            idLpar=lpar,
            uso_cpu=round(random.uniform(30.0, 85.0), 2),
            uso_msu=round(random.uniform(100.0, 250.0), 2),
            valor_smf=round(random.uniform(0.0, 100.0), 2),
            timestamp=datetime.now() - timedelta(days=d)
        ).save()

    # Cria Alertas
    if random.choice([True, False]):
        Alert(
            idAlert=i + 1,
            idLpar=lpar,
            type="CPU",
            message=f"Uso de CPU alto em {name}",
            level=random.choice(["warning", "critical"]),
            timestamp=datetime.now()
        ).save()

    # Dashboard (um por LPAR)
    Dashboard(
        idDashboard=i + 1,
        idLpar=lpar,
        resumo=f"Resumo do desempenho da LPAR {name}",
        status="ativo" if i % 2 == 0 else "inativo"
    ).save()


print("MongoDB populado com sucesso com LPARs, Resources, Histories, Alerts e Dashboards.")
