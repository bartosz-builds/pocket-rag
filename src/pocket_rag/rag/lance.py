# Connect to LanceDB local volume
import lancedb

from pocket_rag.config.config import DB_DIR

db = lancedb.connect(DB_DIR)
