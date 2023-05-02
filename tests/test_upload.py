from seleniumbase import BaseCase

class UploadTest(BaseCase):
    def test_visible_upload(self):
        # open the page
        self.open_url("https://the-internet.herokuapp.com/upload")
        # Get the file path
        file_path = './data/website.jpg'

        # upload file
        self.choose_file("input[id=file-upload]", file_path)
        # click the upload button
        self.click("input[id=file-submit]")
        # assert file uploaded text
        self.assert_text("File Uploaded!", "h3")




    def test_hidden_upload(self):
        self.open_url("https://practice.automationbro.com/cart/")
        file_path = './data/website.jpg'

        # add js code
        remove_hidden_class = "document.getElementById('upfile_1').classList.remove('file_input_hidden')"
        self.add_js_code(remove_hidden_class)
        self.choose_file("#upfile_1", file_path)
        # self.choose_file("input[type=file]", file_path)
        self.click("input[id=upload_1]")
        self.assert_text("File website.jpg uploaded successfully", ".file_messageblock_fileheader_label")