from selenium.webdriver.common.by import By

class loc(object):
    upload = (By.LINK_TEXT, "File Upload")
    file_up = (By.ID, "file-upload")
    submit= (By.ID, "file-submit")
    checker="File uploaded"