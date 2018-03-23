#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import scrapy
import unicodedata

class FutheadSpider(scrapy.Spider):
    name = "futhead"
    start_urls = [
        'https://www.futhead.com/18/players/?group=all&level=all_nif&bin_platform=ps',
    ]
    
    def parsePlayerPage(self, response):

        infobox = response.css('li.media')
        info_tab = response.css('div.tab')[0].css('div.player-sidebar-item')
        stats = response.css('div.igs-group')
        playercard = response.css('div.player-detail-card')

        name = response.meta['name']
        full_name = infobox.css('div.fh-red a::text').extract_first()
        overall = int(playercard.css('div.playercard-rating::text').extract_first().strip())
        position = playercard.css('div.playercard-position::text').extract_first().strip()
        pac = int(playercard.css('div.playercard-attr1 span.chembot-value::text').extract_first().strip())
        sho = int(playercard.css('div.playercard-attr2 span.chembot-value::text').extract_first().strip())
        pas = int(playercard.css('div.playercard-attr3 span.chembot-value::text').extract_first().strip())
        dri = int(playercard.css('div.playercard-attr4 span.chembot-value::text').extract_first().strip())
        defend = int(playercard.css('div.playercard-attr5 span.chembot-value::text').extract_first().strip())
        phy = int(playercard.css('div.playercard-attr6 span.chembot-value::text').extract_first().strip())

        for attr in info_tab:
            if attr.css('div.col-xs-7::text').extract_first() is None:
                continue

            if attr.css('div.col-xs-7::text').extract_first().strip() == "Club":
                club = attr.css('div.player-sidebar-value a::text').extract_first()

            if attr.css('div.col-xs-7::text').extract_first().strip() == "League":
                league = attr.css('div.player-sidebar-value a::text').extract_first()

            if attr.css('div.col-xs-7::text').extract_first().strip() == "Nation":
                nation = attr.css('div.player-sidebar-value a::text').extract_first()

            if attr.css('div.col-xs-7::text').extract_first().strip() == "Strong Foot":
                strong_foot = attr.css('div.player-sidebar-value::text').extract_first()

            if attr.css('div.col-xs-7::text').extract_first().strip() == "Age":
                age = int(attr.css('div.player-sidebar-value::text').extract_first().split('-')[0].strip())
                dob = attr.css('div.player-sidebar-value::text').extract_first().split('-')[1].strip()

            if attr.css('div.col-xs-7::text').extract_first().strip() == "Height":
                height = int(attr.css('div.player-sidebar-value::text').extract_first().split('|')[0].strip().replace('cm',''))

        acceleration = int(stats[0].css('div.player-stat-row')[0].css('span.player-stat-value::text').extract_first())
        sprint_speed = int(stats[0].css('div.player-stat-row')[1].css('span.player-stat-value::text').extract_first())

        positioning = int(stats[1].css('div.player-stat-row')[0].css('span.player-stat-value::text').extract_first())
        finishing = int(stats[1].css('div.player-stat-row')[1].css('span.player-stat-value::text').extract_first())
        shot_power = int(stats[1].css('div.player-stat-row')[2].css('span.player-stat-value::text').extract_first())
        long_shots = int(stats[1].css('div.player-stat-row')[3].css('span.player-stat-value::text').extract_first())
        volleys = int(stats[1].css('div.player-stat-row')[4].css('span.player-stat-value::text').extract_first())
        penalties = int(stats[1].css('div.player-stat-row')[5].css('span.player-stat-value::text').extract_first())

        vision = int(stats[2].css('div.player-stat-row')[0].css('span.player-stat-value::text').extract_first())
        crossing = int(stats[2].css('div.player-stat-row')[1].css('span.player-stat-value::text').extract_first())
        free_kick = int(stats[2].css('div.player-stat-row')[2].css('span.player-stat-value::text').extract_first())
        short_passing = int(stats[2].css('div.player-stat-row')[3].css('span.player-stat-value::text').extract_first())
        long_passing = int(stats[2].css('div.player-stat-row')[4].css('span.player-stat-value::text').extract_first())
        curve = int(stats[2].css('div.player-stat-row')[5].css('span.player-stat-value::text').extract_first())

        agility = int(stats[3].css('div.player-stat-row')[0].css('span.player-stat-value::text').extract_first())
        balance = int(stats[3].css('div.player-stat-row')[1].css('span.player-stat-value::text').extract_first())
        reactions = int(stats[3].css('div.player-stat-row')[2].css('span.player-stat-value::text').extract_first())
        ball_control = int(stats[3].css('div.player-stat-row')[3].css('span.player-stat-value::text').extract_first())
        dribbling = int(stats[3].css('div.player-stat-row')[4].css('span.player-stat-value::text').extract_first())
        composure = int(stats[3].css('div.player-stat-row')[5].css('span.player-stat-value::text').extract_first())

        interceptions = int(stats[4].css('div.player-stat-row')[0].css('span.player-stat-value::text').extract_first())
        heading = int(stats[4].css('div.player-stat-row')[1].css('span.player-stat-value::text').extract_first())
        marking = int(stats[4].css('div.player-stat-row')[2].css('span.player-stat-value::text').extract_first())
        standing_tackle = int(stats[4].css('div.player-stat-row')[3].css('span.player-stat-value::text').extract_first())
        sliding_tackle = int(stats[4].css('div.player-stat-row')[4].css('span.player-stat-value::text').extract_first())

        jumping = int(stats[5].css('div.player-stat-row')[0].css('span.player-stat-value::text').extract_first())
        stamina = int(stats[5].css('div.player-stat-row')[1].css('span.player-stat-value::text').extract_first())
        strength = int(stats[5].css('div.player-stat-row')[2].css('span.player-stat-value::text').extract_first())
        aggression = int(stats[5].css('div.player-stat-row')[3].css('span.player-stat-value::text').extract_first())

        yield {
            'name': name,
            'full_name': unicodedata.normalize('NFKD', full_name).encode('ascii','ignore'),
            'overall': overall,
            'position': unicodedata.normalize('NFKD', position).encode('ascii', 'ignore'),
            'club': unicodedata.normalize('NFKD', club).encode('ascii','ignore'),
            'league': unicodedata.normalize('NFKD', league).encode('ascii','ignore'),
            'nation': unicodedata.normalize('NFKD', nation).encode('ascii','ignore'),
            'strong foot': strong_foot,
            'age': age,
            'dob': unicodedata.normalize('NFKD', dob).encode('ascii','ignore'),
            'height': height,
            'pac': pac,
            'acceleration': acceleration,
            'sprint speed': sprint_speed,
            'sho': sho,
            'positioning': positioning,
            'finishing': finishing,
            'shot power': shot_power,
            'long shots': long_shots,
            'volleys': volleys,
            'penalties': penalties,
            'pas': pas,
            'vision': vision,
            'crossing': crossing,
            'free kick': free_kick,
            'short passing': short_passing,
            'long passing': long_passing,
            'curve': curve,
            'dri': dri,
            'agility': agility,
            'balance': balance,
            'reactions': reactions,
            'ball control': ball_control,
            'dribbling': dribbling,
            'composure': composure,
            'def': defend,
            'interceptions': interceptions,
            'heading': heading,
            'marking': marking,
            'standing tackle': standing_tackle,
            'sliding tackle': sliding_tackle,
            'phy': phy,
            'jumping': jumping,
            'stamina': stamina,
            'strength': strength,
            'aggression': aggression,
        }
        
    def parse(self, response):
        list_items = response.css('li.player-group-item')
        for i in range(1, len(list_items)):
            item = list_items[i]
            player_name = item.css('a span.player-name::text').extract_first()
            link = item.css('a::attr(href)').extract_first()
            
            next_page = response.urljoin(link)
            request = scrapy.Request(next_page, callback=self.parsePlayerPage)
            request.meta['name'] = player_name
            yield request

        links = response.css('li.list-group-pagination a')
        next = links[len(links) - 1]
        if next.css('a::attr(href)').extract_first() is not None:
            next_url = response.urljoin(next.css('a::attr(href)').extract_first().strip())
            yield scrapy.Request(next_url, callback=self.parse)
