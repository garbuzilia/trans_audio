import os
from faster_whisper import WhisperModel
from pathlib import Path

# Пути
BASE_DIR = Path(__file__).parent
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"
MODELS_DIR = BASE_DIR / "models"

# Создаём папки, если нет
INPUT_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)
MODELS_DIR.mkdir(exist_ok=True)

# Имя модели (папка с model.bin внутри)
# Скачайте модель с https://huggingface.co/guillaumekln/faster-whisper-<размер>
# и положите в папку models/
MODEL_NAME = "faster-whisper-base"

# Путь к модели
model_path = MODELS_DIR / MODEL_NAME

if not model_path.exists():
    print(f"Модель не найдена в {model_path}")
    print(f"Скачайте модель с https://huggingface.co/guillaumekln/{MODEL_NAME}")
    print(f"Распакуйте в папку {MODELS_DIR}")
    exit(1)

# Загружаем модель из локальной папки
model = WhisperModel(str(model_path), device="cpu", compute_type="int8")

# Поддерживаемые расширения
AUDIO_EXTENSIONS = {".mp3", ".wav", ".m4a", ".mp4", ".ogg", ".flac"}

# Обрабатываем файлы
for file_path in INPUT_DIR.iterdir():
    if file_path.suffix.lower() in AUDIO_EXTENSIONS:
        print(f"Обрабатываю: {file_path.name}")

        # Распознавание
        segments, info = model.transcribe(str(file_path), language="ru")
        text = "".join([segment.text for segment in segments])

        # Сохраняем текст
        output_file = OUTPUT_DIR / f"{file_path.stem}.txt"
        with open(output_file, "w", encoding="cp1251", errors="replace") as f:
            f.write(text)

        print(f"Готово: {output_file.name}")

print("Все файлы обработаны.")
