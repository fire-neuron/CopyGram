import unittest
import Uploader
import os
import Initializer
import random

r_val = random.randint(0, 100)
put_file = Initializer.settings['FtpUploader']['folder_for_scan']
file_path = os.path.join(put_file, 'TestEsr.test')
file_get_path = os.path.join(put_file, 'TestEsrGet.test')


class test_uploadfile(unittest.TestCase):
    def setUp(self):
        with open(file_path, 'w') as self.file:
            self.file.write(str(r_val))
        Uploader.myFTP.set_debuglevel(0)
        Uploader.start()

    def tearDown(self):
        os.remove(file_path)
        os.remove(file_get_path)
        Uploader.myFTP.delete('TestEsr.test')

    def test_uploader(self):
        local_file = 'testEsrGet.test'
        ftp_file = 'TestEsr.test'  # Имя файла на сервере
        os.chdir(put_file)
        with open(local_file, 'wb') as local_file:
            Uploader.myFTP.retrbinary('retr ' + ftp_file, local_file.write)
        with open(file_get_path, 'r') as check:
            t = check.read()
        self.assertEqual(str(r_val), t)

