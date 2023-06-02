import os
import random
import pytest
from griptape.artifacts import TextArtifact, ErrorArtifact


class TestPdfReader:
    @pytest.fixture
    def pdf_reader(self):
        from griptape.labs.tools import PdfReader

        return PdfReader()

    def test_read_pdf(self, pdf_reader):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "resources/bitcoin.pdf")
        artifact = pdf_reader.get_content({"values": {"path": path}})

        assert isinstance(artifact, TextArtifact)

        response = artifact.value

        assert response.startswith("Bitcoin: A Peer-to-Peer Electronic Cash System")

    def test_read_pdf_fails(self, pdf_reader):
        n = random.randint(0, 100)
        artifact = pdf_reader.get_content({"values": {"path": f"./this-will-never-exist-{n}.pdf"}})

        assert isinstance(artifact, ErrorArtifact)
