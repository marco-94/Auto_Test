# -*- coding: utf-8 -*-
"""
author:Shanchi Liang
"""
import os
import time
import unittest
import random
from selenium import webdriver
from dateutil.parser import parse
from BeautifulReport import BeautifulReport
from selenium.webdriver.chrome.options import Options


class Test(unittest.TestCase):
    def save_img(self, img_name):
        self.browser \
            .get_screenshot_as_file('{}/{}.png'
                                    .format(os.path.abspath("D:/test/Auto_Test/img"), img_name))

    def setUp(self):
        self.browser = webdriver.Chrome()
        # self.chrome_options = Options()
        # # 禁止图片加载
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # self.chrome_options.add_experimental_option("prefs", prefs)
        # # 设置chrome浏览器无界面模式
        # self.chrome_options.add_argument('--headless')
        # self.browser = webdriver.Chrome(options=self.chrome_options)
        self.browser.set_window_size(1920, 1080)
        self.browser.get("https://weixin.sogou.com/")
        time.sleep(3)

    def tearDown(self):
        self.browser.quit()

    @BeautifulReport.add_test_img('滚动到底部')
    def test_scroll_to_the_bottom(self):
        u"""滚动到底部"""
        self.browser.execute_script("var action=document.documentElement.scrollTop=10000")
        time.sleep(1)
        self.save_img('滚动到底部')

    @BeautifulReport.add_test_img('查看更多')
    def test_look_more(self):
        u"""查看更多"""
        self.browser.find_element_by_xpath("//*[@id=\"look-more\"]/span").click()
        time.sleep(1)
        self.save_img('查看更多')

    @BeautifulReport.add_test_img('滚动到顶部')
    def test_scroll_to_the_top(self):
        u"""滚动到顶部"""
        # 拖动滚动条
        self.browser.execute_script("var action=document.documentElement.scrollTop=0")
        # 点击返回按钮返回顶部
        # self.browser.find_element_by_xpath("//*[@id=\"loginWrap\"]/div[8]/a")
        time.sleep(1)
        self.save_img('滚动到顶部')

    @BeautifulReport.add_test_img('翻页')
    def test_select_page(self):
        u"""翻页"""
        self.browser.find_element_by_xpath("//*[@id=\"query\"]").send_keys("微信")
        self.browser.find_element_by_xpath("//*[@id=\"searchForm\"]/div/input[3]").click()
        time.sleep(2)
        for i in range(0, 10):
            total = len(self.browser.find_elements_by_xpath("//*[@id=\"pagebar_container\"]/descendant::a"))
            j = random.randint(0, total-1)
            self.browser.execute_script("var action=document.documentElement.scrollTop=10000")
            time.sleep(1)
            self.save_img('翻页')
            self.browser.find_elements_by_xpath("//*[@id=\"pagebar_container\"]/descendant::a")[j].click()
            time.sleep(1)


if __name__ == '__main__':
    unittest.main()
