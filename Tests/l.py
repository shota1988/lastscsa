
from Steps.TEST import Main_Step
import unittest
import allure


class test_main(unittest.TestCase):
    @allure.description("check file uploading")
    @allure.severity(allure.severity_level.MINOR)

    def test_file_upload_action(self):
        Main_Step.setUp(self)
        Main_Step.open_upload_file(self)
        Main_Step.upload_file(self)
        Main_Step.submit_upload_file(self)
        self.assertTrue(Main_Step.checker(self))
        Main_Step.tearDown(self)

if __name__=="__main__":
    unittest.main()