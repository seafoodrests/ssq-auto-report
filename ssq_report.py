import smtplib
from email.mime.text import MIMEText
import datetime

title = "双色球策略验证报告"

content = f"""
双色球自动回测报告
时间：{datetime.datetime.now()}

【上期开奖结果】
自动抓取

【你的投注】
自动生成

【你老婆的投注】
自动生成

【命中情况】
自动计算

【年度统计】
自动累计

【下期推荐号码】
按既定冷热策略生成
"""

msg = MIMEText(content, "plain", "utf-8")
msg["Subject"] = title
msg["From"] = "双色球系统"
msg["To"] = "77630984@qq.com"

server = smtplib.SMTP_SSL("smtp.qq.com", 465)
server.login("你的QQ邮箱", "SMTP授权码")
server.send_message(msg)
server.quit()
