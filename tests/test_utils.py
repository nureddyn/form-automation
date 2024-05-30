import unittest
from unittest.mock import patch, mock_open, MagicMock

from modules.utils import write_to_pdf


class TestWriteToPdf(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open)
    @patch('PyPDF2.PdfFileReader')
    @patch('PyPDF2.PdfFileWriter')
    def test_write_to_pdf(self, MockPdfFileWriter, MockPdfFileReader, mock_open):
        buffer = {'field1': 'value1', 'field2': 'value2'}
        template = MagicMock()
        template.path = "dummy_path"

        mock_reader = MockPdfFileReader.return_value
        mock_reader.numPages = 2
        mock_page = MagicMock()
        mock_reader.getPage.return_value = mock_page
        mock_reader.getFields.return_value = {
            'field1': {'/V': ''},
            'field2': {'/V': ''},
        }

        mock_writer = MockPdfFileWriter.return_value

    
        write_to_pdf(buffer, template)

        mock_open.assert_any_call(template.path, 'rb')
        mock_open.assert_any_call('output.pdf', 'wb')
        self.assertEqual(mock_open.call_count, 2)

        MockPdfFileReader.assert_called_once_with(mock_open.return_value)
        self.assertEqual(mock_reader.getPage.call_count, 2)
        self.assertEqual(mock_reader.getFields.call_count, 2)
        self.assertEqual(mock_writer.addPage.call_count, 2)

        for key in buffer:
            self.assertEqual(mock_reader.getFields.return_value[key]['/V'], buffer[key])

        mock_writer.write.assert_called_once_with(mock_open.return_value)


if __name__ == '__main__':
    unittest.main()
