import matplotlib.font_manager as fm 
from wordcloud import WordCloud

wc = WordCloud(font_path= "C:\Windows\Fonts/batang.ttc", background_color= "white", width = 1800, height = 1200)


text = ""
for i in range(29):
    with open("Talk_2021.8.24 13_10-"+str(i+1)+'.txt', 'r', encoding = "utf-8") as txt :
        
        lines = txt.readlines()
        for line in lines :
            
            if ': ' in line :
                text += ( line.split(': ')[1].replace('이모티콘', "")
                .replace("사진", "").replace('삭제된 메세지입니다', "").replace('ㅇ', '').replace("샵검색", '').replace('ㅋ', '').replace('\n','').replace('watch v','').replace('youtu','').replace('메세지입니다','').replace('youtube','').strip() )
for i in range(29,88):
    with open("Talk_2021.8.24 13_11-"+str(i+1)+'.txt', 'r', encoding = "utf-8") as txt :
        
        lines = txt.readlines()
        for line in lines[4:] :
            
            if ': ' in line :
                text += ( line.split(': ')[1].replace('이모티콘', "")
                .replace("사진", "").replace('삭제된 메세지입니다', "").replace('ㅇ', '').replace("샵검색", '').replace('ㅋ', '').replace('\n','').replace('watch v','').replace('youtu','').replace('메세지입니다','').replace('youtube','').strip() )



wc.generate(text) # 많이 나오는 텍스트를 서칭하고 정리하는 메서드
wc.to_file("house3.png")