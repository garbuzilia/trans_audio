# transcribe_audio.py

Пакетное распознавание речи из аудио/видео на русском языке через локальную модель [faster-whisper](https://github.com/SYSTRAN/faster-whisper). Работает офлайн.

## Возможности

- Обработка всех файлов из `input/`
- Язык распознавания: русский
- Работа на CPU, без видеокарты
- Поддержка: `.mp3`, `.wav`, `.m4a`, `.mp4`, `.ogg`, `.flac`
- Результат — `.txt` в папке `output/`

## Структура
transcribe_audio/
├── transcribe_audio.py
├── input/ # аудиофайлы (создаётся автоматически)
├── output/ # результаты .txt (создаётся автоматически)
├── models/
  └── faster-whisper-base/ # модель (см. ниже)
  ├── model.bin
  ├── config.json
  ├── tokenizer.json
  └── vocabulary.txt
