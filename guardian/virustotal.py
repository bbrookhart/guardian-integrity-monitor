<class VirusTotalClient:
    """
    Safe placeholder for VirusTotal integration.
    This module does NOT perform any scanning or remote lookups.
    It only simulates a lookup response for demo purposes.
    """

    def __init__(self, api_key=None):
        self.api_key = api_key

    def lookup_hash(self, file_hash):
        # Safe mock response
        return {
            "file_hash": file_hash,
            "found": False,
            "message": "VirusTotal lookup disabled in demo mode."
        }
>
