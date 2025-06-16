from typing import List, Dict, Any

class Document:
    def __init__(self, title: str, content: str, metadata: Dict[str, Any] = None):
        self.title = title
        self.content = content
        self.metadata = metadata if metadata is not None else {}

class Vector:
    def __init__(self, values: List[float]):
        self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, index: int) -> float:
        return self.values[index]