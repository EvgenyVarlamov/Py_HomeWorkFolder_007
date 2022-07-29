def format_str(nam, sur, phn, dsn, stat):
    if stat == 'write_1':
        return f'{nam}; {sur}; {phn}; {dsn}'
    elif stat == 'write_4':
        return f'{nam}\n\n{sur}\n\n{phn}\n\n{dsn}'
