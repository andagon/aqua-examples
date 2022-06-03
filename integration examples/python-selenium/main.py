#!/bin/sh
"exec" "`dirname $0`/.venv/bin/python" "$0" "$@"

import unittest
import geckodriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class PythonTestExample(unittest.TestCase):

    def setUp(self) -> None:
        geckodriver_autoinstaller.install()

        options = webdriver.FirefoxOptions()
        options.headless = True
        self.driver = webdriver.Firefox(options=options)

        return super().setUp()

    def test_search_in_python_org(self) -> None:
        self.driver.get("https://www.python.org")

        self.assertIn("Python", self.driver.title)

        elem = self.driver.find_element(By.NAME, "q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)

        self.assertNotIn("No results found.", self.driver.page_source)

        self.driver.save_screenshot("screenshots/page.png")

    def tearDown(self) -> None:
        self.driver.quit()

        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
