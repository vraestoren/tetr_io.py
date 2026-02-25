# tetr_io.py
Web-API for [tetr.io](https://tetr.io) website TETRA CHANNEL REST-API

## Example
```python
from tetr_io import TetrIo

tetr_io = TetrIo()
latest_news = tetr_io.get_latest_news()
print(latest_news)
```
