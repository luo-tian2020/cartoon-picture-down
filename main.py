#https://www.opacg.com/bg/PC/acgurl.php, {"User-Agent": UserAgent().random}
#https://api.ixiaowai.cn/api/api.php
#https://api.dongmanxingkong.com/suijitupian/acg/1080p/index.php
# https://api.dongmanxingkong.com/suijitupian/acg/4k/index.php
#https://api.vvhan.com/api/acgimg
#https://img.xjh.me/random_img.php
from jiekou import jiekoupicture
print("注意：API接口必须是开放的，且能在国内访问，版权所有归洛天")
apiurl=input("请输入Api链接：")
jiekoupicture(apiurl)
print("已完成下载！")