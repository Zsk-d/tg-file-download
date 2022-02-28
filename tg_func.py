def download_file(app,file_id,file_name):
    return app.download_media(file_id,file_name=file_name, block = True)
