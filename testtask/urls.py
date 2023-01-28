import pathlib
from http.client import HTTPException

import pandas as pd
import dropbox
from dropbox.exceptions import AuthError
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
import requests

api = NinjaAPI()
dbx = dropbox.Dropbox("lj6mb7683g6992q")

headers = {
    "Authorization": "Bearer sl.BXs9Zzz5OIRND4kELhSQzr8Ro_zDDqchjQLrXECwATm2BLK2kbt1gCRNl5YyBkenOw7KD-DhK2TqW_5KvL2GaL-o4ERcdk8e7bLiajg54wuQO83tK7_S_jg04piq4Lw6Wgops6o",
    'Content-Type': 'application/json'
}


@api.get("/file/{key}")
def get_file(key: str):
    try:
        dbx = dropbox.Dropbox('lj6mb7683g6992q')
        file = dbx.files_download(key)
        return file.content
    except dropbox.exceptions.ApiError as e:
        raise HTTPException(status_code=400, detail="Failed to retrieve file.")


@api.put("/file/{key}")
def update_file(key: str, new_content):
    try:
        dbx = dropbox.Dropbox("lj6mb7683g6992q")
        file = dbx.files_upload(new_content, key)
        return {"message": "File updated successfully"}
    except dropbox.exceptions.ApiError as e:
        raise HTTPException(status_code=400, detail="Failed to update file.")




urlpatterns = [path("admin/", admin.site.urls), path("", api.urls)]
