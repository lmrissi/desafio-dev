import datetime

def parse_cnab_file (cnab_file):
    date_format = '%Y%m%d'
    cnab_dict_list = []
    
    for line in cnab_file:
        cnab_dict = dict(
        type = '',
        date = '',
        value = '',
        cpf = '',
        card = '',
        hour = '',
        store_owner = '',
        store_name = '',
    )
        cnab_dict['type'] = int(line[0:1].decode("utf-8"))
        cnab_dict['date'] = datetime.datetime.strptime(line[1:9].decode("utf-8"), date_format).date()
        cnab_dict['value'] = round(float(int(line[9:19].decode("utf-8"))/100),2)
        cnab_dict['cpf'] = line[19:30].decode("utf-8") 
        cnab_dict['card'] = line[30:42].decode("utf-8") 
        cnab_dict['hour'] = datetime.time(
            int(line[42:44].decode("utf-8")),
            int(line[44:46].decode("utf-8")),
            int(line[46:48].decode("utf-8"))
        )
        cnab_dict['store_owner'] = line[48:62].decode("utf-8") 
        cnab_dict['store_name'] = line[62:81].strip().decode("utf-8")
        cnab_dict_list.append(cnab_dict)

    return cnab_dict_list
    
