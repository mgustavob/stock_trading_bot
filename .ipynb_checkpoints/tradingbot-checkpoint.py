{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium import webdriver"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime, re, requests, io, time, random, string"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "from credentials import email, password"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "driver = webdriver.Chrome('/Users/nataliiadusanovska/Downloads/chromedriver')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "driver.get('https://wallmine.com')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "martin.briceno@live.com\n"
     ]
    }
   ],
   "source": [
    "print(email)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Going to sign in page\n"
     ]
    }
   ],
   "source": [
    "sign_in_link = driver.find_element_by_xpath('/html/body/main/header/div/ul/li[1]/ul/li[3]/a')\n",
    "sign_in_link.click()\n",
    "time.sleep(3)\n",
    "print('Going to sign in page')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "login_email = driver.find_element_by_xpath('//*[@id=\"user_email\"]')\n",
    "sign_in_password = driver.find_element_by_xpath('//*[@id=\"new_user\"]/div[5]/div[1]/div[2]')\n",
    "sign_in_password.click()\n",
    "time.sleep(0.2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "login_password = driver.find_element_by_xpath('//*[@id=\"user_password\"]')\n",
    "sign_in_button = driver.find_element_by_xpath('//*[@id=\"new_user\"]/div[5]/div[2]/div[1]/button')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "login_email.send_keys(email)\n",
    "login_password.send_keys(password)\n",
    "sign_in_button.click()\n",
    "time.sleep(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "On the right Page\n"
     ]
    }
   ],
   "source": [
    "if \"Stock market overview\" in driver.page_source:\n",
    "    print('On the right Page')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [],
   "source": [
    "heatmap = driver.find_element_by_xpath('//*[@id=\"homepage-heatmap\"]/a/div[2]')\n",
    "heatmap.click()\n",
    "time.sleep(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [],
   "source": [
    "overview_tab = driver.find_element_by_xpath('/html/body/main/section/div[5]/div/div/div[1]/div/ul/li[1]/a')\n",
    "overview_tab.click()\n",
    "time.sleep(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
