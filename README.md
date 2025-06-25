# A simple mood tracking desktop app ![Python](https://img.shields.io/badge/python-3.12.10-yellow?logo=python&logoColor=white)
Log how you feel each day (on a scale from 1 to 10), and view a colorful summary of your mood history.

## Requirements
* [Python](https://python.org) 3.8+
* [Pillow](https://pypi.org/project/pillow/)
* tkinter (comes with Python)

Install the required libraries with:
```bash
pip install -r requirements.txt
```

## How to use
### Option 1:
1. Just download:
   * [mood_logger.exe](https://github.com/KajetanFilipMigdalski/MoodLogger/blob/main/dist/mood_logger.exe) 
   * [mood_summary.exe](https://github.com/KajetanFilipMigdalski/MoodLogger/blob/main/dist/mood_summary.exe)
2. Add the ```file mood_logger.exe``` to  ```C:\Users\<YourUsername>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup```

The mood logs will be saved automatically to:
```C:\Users\YourName\mood_logger\mood_log.json```
### Option 2:
1. Download the source (Python):
```bash
git clone https://github.com/KajetanFilipMigdalski/MoodLogger.git
cd MoodLogger
pip install -r requirements.txt
```
2. Run the python files:
```bash
python mood_logger.py  # for logging
python mood_summary.py # for summary
```

