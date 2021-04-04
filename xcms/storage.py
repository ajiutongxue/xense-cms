from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

from django.conf import settings

import uuid


class ImageStorage(FileSystemStorage):
    def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
        # init
        super(ImageStorage, self).__init__(location, base_url)

    # 重写 save
    def _save(self, name, content):
        # name 为上传文件名称
        import os
        # 扩展名
        ext = '.' + name.split('.')[-1]
        dir_name = os.path.dirname(name)
        name = os.path.join(dir_name, str(uuid.uuid1()) + ext)
        # 调用父类方法
        return super(ImageStorage, self)._save(name, content)
