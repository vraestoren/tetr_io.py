# <img src="https://tetr.io/res/logo.png" width="40" style="vertical-align:middle;" /> tetr_io.py

> Web-API for [tetr.io](https://tetr.io) website TETRA CHANNEL REST-API fetch server stats, player info, leaderboards, and news.

## Quick Start
```python
from tetr_io import TetrIo

tetr = TetrIo()

# Get latest news
print(tetr.get_latest_news())
```

---

## Server

| Method | Description |
|--------|-------------|
| `get_server_statistics()` | Get overall server statistics |
| `get_server_activity()` | Get server activity histogram |

---

## Users

| Method | Description |
|--------|-------------|
| `get_user_info(username)` | Get a player's public profile |
| `get_user_records(username)` | Get a player's personal records |
```python
tetr.get_user_info("tarikgd")
tetr.get_user_records("tarikgd")
```

---

## Leaderboards

| Method | Description |
|--------|-------------|
| `get_league_leaderboard(after, before, limit, country)` | Get TETRA LEAGUE rankings |
| `get_league_leaderboard_full(country)` | Get full TETRA LEAGUE ranking list |
| `get_xp_leaderboard(after, before, limit, country)` | Get XP-based rankings |
```python
# Top 50 US league players
tetr.get_league_leaderboard(limit=50, country="US")

# Full global league leaderboard
tetr.get_league_leaderboard_full()
```

---

## Streams

| Method | Description |
|--------|-------------|
| `get_stream_info(stream)` | Get records in a stream |
```python
tetr.get_stream_info("40l_global")
```

---

## News

| Method | Description |
|--------|-------------|
| `get_latest_news(limit)` | Get latest global news |
| `get_stream_latest_news(stream, limit)` | Get latest news for a stream |
```python
# Latest 25 global news items
tetr.get_latest_news(limit=25)

# News for a specific stream
tetr.get_stream_latest_news("user_tarikgd")
```
