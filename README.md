# workflow-upimage
>  将复制的图片上传到图床并自动复制markdown链接的workflow~ 可配合leancloud使用，管理上传记录。

## 下载地址: [release](https://github.com/ahjsrhj/workflow-upimage/releases)

## 使用方式

- `imgup`:首先复制一张图片，或者按住ctrl截图，之后使用`imgup`上传图片，完成后会有通知发出并自动复制markdown链接到剪贴板，按下ctrl+回车复制正常的链接。

  ![1526554826889.gif](https://i.loli.net/2018/05/17/5afd60e776c4a.gif)

- `imglist`:使用之前需要前往leancloud创建一个项目，并且需要新建一个`class`，名为：`image`，之后获取`app_key`与`app_id`，获取到后运行该命令，直接敲回车，将`app_key`，`app_id`填入，格式为`app_key app_id;`，按回车设置，设置成功后之后每次上传图片都会将图片`url`与图片的`deleteUrl`保存到leancloud中，通过`imglist`命令查看管理已经上传的图片列表。在列表内的操作如下:

  - Enter: 复制图片链接到剪贴板。
  - Cmmmand + Enter: 调用delete链接，删除图片，同时在列表内移除这条链接。（图片被删除之后有一段时间的缓存期，约一两分钟后生效）
  - Ctrl + Enter: 在浏览器内打开图片链接。
  - Option + Enter: 复制markdown链接到剪贴板

  ![](https://s19.aconvert.com/convert/p3r68-cdx67/mk0ch-6qfya.gif)

图床使用的是[sm.ms](https://sm.ms), api 地址[https://sm.ms/doc/](https://sm.ms/doc/)

部分代码来自以下项目:

- [**alfred-workflow**](https://github.com/deanishe/alfred-workflow)
- [**markdown-img-upload**](https://github.com/tiann/markdown-img-upload)
