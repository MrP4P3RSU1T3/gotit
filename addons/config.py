#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 赞助者
sponsor = (
    ('zhwei', '0.01'),
    ('*伟颖', '0.10'),
    ('*健', '3.00'),
    ('*竞一', '1.00'),
    ('*昌昌', '2.00'),
    ('*德昊', '1.00'),
    ('张宇', '0.01'),
    ('杨林晓', '1.00'),
    ('王磊', '0.10'),
    ('王京凯', '0.01'),
    ('高道成', '1.00'),
    ('孟竑光', '0.50'),
    ('武德研', '5.00'),
    ('王士钰', '0.09'),
    ('袁羿霖', '0.10'),
    ('张凯', '1.00'),
    ('杨博', '1.00'),
    ('许建栋', '0.01'),
    ('刘传金', '1.00'),
    ('刘飞', '1.00'),
)

## 正方 说明/警告
zheng_alert = ""


# 配置参数
# ---------------------------
# 正方教务系统
# 教务系统url,注意不要忘记最后的"/"
zf_url = "http://210.44.176.133/"
# url中是否有随机字符串
random = True

# 成绩查询网址
score_url = "http://210.44.176.116/cjcx/zcjcx_list.php"

# 四六级成绩查询

# POST地址
cet_url = "http://www.chsi.com.cn/cet/query"

# 是否使用bae查询
baefetch = True

# 查询页缓存时间(秒)
index_cache = 1000

# 网站运行模式
debug_mode = False
