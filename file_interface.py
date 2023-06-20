import os
import json
import base64
from glob import glob


class FileInterface:
    def __init__(self):
        os.chdir('files/')

    def list(self, params=[]):
        try:
            filelist = glob('*.*')
            return dict(status='OK', data=filelist)
        except Exception as e:
            return dict(status='ERROR', data=str(e))

    def get(self, params=[]):
        try:
            filename = params[0]
            if (filename == ''):
                return None
            fp = open(f"{filename}", 'rb')
            isifile = base64.b64encode(fp.read()).decode()
            return dict(status='OK', data_namafile=filename, data_file=isifile)
        except Exception as e:
            return dict(status='ERROR', data=str(e))
    
    # protokol upload file
    def add(self, params=[]) -> dict:
        try:
            if (len(params) != 2):
                raise Exception(
                    'Please provide correct params: <FILENAME> <CONTENT_FILE>')

            filename = params[0]
            if (filename == ''):
                raise Exception('Filename must not be empty')

            content_file = params[1]
            if (content_file == ''):
                raise Exception('Content file must not be empty')

            decoded_content = base64.b64decode(content_file)
            with open(filename, "wb") as f:
                f.write(decoded_content)

            return dict(status='OK', data=f"Name: {filename} Berhasil ditambahkan ke files/{filename}")
        except Exception as e:
            return dict(status='ERROR', data=str(e))

    # protokol hapus file
    def remove(self, params=[]) -> dict:
        try:
            if (len(params) != 1):
                raise Exception('Please provide correct params: <FILENAME>')

            filename = params[0]
            if (filename == ''):
                raise Exception('Filename must not be empty')

            if os.path.isfile(filename):
                os.remove(filename)
            else:
                raise Exception('File not found')

            return dict(status='OK', data=f"Name: {filename} Terhapus")
        except Exception as e:
            return dict(status='ERROR', data=str(e))


if __name__ == '__main__':
    file = open('normal_img.jpg', 'rb')
    cc = base64.b64encode(file.read())

    f = FileInterface()
    # print(f.list())
    # print(f.get(['pokijan.jpg']))
    print(f.upload(['normal_img.jpg', str(cc)]))