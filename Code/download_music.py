import os
import time

from selenium import webdriver


class Web:
    # The web that can let us to download the music
    download_web = "https://www.y2meta.com/zh-tw/youtube-to-mp3/eqtGDY0llkI"
    user_name = os.getlogin()

    def __init__(self, file_name: str, music_url: str):
        """
        Please input the file name and music url.
        Args:
            file_name (str): Tha music file name
            music_url (str): Which music is user want to download
        """
        self.driver = webdriver.Chrome()
        self.music_url = music_url
        self.file_name = file_name

    def open_download_page(self):
        self.driver.get(self.download_web)
        time.sleep(2)

    def key_in_music_url(self):
        keyin_field = self.driver.find_element(
            "xpath", "//*[@id=\"txt-url\"]")
        keyin_field.send_keys(self.music_url)
        time.sleep(5)

    def get_download_link(self):
        get_link_button = self.driver.find_element(
            "xpath", "//*[@id=\"process_mp3\"]")
        get_link_button.click()
        time.sleep(5)

    def start_download(self):
        download_button = self.driver.find_element(
            "xpath", "//*[@id=\"process-result\"]/div/a[1]")
        download_button.click()
        time.sleep(10)

    def rename_filename(self):
        # Sort based by time, and save these info to temp.txt
        os.system(f"dir C:\\Users\\{self.user_name}\\Downloads /b /o-d /tw > temp.txt")
        # Open file and read the first line
        file = open("temp.txt")
        current_name = file.readline().strip("\n")
        file.close()
        # Remove the temp.txt
        os.system("del temp.txt")
        file_path = f'C:\\Users\\{self.user_name}\\Downloads\\"{current_name}"'
        rename_command = f"ren {file_path} {self.file_name}.mp3"
        os.system(rename_command)

    def main(self):
        self.open_download_page()
        self.key_in_music_url()
        self.get_download_link()
        self.start_download()
        self.rename_filename()


Downloader = Web("Example", "https://www.youtube.com/watch?v=tZKFGmks6hA")
Downloader.main()
