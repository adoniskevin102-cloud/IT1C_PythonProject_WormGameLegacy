# Worm Game - Installation Guide

## Quick Start

### Windows
Just run the game - Windows has built-in sound support!
```
python source/main.py
```

### Mac & Linux
Install dependencies first:
```bash
pip install -r requirements.txt
```

Then run the game:
```bash
python source/main.py
```

## Sound Support

- **Windows**: Uses native `winsound` module ✅ (no extra installation needed)
- **Mac & Linux**: Uses `pygame` for sound ✅ (requires `pip install pygame`)

## Troubleshooting

### If pygame won't install on Mac:
```bash
pip install pygame --pre
```

### If you get audio errors:
- The game will still work - sounds will just be skipped
- This is completely normal and doesn't affect gameplay

### If the background image isn't found:
- The game automatically uses a green background as fallback
- Place `worm_bg.png` in the same directory as `main.py` to use a custom background

## Dependencies
- `turtle` - Built-in with Python
- `pygame` - Optional, for Mac/Linux sound support

