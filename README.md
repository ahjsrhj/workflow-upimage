# workflow-upimage
将复制的图片上传到图床并自动复制markdown链接的workflow~

图床使用的是[sm.ms](https://sm.ms), api 地址[https://sm.ms/doc/](https://sm.ms/doc/)

可以配合leancloud使用，将上传图片的历史记录存储到leancloud，此功能需要先去leancloud创建一个项目，将app_id与app_key填入workflow

使用命令 `imglist` 进行app_id与app_key的初始化工作

部分代码来自以下项目:

- [**alfred-workflow**](https://github.com/deanishe/alfred-workflow)
- [**markdown-img-upload**](https://github.com/tiann/markdown-img-upload)