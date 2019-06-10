# -*- coding: UTF-8 -*-
def hs(x):

    dict = {'Capricorn': "今日运势： 摩羯大致良好",
            'Aquarius': "今日运势： 水瓶有好有坏",
            'Pisces': "今日运势：双鱼座整体状况有些反复，运势大体尚可 ",
            'Aries': "今日运势： 白羊座的整体星座运势较为平顺。",
            'Taurus': "今日运势： 运势表现大体尚好，金牛座在爱情方面的运势大致尚可",
            'Gemini': "今日运势： 双子座的整体运势大体普通",
            'Cancer': "今日运势：巨蟹座的整体运势会来一个大翻转 ",
            'Leo': "今日运势： 狮子座的整体运势有所回升",
            'Virgo': "今日运势： 处女座的整体运势大体顺利",
            'Libra': "今日运势： 天秤座的整体运势较为平顺，感情和工作都还不错",
            'Scorpio': "今日运势：天蝎座整体运势较为理想，在本月能够保持冷静谦和的心态",
            'Sagittarius': "今日运势： 射手座运势旺盛，心想事成"}

    horo_key = ['Capricorn', 'Aquarius', 'Pisces', 'Aries', 'Taurus',
                'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius']
    match = False

    for key in horo_key:

        if key == x:
            match = True
            return match, dict[key]

    return match, ' '
