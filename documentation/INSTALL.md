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
- `turtle` - Built-in with Python ✓
- `pygame` - Optional, for Mac/Linux sound support
  - **Note**: Pygame pre-built wheels not yet available for Python 3.14
  - Game works perfectly without it - will use system sound fallback

## Python Version Support

| Python Version | Status | Sound Method |
|---|---|---|
| 3.11-3.13 | ✅ Full support | pygame (Mac/Linux) or winsound (Windows) |
| 3.14+ | ✅ Supported | winsound (Windows) or silent (other OS) |

**Note for Python 3.14 users**: The game works great! Pygame isn't available yet for this version, but your installation will automatically use the available fallback sound system (winsound on Windows, or silent mode if unavailable).

## Resolving "pygame is not satisfied" Error

If you see a pip error about pygame not being satisfied:

1. **On Python 3.14**: This is expected - pygame wheels aren't ready yet. Your game will still run!
   - No action needed - the game has built-in fallbacks
   
2. **On Python 3.13 or earlier**: Try installing pygame:
   ```bash
   pip install pygame>=2.5.2
   ```
   
   Or use the pre-release version:
   ```bash
   pip install pygame --pre
   ```

