
def progress(current, total,args):
    print(f"{current * 100 / args:.1f}%")

def download_file(app,file_id,file_name,total):
    return app.download_media(file_id,file_name=file_name, block = True,progress=progress,progress_args =(total,))
