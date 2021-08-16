from jieba import lcut
from wordcloud import WordCloud as Wc

if __name__ == "__main__":
    while True:
        print("开始输入，输入 qpzm.?! 结束")
        words = ""
        while True:
            t = input()
            if t == "qpzm.?!":
                words = " ".join(lcut(words[:-1]))
                break
            else:
                words += t + "\n"

        wc = Wc(background_color="white", width=2000, height=2000,
                font_path="C:/Windows/Fonts/STZHONGS.TTF")  # 字体文件路径可能需要修改
        wc.generate(words)
        wc.to_file("cloud.webp")

        print("Finished.")
