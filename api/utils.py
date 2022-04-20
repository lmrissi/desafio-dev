def parse_cnab_file (cnab_file):
    dict_list = []
    dict = dict(
        type = '',
        date = '',
        value = '',
        cpf = '',
        card = '',
        hour = '',
        store_owner = '',
        store_name = '',
    )

    for line in cnab_file:
        dict['type'] = line[0:1]
        dict['date'] = line[1:2]
        dict['value'] = line[11:20]
        dict['cpf'] = line[21:31]
        dict['card'] = line[32:43]
        dict['hour'] = line[44:49]
        dict['store_owner'] = line[50:63]
        dict['store_name'] = line[64:82]
        dict_list.append(dict)

    return dict_list
    
