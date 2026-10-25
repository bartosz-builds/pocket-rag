import sys

from watchdog.observers.polling import PollingObserver

from pocket_rag.config.config import INBOX_DIR
from pocket_rag.file.factory import FileHandlerFactory
from pocket_rag.file.handler import PDFFileHandler, URLHandler
from pocket_rag.file.watcher import FileWatcher
from pocket_rag.models.vectorizer import LLAMAProcessor
from pocket_rag.rag.repository import LanceDBAdapter
from pocket_rag.server.controller import MCPController


def main():
    print("Starting PDF watcher...", file=sys.stderr)
    print(f"[*] Watching {INBOX_DIR} for new PDFs...", file=sys.stderr)
    embedding_processor = LLAMAProcessor()
    repository = LanceDBAdapter(embedding_processor)
    pdf_file_handler = PDFFileHandler(repository)
    url_handler = URLHandler(repository)

    file_handler = FileHandlerFactory(pdf_file_handler, url_handler)
    event_handler = FileWatcher(file_handler)
    observer = PollingObserver()
    observer.schedule(event_handler, INBOX_DIR, recursive=True)
    observer.start()

    mcp_controller = MCPController(pdf_file_handler, repository)
    mcp_controller.start()
