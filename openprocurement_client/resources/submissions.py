import logging

from openprocurement_client.clients import APIResourceClient
from openprocurement_client.constants import (DOCUMENTS, SUBMISSIONS)

LOGGER = logging.getLogger(__name__)


class SubmissionsClient(APIResourceClient):
    """Client for submissions"""

    resource = SUBMISSIONS

    def create_submission(self, submission):
        return self.create_resource_item(submission)

    def upload_submission_document(self, file, submission_id, use_ds_client=True,
                              doc_registration=True, access_token=None):
        return self.upload_document(file, submission_id,
                                    use_ds_client=use_ds_client,
                                    doc_registration=doc_registration,
                                    access_token=access_token)


