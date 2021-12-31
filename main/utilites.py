from datetime import datetime
from os.path import splitext


# генерирующей  имена  сохраняемых  в  модели  выгруженных  файлов
def get_timestamp_path(instance, filename):
    return '%s%s' % (datetime.now().timestamp(), splitext(filename)[1])