import operation
import ioport
import logger


def run():
    status = ''
    while status != 'exit':
        status = ioport.menu()
        if status == 'read_1' or status == 'read_4':
            output = logger.read_file(status)
            ioport.output_data(output)
        elif status == 'write_1' or  status == 'write_4':
            name = ioport.get_data('Введите фамилию: ')
            surname = ioport.get_data('Введите имя: ')
            phone_number = ioport.get_data('Введите номер телефона: ')
            description = ioport.get_data('Введите описание: ')
            record = operation.format_str(name, surname, phone_number, description, status)
            logger.log(record, status)
            ioport.output_data(record)