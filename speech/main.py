import time

def text_talk():
    while True:
        msg = input()
        if msg == 'ただいま':  # ユーザーが「ただいま」と言い帰ってきたときを想定したパターン
            time.sleep(3)
            print('システム：おかえりなさい')
            time.sleep(3)
            print('システム：ちょっとお話ししませんか？')
            time.sleep(3)
            msg1 = input()
            if msg1 == 'つかれた':  # 仕事から疲れて帰ってきて「つかれた」と話しかけられた場合
                print('システム：お疲れ様です。今日は何されてたんですか？')
                msg2 = input()
                if msg2 == '仕事' or msg2 == 'しごと':  # 仕事 または しごと と発言した場合
                    print('システム：お仕事お疲れ様です。 お仕事楽しいですか？')
                    msg3 = input()
                    if msg3 == '普通' or 'ふつう':  # 普通 または ふつう と発言した場合
                        print('システム：そうなんですか')
                    elif msg3 == '楽しくない' or msg3 == 'たのしくない' or msg3 == '面白くない' or msg3 == 'おもしろくない' or msg3 == '辞めたい' or msg3 == 'やめたい':  # 楽しくない または たのしくない または 面白くない　または　おもしろくない　または　辞めたい　または やめたい と発言した場合
                        print('システム：何かあったんですか？')
                    else:  # それ以外を発言した場合
                        print('システム：どうかされましたか？')
                elif msg2 == '今日何かあった？':
                    print('このような出来事がありました')
            elif msg == 'ねむたい':  # ユーザーがねむたいパターン
                print('システム：お休みされますか？')
                msg1 = input()
                if msg1 == 'もう寝るよ':  # ユーザーがもう寝るパターン
                    print('システム：ゆっくり休んでください おやすみなさい')
                    time.sleep(3)
                elif msg1 == 'まだ寝ないよ':  # ユーザーがまだ寝ないパターン
                    print('システム：寝不足にならないよう気を付けてください')
                else:
                    print('システム：今日は何をされてたんですか？')
                    time.sleep(3)
                    msg2 = input()
                    if msg2 == '仕事' or msg2 == 'しごと' or msg2 == '仕事してた' or msg2 == 'しごとしてた':
                        print('お仕事お疲れ様です。')
            elif msg == 'しんどい':  # ユーザーがしんどいパターン
                print('何をされているんですか？')
                msg1 = input()
                if msg1 == '片付けしてる':  # ユーザーが片付けしてるパターン
                    print('システム：片付けは小まめにしないと大変ですよね')
            elif msg == 'ちょっとってどれくらいですか' or msg == 'ちょっとってどれくらい':
                print('システム：5分くらいです')
                msg1 = input()
                if msg1 == '分かった' or msg1 == 'わかった' or msg1 =='分かりました' or msg1 == 'わかりました' or msg1 == 'はい' or msg1 == 'うん':
                    print('システム：ありがとうございます。')
                elif msg1 == 'ちょっと待ってもらえる？' or msg1 == 'ちょっと待って' or msg1 == '待って':
                    print('システム：どれくらい待てばいいですか？')
                elif msg1 == '無理' or msg1 == 'むり' or msg1 == '今忙しい' or msg1 == '今急いでる':
                    print('システム：分かりました')
            else:
                print('システム：大丈夫ですか？')
                time.sleep(3)
                msg2 = input()
                if msg2 == 'うん':
                    print('システム：無理しないでくださいね')
                elif msg2 == 'はい':
                    print('システム：無理しないでくださいね')
                elif msg2 == '大丈夫':
                    print('システム：無理しないでくださいね')
                elif msg2 == 'だいじょうぶ':
                    print('システム：無理しないでくださいね')
                else:
                    print('システム：ゆっくりやすみませんか？')
                    msg3 = input()
                    if msg3 == 'うん':
                        print('システム：ゆっくり休んでくださいね')
                    elif msg3 == 'はい':
                        print('システム：ゆっくり休んでくださいね')
                    elif msg3 == 'そうする':
                        print('システム：ゆっくり休んでくださいね')
                    elif msg3 == 'そうするよ':
                        print('システム：ゆっくり休んでくださいね')
                    else:
                        print('システム：無理しないでくださいね')
        elif msg == 'おはよう':  # ユーザーが「おはよう」と喋りかけてきたパターン
            print('システム：おはようございます')
            time.sleep(3)
            print('システム：今日は何をされるんですか？')
            msg1 = input()
            if msg1 == '仕事があります' or msg1 == '仕事' or msg1 == 'しごと':  # ユーザーが仕事があるパターン
                print('システム：頑張ってください')
                print('今日帰ってきたら何したいですか？')
                msg2 = input()
                if msg2 == '寝たい' or msg2 == 'ねたい' or msg2 == 'ベットで寝たい' or msg2 == 'ベットでねたい' or msg2 == 'ゆっくり休みたい' or msg2 == 'ゆっくりやすみたい':
                    print('システム：疲れているんですね')
                    time.sleep(3)
                    print('システム：ちゃんと睡眠できていますか？')
                    msg3 = input()
                    if msg3 == 'うん' or msg3 == 'はい' or msg3 == 'できてる' or msg3 == '眠れてる' or msg3 == 'ねむれてる':
                        print('システム：なら良かったです')
                    else:
                        print('システム：今日はゆっくり休みましょう')
                elif msg2 == '何もしたくない' or msg2 == 'なにもしたくない' or msg2 == 'ぼーっとしたい' or msg2 == 'ボーっとしたい' or msg2 == '一人で居たい' or msg2 == '一人になりたい':
                    print('システム:何かありましたか？')
                elif msg2 == '':
                    print('')
                elif msg2 == '':
                    print('')
                else:
                    print('')
            elif msg1 == '休みだからもう一回寝るね':  # ユーザーがお休みで二度寝するパターン
                print('システム：おやすみなさい')
            elif msg1 == '休みだからどこかに行こうと思う':  # ユーザーがお休みでおでかけするパターン
                print('システム：いいですね')
            elif msg1 == '体調が悪い':  # ユーザーが体調不良のパターン
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
            print('システム：何をしているんですか？')  # ユーザーが何かをしていて物音を検知した時
            msg1 = input()
            if msg1 == 'トイレに行くよ':  # ユーザーがトイレに行くパターン
                print('システム：足元を気を付けてくださいね')
                print('ユーザー：ありがとう')
            elif msg1 == '調べものしてる':  # ユーザーがPC・スマホで調べものをしているパターン
                print('システム：何を調べてるんですか？')
            elif msg1 == 'お腹空いた':  # ユーザーがお腹空いているパターン
                print('システム：何が食べたいですか？')
                time.sleep(3)
                print('ユーザー：和食が食べたい')
                time.sleep(3)
                print('システム：良いですね　作りませんか？')
            elif msg1 == 'ニュース見てる' or msg1 == 'ニュースを見てます':  # ユーザーがテレビ・PC・スマホでニュースを見ているパターン
                print('システム：どんなニュースですか？')
                msg2 = input()
                if msg2 == 'オリンピック' or msg2 == 'おりんぴっく' or msg2 == '東京五輪':
                    print('システム：誰か活躍しましたか？')
                    msg3 = input()
                    print('システム：すごいですね')
                print('システム：誰か活躍されましたか？')
            elif msg1 == '外を見てるの':  # ユーザーが外を眺めているパターン
                print('システム：天気はどうですか？')
                weather_msg = input()
                if weather_msg == '晴れてるよ':  # 外が晴れているパターン
                    print('システム：良い散歩日和ですね')
                else:  # それ以外の時
                    print('システム：雨は好きですか？')
            elif msg1 == '仕事' or msg1 == 'しごと' or msg1 == '仕事してた' or msg1 == 'しごとしてた':
                print('システム：お疲れ様です。進み具合はどうですか？')
                msg2 = input()
                if msg2 == '普通' or msg2 == 'ふつう' or msg2 == '普通かな' or msg2 == 'ふつうかな' or msg2 == 'まぁまぁ' or msg2 == 'まぁまぁかな' or msg2 == 'ぼちぼち' or msg2 == 'ぼちぼちかな':
                    print('システム：そうなんですね　頑張ってください！')
                else:
                    print('')
            else:
                print('システム：どうしたんですか？')

if __name__ == '__main__':
    text_talk()
