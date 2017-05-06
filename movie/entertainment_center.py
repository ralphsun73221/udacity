import media
import fresh_tomatoes

toy_story = media.Movie("玩具總動員", "這是一個玩具故事", "http://www.sabedoriaglobal.com.br/wp-content/uploads/2012/10/Toy-Story-wallpaper-11.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)
#toy_story.show_trailer()

avatar = media.Movie("阿凡達", "就是一個阿凡達的故事", "dk", "tt")

#print(avatar.storyline)

gits = media.Movie("攻殼機動隊", "什麼是人？", "http://www.gameapps.hk/images/201511/26/sd4.jpg", "https://www.youtube.com/watch?v=Fy0BxJgHgHo")
#print(GITS.storyline)
#GITS.show_trailer()

gotg = media.Movie("星際異攻隊", "《星際異攻隊》（英語：Guardians of the Galaxy，或稱Guardians of the Galaxy Vol. 1[4][5]）是一部於2014年上映的美國超級英雄電影，改編自漫威漫畫的同名作品。本片為漫威電影宇宙系列的第十部作品。由漫威影業製作，華特迪士尼影業負責發行。導演為詹姆士·昆恩，由妮可·帕爾曼撰寫劇本。美國於2014年8月1日上映。", "https://zh.wikipedia.org/wiki/File:Guardians_of_the_galaxy_ver2.jpg", "https://www.youtube.com/watch?v=HGS1ntWIhb8")
pacific_rim = media.Movie("環太平洋", "《環太平洋》（英語：Pacific Rim）是一部2013年美國科幻怪獸動作片。由吉勒摩·戴托羅執導，查理·杭南、菊地凜子、伊卓瑞斯·艾巴和朗·帕爾曼等人主演。劇本由特拉維斯·比徹姆基及吉勒摩·戴托羅設計。《環太平洋》是一部由傳奇影業公司製作，華納兄弟娛樂公司發行的電影", "https://en.wikipedia.org/wiki/File:Pacific_Rim_FilmPoster.jpeg", "https://www.youtube.com/watch?v=5guMumPFBag")

movies = [toy_story, avatar, gits, gotg, pacific_rim]
fresh_tomatoes.open_movies_page(movies)