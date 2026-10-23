import os
import sqlite3
import gzip
import shutil

class CryptoVault:
    def __init__(self, db_path="sentience_core_ledger.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("CREATE TABLE IF NOT EXISTS system_logs (id INTEGER PRIMARY KEY, msg TEXT)")

    def archive_ledger_transaction(self):
        # Compresses raw database to offline memory vault paths
        archive = f"archived_memories/backup_vault.db.gz"
        try:
            with open(self.db_path, 'rb') as f_in, gzip.open(archive, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        except IOError:
            pass
