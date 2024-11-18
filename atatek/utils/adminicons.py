import os
from werkzeug.utils import secure_filename
import uuid


def save_file(file, old_path=None):
    if not file:
        return old_path

    # Создаем уникальное имя файла
    filename = secure_filename(file.filename)
    ext = os.path.splitext(filename)[1]
    unique_filename = f"{uuid.uuid4()}{ext}"

    # Путь для сохранения
    save_path = os.path.join('atatek', 'static', 'images', 'icons', unique_filename)

    # Создаем директорию, если она не существует
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # Сохраняем файл
    file.save(save_path)

    # Если есть старый файл, удаляем его
    if old_path and os.path.exists(old_path):
        try:
            os.remove(old_path)
        except:
            pass  # Игнорируем ошибки при удалении старого файла

    return unique_filename