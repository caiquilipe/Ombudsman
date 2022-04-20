from enum import Enum

class ManifestationStatus(Enum):
    COMPLAINT = (1, 'Reclamação')
    SUGGESTION = (2, 'Segestão')
    PRAISE = (3, 'Elogio')
    
manifestation_accept_status = {
    ManifestationStatus.COMPLAINT.value[0]: ManifestationStatus.COMPLAINT.value[1],
    ManifestationStatus.SUGGESTION.value[0]: ManifestationStatus.SUGGESTION.value[1],
    ManifestationStatus.PRAISE.value[0]: ManifestationStatus.PRAISE.value[1],
}

class Manifestation:
    def __init__(self, id, description, status, name):
        self.id = id
        self.description = description
        self.status = manifestation_accept_status[status]
        self.name = name

    def __str__(self) -> str:
        return f'{self.id}-{self.status}-{self.name}-{self.description}'