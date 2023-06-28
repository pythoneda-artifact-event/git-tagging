"""
pythonedaartifacteventgittagging/tag_credentials_provided.py

This file declares the TagCredentialsProvided event.

Copyright (C) 2023-today rydnr's pythoneda-artifact-event/git-tagging

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from pythoneda.event import Event
from pythoneda.value_object import attribute, primary_key_attribute, sensitive


class TagCredentialsProvided(Event):
    """
    Represents the response to a request for credentials required for tagging a repository.

    Class name: TagRequested

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - TagCredentialsRequested: The event requesting the credentials for tagging.
    """

    def __init__(self, requestId: str, repositoryUrl: str, branch: str, sshUsername: str, privateKeyFile: str, privateKeyPassphrase: str):
        """
        Creates a new TagCredentialsProvided instance.
        :param requestId: The id of the event requesting the credentials.
        :type requestId: str
        :param repositoryUrl: The url of the repository.
        :type repositoryUrl: str
        :param branch: The branch.
        :type branch: str
        :param sshUsername: The SSH username.
        :type sshUsername: str
        :param privateKeyFile: The file with the private key.
        :type privateKeyFile: str
        :param privateKeyPassphrase: The passphrase of the private key.
        :type privateKeyPassphrase: str
        """
        super().__init__()
        self._request_id = requestId
        self._repository_url = repositoryUrl
        self._branch = branch
        self._ssh_username = sshUsername
        self._private_key_file = privateKeyFile
        self._private_key_passphrase = privateKeyPassphrase

    @property
    @primary_key_attribute
    def request_id(self) -> str:
        """
        Retrieves the id of the event requesting the credentials for tagging.
        :return: Such id.
        :rtype: str
        """
        return self._request_id

    @property
    @attribute
    def repository_url(self) -> str:
        """
        Retrieves the url of the repository to tag.
        :return: Such url.
        :rtype: str
        """
        return self._repository_url

    @property
    @attribute
    def branch(self) -> str:
        """
        Retrieves the branch of the repository to tag.
        :return: Such name.
        :rtype: str
        """
        return self._branch

    @property
    @attribute
    def ssh_username(self) -> str:
        """
        Retrieves the ssh username.
        :return: Such name.
        :rtype: str
        """
        return self._ssh_username

    @property
    @attribute
    @sensitive
    def private_key_file(self) -> str:
        """
        Retrieves the file with the private key.
        :return: Such path.
        :rtype: str
        """
        return self._private_key_file

    @property
    @attribute
    @sensitive
    def private_key_passphrase(self) -> str:
        """
        Retrieves the passphrase of the private key.
        :return: Such passphrase.
        :rtype: str
        """
        return self._private_key_passphrase
