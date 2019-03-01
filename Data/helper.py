#coding:utf-8
import re
import os

# 日期 内容 打分 有用数 类型
regex_comment_block = '<div class=\'comment_block J_asyncCmt\'.*?</div></div></div>'

regex_date = '<span class=\'time\'>.*?</span>'
regex_text = '<div class=\'comment_txt\'>.*?</div>'
regex_score = '<span class=\'score\'>.*?</span>'
regex_useful = '<a class=\'useful.*?>'
regex_type = '<span class=\'type\'>.*?</span>'

pattern_comment_block = re.compile(regex_comment_block)

pattern_date = re.compile(regex_date)
pattern_text = re.compile(regex_text)
pattern_score = re.compile(regex_score)
pattern_useful = re.compile(regex_useful)
pattern_type = re.compile(regex_type)

my_path = os.getcwd()
raw_text = os.path.join(my_path, 'hotel.txt')

print(raw_text)
with open('hotel.txt', 'r', encoding='utf-8') as html:
    html_text = html.read().replace('\n', '')
    print(html_text)
    # exit()
    comment_blocks = pattern_comment_block.findall(html_text)
    # print(comment_blocks)
    for comment_block in comment_blocks:
        # print(comment_block)
        date = pattern_date.findall(comment_block)[0].replace('<span class=\'time\'>', '').replace('</span>', '').replace('发表于', '')
        text = pattern_text.findall(comment_block)[0].replace('<div class=\'comment_txt\'><div class=\'J_commentDetail\'>', '').replace('</div>', '')
        score = pattern_score.findall(comment_block)[0].replace('<span class=\'score\'><span class=\'n\'>', '').replace('</span>', '')
        useful = pattern_useful.findall(comment_block)[0].split('data-voted=')[1][1:2]
        type_ = pattern_type.findall(comment_block)[0].split('</i>')[1].replace('</span>', '')
        print('Info:\n{0}\n{1}\n{2}\n{3}\n{4}'.format(date, text, score, useful, type_))
        with open('result.txt', 'a', encoding='utf-8') as result:
            result.write('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(date, text, score, useful, type_))
