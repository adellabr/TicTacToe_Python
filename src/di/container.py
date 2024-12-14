from datasource.repository import GameStorage
from datasource.repository import GameRepository
from datasource.model import StorageModel

class Container:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Container, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        self.storage = GameStorage()
        self.repository = GameRepository(self.storage)
        
    def save(self, storage_model: StorageModel):
        self.repository.save(storage_model)
        
    def get(self, game_id):
        return self.repository.get(game_id)