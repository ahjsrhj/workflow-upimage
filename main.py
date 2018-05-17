# -*- coding: utf-8 -*-
import sys
import os
from workflow import Workflow3
import leancloud
import util

log = None


def get_file_and_upload(wf):
    from clipboard import get_paste_img_file
    from upload import upload_smms
    import time
    import util
    import shutil

    result = get_paste_img_file()
    if result != None and len(result) == 3:
        img_file, need_format, format = result
        # 处理图片
        print(img_file.name)
        upload_name = "%s.%s" % (int(time.time() * 1000), format)
        tmp_file = util.try_compress_png(img_file, format)
        upload_file_path = "/tmp/%s" % upload_name
        shutil.copy(tmp_file.name, upload_file_path)
        url, delete = upload_smms(upload_file_path, upload_name)
        leancloud.save_url(url, delete, wf)
        os.remove(upload_file_path)
        return url, upload_name
    else:
        # 没有图片
        # print('剪贴板内没有图片')
        return None, None


def get_img_list(wf):
    app_id = wf.stored_data('app_id')
    if app_id:
        # wf.add_item(title='jifdjsi', subtitle='jifdsji')
        # wf.send_feedback()
        img_list = leancloud.get_list(wf)
        if len(img_list) > 0:
            for img in img_list:
                url = img[u'url']
                delete = img[u'delete']
                arg = u"url:%s delete:%s" % (url, delete)
                created_at = util.get_time(img[u'createdAt'])
                wf.add_item(
                    url,              # title
                    # subtitle
                    u'创建时间:%s' % created_at,
                    arg=arg,
                    quicklookurl=url,
                    valid=True
                )

        else:
            wf.add_item(title='什么都没查到奥',
                        subtitle='设置app_id与app_key之后才开始记录上传列表')
        wf.send_feedback()
        pass
    else:
        wf.add_item(title='鉴权失败,请先设置Leancloud的App_id,app_key再进行使用',
                    subtitle='回车进行设置', arg='set:', valid=True)
        wf.send_feedback()


def set_appid_appkey(wf, str):
    strs = str.split()
    if len(strs) > 1:
        app_id, app_key = strs
        log.debug(app_id)
        log.debug(app_key)
        wf.store_data('app_id', app_id)
        wf.store_data('app_key', app_key)
        print('保存成功')
    else:
        print('保存失败!格式不正确')


def delete_url(wf, delete):
    img_list = leancloud.get_delete_list(wf, delete)
    if len(img_list) > 0:
        object_id = img_list[0]['objectId']
        leancloud.delete_url(wf, object_id, delete)
        print('删除成功')


def main(wf):
    args = wf.args[0]
    log.debug(args)
    if args == 'up':
        # 上传
        url, upload_name = get_file_and_upload(wf)
        if url != None:
            print("![%s](%s)" % (upload_name, url))
        else:
            print('err:剪贴板内没有图片，请先复制要上传的图片')
    elif args == 'upnormal':
        url, upload_name = get_file_and_upload(wf)
        if url != None:
            print(url)
        else:
            print('err:剪贴板内没有图片，请先复制要上传的图片')
    elif args == 'list':
        # 查看列表
        get_img_list(wf)
    elif args[0:4] == 'set:':
        if args[-1] == ';':
            wf.add_item(title='请按回车设置',
                        subtitle='输入app_id app_key,以空格隔开', arg="save:%s" % args[4:-1], valid=True)
        else:
            wf.add_item(title='输入app_id app_key,以空格隔开',
                        subtitle='输入完成后请输入分号(;)')
        wf.send_feedback()
    elif args[0:5] == 'save:':
        # 保存appid, appkey
        set_appid_appkey(wf, args[5:])
    elif args[0:7] == 'delete:':
        delete = args[7:]
        delete_url(wf, delete)


if __name__ == '__main__':
    wf = Workflow3()
    log = wf.logger
    sys.exit(wf.run(main))
