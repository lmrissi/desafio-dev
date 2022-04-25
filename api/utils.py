import datetime
from .models import Cnab, CnabTransactionsTypes, Store

def parse_cnab_file (cnab_file):
    date_format = "%Y%m%d"
    cnab_dict_list = []
    
    for line in cnab_file:
        cnab_dict = dict(
            type = int(line[0:1].decode("utf-8")),
            date = datetime.datetime.strptime(line[1:9].decode("utf-8"), date_format).date(),
            value = round(float(int(line[9:19].decode("utf-8"))/100),2),
            cpf = line[19:30].decode("utf-8"),
            card = line[30:42].decode("utf-8"),
            hour = datetime.time(
                int(line[42:44].decode("utf-8")),
                int(line[44:46].decode("utf-8")),
                int(line[46:48].decode("utf-8"))
            ),
            store_owner = line[48:62].decode("utf-8"),
            store_name = line[62:81].strip().decode("utf-8"),
        )
        cnab_dict_list.append(cnab_dict)

    return cnab_dict_list
    
def save_parsed_cnab(parsed_cnab_dict_list):
    is_store_saved(parsed_cnab_dict_list)

    for cnab_dict in parsed_cnab_dict_list:
        cnab = Cnab()

        cnab.type=CnabTransactionsTypes.objects.get(type=cnab_dict["type"])
        cnab.date=cnab_dict["date"]
        cnab.value=cnab_dict["value"]
        cnab.cpf=cnab_dict["cpf"]
        cnab.card=cnab_dict["card"]
        cnab.hour=cnab_dict["hour"]
        cnab.store=Store.objects.get(name=cnab_dict["store_name"])
        
        cnab.save()

def save_store(owner, name):
    store = Store()
    store.owner = owner
    store.name = name
    store.save()

def is_store_saved(parsed_cnab_dict_list):
    for cnab_dict in parsed_cnab_dict_list:
        store = Store.objects.filter(name=cnab_dict["store_name"])
        if not store:
            save_store(
                cnab_dict["store_owner"],
                cnab_dict["store_name"]
            )

def list_cnabs_by_store(stores, cnabs):
    cnabs_by_store = dict()

    for store in stores:
        cnabs_by_store[store.name] = {
            "total": store.calculate_total(),
            "transactions": []
        }

        for cnab in cnabs:
            if cnab.store.name == store.name:
                cnabs_by_store[store.name]["transactions"].append({
                    "type": cnab.type.description,
                    "date": cnab.date,
                    "value": cnab.value,
                    "cpf": cnab.cpf,
                    "card": cnab.card,
                    "hour": cnab.hour
                })

    return cnabs_by_store