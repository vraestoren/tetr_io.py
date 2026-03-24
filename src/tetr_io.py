from requests import Session

class TetrIo:
    def __init__(self) -> None:
        self.api = "https://ch.tetr.io/api"
        self.session = Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
        }

    def _get(self, endpoint: str, params: dict = None) -> dict:
        return self.session.get(
            f"{self.api}{endpoint}", params=params).json()

    def _filter(self, data: dict) -> dict:
        return {key: value for key, value in data.items() if value is not None}

    def get_server_statistics(self) -> dict:
        return self._get("/general/stats")

    def get_server_activity(self) -> dict:
        return self._get("/general/activity")

    def get_user_info(self, username: str) -> dict:
        return self._get(f"/users/{username}")

    def get_user_records(self, username: str) -> dict:
        return self._get(f"/users/{username}/records")

    def get_league_leaderboard(
            self,
            after: int = 25000,
            before: int = None,
            limit: int = 50,
            country: str = "US") -> dict:
        params = self._filter({
            "after": after,
            "before": before,
            "limit": limit,
            "country": country
        })
        return self._get("/users/lists/league", params)

    def get_league_leaderboard_full(
            self, country: str = "US") -> dict:
        return self._get(f"/users/lists/league/all?country={country}")

    def get_xp_leaderboard(
            self,
            after: int = 25000,
            before: int = None,
            limit: int = 50,
            country: str = "US") -> dict:
        params = self._filter({
            "after": after,
            "before": before,
            "limit": limit,
            "country": country
        })
        return self._get("/users/lists/xp", params)

    def get_stream_info(self, stream: str) -> dict:
        return self._get(f"/streams/{stream}")

    def get_latest_news(self, limit: int = 25) -> dict:
        return self._get(f"/news?limit={limit}")

    def get_stream_latest_news(
            self, stream: str, limit: int = 25) -> dict:
        return self._get(f"/news/{stream}?limit={limit}")
