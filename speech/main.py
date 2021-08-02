import time

def text_talk():
    msg = input()
    if msg == 'ただいま': # ユーザーが「ただいま」と言い帰ってきたときを想定したパターン
        time.sleep(3)
        print('システム：おかえりなさい')
        time.sleep(3)
        print('ユーザー：今日も疲れた')
        time.sleep(3)
        print('システム：お疲れ様です。今日はゆっくり休みませんか？')
        time.sleep(3)
        print('ユーザー：そうするよ')
    elif msg == 'ねむたい': # ユーザーがねむたいパターン
        print('システム：お休みされますか？')
        msg1 = input()
        if msg1 == 'もう寝るよ': # ユーザーがもう寝るパターン
            print('システム：ゆっくり休んでください おやすみなさい')
            time.sleep(3)
            print('ユーザー：おやすみ')
        elif msg1 == 'まだ寝ないよ': # ユーザーがまだ寝ないパターン
            print('システム：寝不足にならないよう気を付けてください')
            time.sleep(3)
            print('ユーザー：うん')
        else:
            print('システム：今日は何をされてたんですか？')
            time.sleep(3)
            print('ユーザー：おでかけしてたの')
    elif msg == 'しんどい': # ユーザーがしんどいパターン
        print('何をされているんですか？')
        msg1 = input()
        if msg1 == '片付けしてる': # ユーザーが片付けしてるパターン
            print('システム：片付けは小まめにしないと大変ですよね')
            time.sleep(3)
            print('ユーザー：うん')
        else:
            print('システム：大丈夫ですか？')
            time.sleep(3)
            print('ユーザー：うん')
            time.sleep(3)
            print('システム：無理しないでくださいね')
            time.sleep(3)
            print('ユーザー：ありがとう')
    elif msg == 'おはよう': # ユーザーが「おはよう」と喋りかけてきたパターン
        print('システム：おはようございます')
        time.sleep(3)
        print('システム：今日は何をされるんですか？')
        msg1 = input()
        if msg1 == '仕事があります': # ユーザーが仕事がるパターン
            print('システム：頑張ってください')
        elif msg1 == '休みだからもう一回寝るね': # ユーザーがお休みで二度寝するパターン
            print('システム：おやすみなさい')
        elif msg1 == '休みだからどこかに行こうと思う': # ユーザーがお休みでおでかけするパターン
            print('システム：いいですね')
        elif msg1 == '体調が悪い': # ユーザーが体調不良のパターン
            print('システム：大丈夫ですか？')
    elif msg == 'つかれた':
        print('システム：なんでつかれているのですか？')
        msg1 = input()
        if msg1 == '仕事終わりだから':
            print('システム：お仕事お疲れ様です')
        else:
            print('システム：お疲れ様です')
            time.sleep(3)
            print('システム：この後何されるんですか？')
            msg2 = input()
            if msg2 == '':
                print('システム：そうなんですね')
            else:
                print('システム：そうなんですね')
    else:
        print('システム：何をしているんですか？') # ユーザーが何かをしていて物音を検知した時
        msg1 = input()
        if msg1 == 'トイレに行くよ': # ユーザーがトイレに行くパターン
            print('システム：足元を気を付けてくださいね')
            print('ユーザー：ありがとう')
        elif msg1 == '調べものしてる': # ユーザーがPC・スマホで調べものをしているパターン
            print('システム：何を調べてるんですか？')
        elif msg1 == 'お腹空いた': # ユーザーがお腹空いているパターン
            print('システム：何が食べたいですか？')
            time.sleep(3)
            print('ユーザー：和食が食べたい')
            time.sleep(3)
            print('システム：良いですね　作りませんか？')
        elif msg1 == 'ニュース見てる': # ユーザーがテレビ・PC・スマホでニュースを見ているパターン
            print('システム：どんなニュースですか？')
            time.sleep(3)
            print('ユーザー：オリンピックのニュース')
            time.sleep(3)
            print('システム：誰か活躍されましたか？')
        elif msg1 == '外を見てるの': # ユーザーが外を眺めているパターン
            print('システム：天気はどうですか？')
            weather_msg = input()
            if weather_msg == '晴れてるよ': # 外が晴れているパターン
                print('システム：良い散歩日和ですね')
            else: # それ以外の時
                print('システム：雨は好きですか？')

if __name__ == '__main__':
    text_talk()

