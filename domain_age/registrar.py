import re
from domain_age.constants import SERVER_NOT_FOUND, REGISTRAR_NOT_FOUND


def get_registrar(whois_record):
    try:
        if whois_record == SERVER_NOT_FOUND:
            return REGISTRAR_NOT_FOUND
        pattern = r"Registrar:"
        res = re.search(pattern, whois_record)
        if not res:
            return REGISTRAR_NOT_FOUND
        pattern = "[^\r\n]*"
        registrar = whois_record[res.end():]
        if registrar[1] == '\r' or registrar[1] == '\n':
            registrar = registrar[2:]
        # pdb.set_trace()
        res = re.search(pattern, registrar)
        if not res:
            return REGISTRAR_NOT_FOUND
        registrar = res[0].strip()
        return registrar
    except:
        return REGISTRAR_NOT_FOUND