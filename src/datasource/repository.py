import threading
from datasource.model import StorageModel

class GameStorage:
    def __init__(self):
        self.games = {}
    
class GameRepository:
    def __init__(self, storage: GameStorage):
        self.storage = storage
        self.lock = threading.Lock()
        
        
    def save(self, storage_model: StorageModel):
         with self.lock:
            self.storage.games[storage_model.uuid] = storage_model
            
            
    def get(self, game_id):
        with self.lock:
            return self.storage.games.get(game_id)