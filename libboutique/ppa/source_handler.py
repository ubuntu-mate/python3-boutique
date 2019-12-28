import shutil
import re


class SourceHandler:
    """
        It takes care of the operations related to adding/removing
        external sources.

        This includes: ppa and custom urls
    """
    LAUNCHPAD_URL = "http://ppa.launchpad.net/{user}/{project}/ubuntu"
    SOURCE_LIST_PATH = "/etc/apt/sources.list"
    SOURCE_LIST_BACKUP_PATH  = "/etc/apt/sources.list.back"

    def __init__(self):
        pass
    
    def _backup_source_file(self) -> None:
        """
            Back the source.list file in case
            we need to do a rollback
        """
        shutil.copyfile(src=self.SOURCE_LIST_PATH, dst=self.SOURCE_LIST_BACKUP_PATH)