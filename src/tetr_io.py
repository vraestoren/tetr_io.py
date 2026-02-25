from requests import Session

class TetrIo:
    def __init__(self) -> None:
        self.api = " https://ch.tetr.io/api"
        self.session = Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
        }

    def get_server_statistics(self) -> dict:
        return self.session.get(f"{self.api}/general/stats").json()

    def get_server_activity(self) -> dict:
        return self.session.get(f"{self.api}/general/activity").json()

    def get_user_info(self, username: str) -> dict:
        return self.session.get(f"{self.api}/users/{username}").json()

    def get_user_records(self, username: str) -> dict:
        return self.session.get( f"{self.api}/users/{username}/records").json()

    def get_league_leaderboard(
            self,
            after: int = 25000,
            before: int = None,
            limit: int = 50,
            country: str = "US") -> dict:
        params = {
            key: value for key, value in {"after": after, "before": before}.items() if value is not None}
        return self.session.get(
            f"{self.api}/users/lists/league?limit={limit}&country={country}",
            params=params).json()

    def get_league_leaderboard_full(
            self,
            country: str = "US") -> dict:
        return self.session.get(
            f"{self.api}/users/lists/league/all?country={country}").json()

    def get_xp_leaderboard(
            self,
            after: int = 25000,
            before: int = None,
            limit: int = 50,
            country: str = "US") -> dict:
        params = {
            key: value for key, value in {"after": after, "before": before}.items() if value is not None}
        return self.session.get(
            f"{self.api}/users/lists/xp?limit={limit}&country={country}",
            params=params).json()

    def get_stream_info(self, stream: str) -> dict:
        return self.session.get(f"{self.api}/steams/{stream}").json()

    def get_latest_news(self, limit: int = 25) -> dict:
        return self.session.get(f"{self.api}/news?limit={limit}").json()

    def get_stream_latest_news(self, stream: str, limit: int = 25) -> dict:
        return self.session.get(
            f"{self.api}/news/{stream}?limit={limit}").json()
