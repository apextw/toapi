from .DBStore import DBStore
from .DiskStore import DiskStore


class Storage:
    """
    transfer DBStore and DiskStore functions
    about param settings:
    settings = {
        "PATH": "/User/ToApi,
        "DB_URL": None
    }
    PATH: the path of local file stores, default path is current running file path
    DB_URL: store url source in db, ignoring local store if this param give
    """

    def __init__(self, settings):

        self.path = settings.storage_config.get("PATH")
        if not self.path:
            self.path = "./"
        self.db_url = settings.storage_config.get("DB_URL")

        self.disk_store = DiskStore(self.path)
        self.db_store = DBStore(self.db_url) if self.db_url else None

    def save(self, url, html):

        if not self.db_store:
            return self.disk_store.save(url, html)
        return self.db_store.save(url, html)

    def get(self, url, expiration="inf"):

        if not self.db_store:
            return self.disk_store.get(url, expiration)
        return self.db_store.get(url, expiration)
