#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unicodedata

from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.easports.com/fifa/ultimate-team/fut/database/results?position_secondary=LF,CF,RF,ST,LW,LM,CAM,CDM,CM,RM,RW,LWB,LB,CB,RB,RWB&quality=bronze,silver,gold,rare_bronze,rare_silver,rare_gold")

filename = "ealinks.csv"
file = open(filename, 'w')

line = ("name" + ',' + "full name" + ',' + "overall" + ',' + "club" + ',' + "league" + ',' + "nation" + ',' + "age" + ',' + "height" + ',' + "weight" + ',' + "foot" + ',' + "pac" + ','
                + "acceleration" + ',' + "sprint speed" + ',' + "dri" + ',' + "agility" + ',' + "balance" + ',' + "reactions" + ',' + "ball control" + ',' + "dribbling" + ',' + "composure" + ','
                + "sho" + ',' + "positioning" + ',' + "finishing" + ',' + "shot power" + ',' + "long_shots" + ',' + "volleys" + ',' + "penalties" + ',' + "defending" + ',' + "interceptions" + ','
                + "heading accuracy" + ',' + "marking" + ',' + "standing tackle" + ',' + "sliding tackle" + ',' + "pas" + ',' + "vision" + ',' + "crossing" + ',' + "free kick accuracy" + ','
                + "short passing" + ',' + "long passing" + ',' + "curve" + ',' + "phy" + ',' + "jumping" + ',' + "stamina" + ',' + "strength" + ',' + "aggression" + '\n')

file.write(line)

for i in range(200):
    sleep(10)
    show_more = driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[3]/div/div/ul[2]/li')
    show_more.click()
    print i

links_list = []
names_list = []
list_items = driver.find_elements_by_css_selector('li.ut-item-list-view_row')
for item in list_items:
    url = item.find_element_by_css_selector('a.ut-item-list-view_row-link').get_attribute('href')
    card = item.find_element_by_css_selector('span').text
    name = item.find_element_by_css_selector('h2').text.replace(card, '').strip()
    name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').lower()
    names_list.append(name)
    links_list.append(url)

i = 0
for link in links_list:
    try:
        driver.get(link)
        sleep(5)

        full_name = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div.ut-body-inner > div > div:nth-child(2) > div.ut-bio-details_headings > h2').text.strip()
        full_name = unicodedata.normalize('NFKD', full_name).encode('ascii', 'ignore').lower()

        overall = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div.ut-body-inner > div > div:nth-child(2) > div.ut-bio-details_stats.ut-grid-view > div:nth-child(1) > table > tbody > tr:nth-child(1) > td').text.strip()

        club = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div.ut-body-inner > div > div:nth-child(2) > div.ut-bio-details_stats.ut-grid-view > div:nth-child(1) > table > tbody > tr:nth-child(2) > td').text.strip()
        club = unicodedata.normalize('NFKD', club).encode('ascii', 'ignore').lower()

        league = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div.ut-body-inner > div > div:nth-child(2) > div.ut-bio-details_stats.ut-grid-view > div:nth-child(1) > table > tbody > tr:nth-child(3) > td').text.strip()
        league = unicodedata.normalize('NFKD', league).encode('ascii', 'ignore').lower()

        nation = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div.ut-body-inner > div > div:nth-child(2) > div.ut-bio-details_stats.ut-grid-view > div:nth-child(1) > table > tbody > tr:nth-child(4) > td').text.strip()
        nation = unicodedata.normalize('NFKD', nation).encode('ascii', 'ignore').lower()

        age = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div.ut-body-inner > div > div:nth-child(2) > div.ut-bio-details_stats.ut-grid-view > div:nth-child(2) > table > tbody > tr:nth-child(2) > td').text.strip()

        height = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div.ut-body-inner > div > div:nth-child(2) > div.ut-bio-details_stats.ut-grid-view > div:nth-child(2) > table > tbody > tr:nth-child(3) > td').text.strip()

        weight = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div.ut-body-inner > div > div:nth-child(2) > div.ut-bio-details_stats.ut-grid-view > div:nth-child(2) > table > tbody > tr:nth-child(4) > td').text.strip()

        foot = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div.ut-body-inner.ut-body-inner--fixed.ut-body-inner--pattern > div > div:nth-child(4) > table > tbody > tr:nth-child(1) > td').text.strip()
        foot = unicodedata.normalize('NFKD', foot).encode('ascii', 'ignore').lower()

        pac = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(1) > div.ut-bio-stats_header > h6 > span.ut-bio-stats_title-value').text.strip()
        acceleration = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(1) > div.ut-bio-stats_content > table > tbody > tr:nth-child(1) > td').text.strip()
        sprint_speed = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(1) > div.ut-bio-stats_content > table > tbody > tr:nth-child(2) > td').text.strip()

        dri = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(2) > div.ut-bio-stats_header > h6 > span.ut-bio-stats_title-value').text.strip()
        agility = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(2) > div.ut-bio-stats_content > table > tbody > tr:nth-child(1) > td').text.strip()
        balance = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(2) > div.ut-bio-stats_content > table > tbody > tr:nth-child(2) > td').text.strip()
        reactions = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(2) > div.ut-bio-stats_content > table > tbody > tr:nth-child(3) > td').text.strip()
        ball_control = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(2) > div.ut-bio-stats_content > table > tbody > tr:nth-child(4) > td').text.strip()
        dribbling = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(2) > div.ut-bio-stats_content > table > tbody > tr:nth-child(5) > td').text.strip()
        composure = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(2) > div.ut-bio-stats_content > table > tbody > tr:nth-child(6) > td').text.strip()

        sho = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(3) > div.ut-bio-stats_header > h6 > span.ut-bio-stats_title-value').text.strip()
        positioning = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(3) > div.ut-bio-stats_content > table > tbody > tr:nth-child(1) > td').text.strip()
        finishing = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(3) > div.ut-bio-stats_content > table > tbody > tr:nth-child(2) > td').text.strip()
        shot_power = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(3) > div.ut-bio-stats_content > table > tbody > tr:nth-child(3) > td').text.strip()
        long_shots = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(3) > div.ut-bio-stats_content > table > tbody > tr:nth-child(4) > td').text.strip()
        volleys = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(3) > div.ut-bio-stats_content > table > tbody > tr:nth-child(5) > td').text.strip()
        penalties = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(3) > div.ut-bio-stats_content > table > tbody > tr:nth-child(6) > td').text.strip()

        defending = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(4) > div.ut-bio-stats_header > h6 > span.ut-bio-stats_title-value').text.strip()
        interceptions = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(4) > div.ut-bio-stats_content > table > tbody > tr:nth-child(1) > td').text.strip()
        heading_accuracy = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(4) > div.ut-bio-stats_content > table > tbody > tr:nth-child(2) > td').text.strip()
        marking = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(4) > div.ut-bio-stats_content > table > tbody > tr:nth-child(3) > td').text.strip()
        standing_tackle = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(4) > div.ut-bio-stats_content > table > tbody > tr:nth-child(4) > td').text.strip()
        sliding_tackle = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(4) > div.ut-bio-stats_content > table > tbody > tr:nth-child(5) > td').text.strip()

        pas = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(5) > div.ut-bio-stats_header > h6 > span.ut-bio-stats_title-value').text.strip()
        vision = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(5) > div.ut-bio-stats_content > table > tbody > tr:nth-child(1) > td').text.strip()
        crossing = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(5) > div.ut-bio-stats_content > table > tbody > tr:nth-child(2) > td').text.strip()
        free_kick_accuracy = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(5) > div.ut-bio-stats_content > table > tbody > tr:nth-child(3) > td').text.strip()
        short_passing = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(5) > div.ut-bio-stats_content > table > tbody > tr:nth-child(4) > td').text.strip()
        long_passing = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(5) > div.ut-bio-stats_content > table > tbody > tr:nth-child(5) > td').text.strip()
        curve = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(5) > div.ut-bio-stats_content > table > tbody > tr:nth-child(6) > td').text.strip()

        phy = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(6) > div.ut-bio-stats_header > h6 > span.ut-bio-stats_title-value').text.strip()
        jumping = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(6) > div.ut-bio-stats_content > table > tbody > tr:nth-child(1) > td').text.strip()
        stamina = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(6) > div.ut-bio-stats_content > table > tbody > tr:nth-child(2) > td').text.strip()
        strength = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(6) > div.ut-bio-stats_content > table > tbody > tr:nth-child(3) > td').text.strip()
        aggression = driver.find_element_by_css_selector('body > div.container-outer > div > div.body-outer > div.ng-view.ng-scope > div:nth-child(1) > div.ut-bio.ut-underlay.ng-scope > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(6) > div.ut-bio-stats_content > table > tbody > tr:nth-child(4) > td').text.strip()

        line = (names_list[i] + ',' + full_name + ',' + overall + ',' + club + ',' + league + ',' + nation + ',' + age + ',' + height + ',' + weight + ',' + foot + ',' + pac + ','
                + acceleration + ',' + sprint_speed + ',' + dri + ',' + agility + ',' + balance + ',' + reactions + ',' + ball_control + ',' + dribbling + ',' + composure + ','
                + sho + ',' + positioning + ',' + finishing + ',' + shot_power + ',' + long_shots + ',' + volleys + ',' + penalties + ',' + defending + ',' + interceptions + ','
                + heading_accuracy + ',' + marking + ',' + standing_tackle + ',' + sliding_tackle + ',' + pas + ',' + vision + ',' + crossing + ',' + free_kick_accuracy + ','
                + short_passing + ',' + long_passing + ',' + curve + ',' + phy + ',' + jumping + ',' + stamina + ',' + strength + ',' + aggression + '\n')

        file.write(line)
        print i
    except:
        print '[EXCEPT]'
        continue

    finally:
        i += 1

file.close()
