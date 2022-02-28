import tg_define as define
import tg_func as tf
import datetime

app = define.app

def parse_search_res(res):
    res_count = len(res)
    if res_count == 0 :return (None,None)
    res.sort(key=lambda x:x[x.media].date,reverse=True)
    file_list = []
    res_str = "---< 查询到{}个文件: >---\n".format(res_count)
    index = 1
    for msg in res:
        file_size_str = str((msg[msg.media].file_size)/(1024*1024))
        file_size_str = file_size_str[:file_size_str.rfind(".")+3]
        item = {
            "filename":msg[msg.media].file_name,
            "fileId":msg[msg.media].file_id,
            "fileSize":file_size_str,
            "date":str(datetime.datetime.fromtimestamp(msg[msg.media].date)),
        }
        file_list.append(item)
        res_str += "   {}. [{}] {}Mb {}\n".format(index,item["filename"],item["fileSize"],item["date"])
        index += 1
    res_str += "   0. 返回\n"
    res_str += "---< 输入序号开始下载: >---"
    return file_list,res_str

while True:
    print("---< keyword: ")
    keyword = input()
    if keyword == ":q":break
    else:
        res = app.search_messages(define.SEARCH_CHAT_ID,query =keyword,filter="document")
        file_list,res_str = parse_search_res(res)
        if file_list:
            print(res_str)
            while True:
                try:
                    select_number = int(input()) - 1
                    if select_number < 0: break
                    else:
                        file = file_list[select_number]
                        print("---< 开始下载 {} >---".format(file["filename"]))
                        while True:
                            res = tf.download_file(app,file["fileId"],"dl/" + file["filename"])
                            if res:
                                print("---< 文件已下载到 {} >---".format(res))
                                break
                            else:
                                print("---< 文件下载失败,重试? y/n")
                                res = input()
                                if res == "y": continue
                                else: break
                        break
                except:
                    print("输入数字")
        else:
            print("---< '" + keyword + "' 相关文件未找到 >---")
