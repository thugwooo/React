text = ""

text = '' 
with open("게기스.txt", "r", encoding="utf-8") as f: 
    lines = f.readlines() 
    for line in lines: 
        if '] [' in line and len(line.split('] '))>2: 
            text += line.split('] ')[2].replace('ㅋ', '').replace('ㅠ', '').replace('ㅜ', '').replace('사진\n', '').replace( '이모티콘\n', '').replace('삭제된 메시지입니다', '')


from wordcloud import WordCloud

wc = WordCloud(font_path= "C:\Windows\Fonts/batang.ttc", background_color= "white", width = 1800, height = 1200)
wc.generate(text) # 많이 나오는 텍스트를 서칭하고 정리하는 메서드
wc.to_file("게기스.png")