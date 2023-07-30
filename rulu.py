from pyknp import KNP

def rule_1(text): #ルール1
    knp = KNP()
    result = knp.parse(text)
    target = "<主節>"
    for clause in result.bnst_list():
        #print(clause.midasi + ":" + clause.spec())#specで「楽しかった たのしかった 楽しい」等が獲得可能になる
        #print(clause.repname)
        predicates = ["楽しい", "好きだ", "最高だ", "素晴らしい", "大好きだ", "便利だ", "満足だ", "面白い",
                  "良い", "良好だ", "優れる", "素敵だ", "嬉しい", "助かる", "完璧だ", "抜群だ",
                  "優秀だ", "最強だ", "絶妙だ", "良質だ", "有り難い", "十二分だ", "ユニークだ",
                  "文句無しだ", "打って付けだ", "パーフェクトだ"]
        #主節を探すコード
        if target in clause.spec():
            for i in predicates:
                if i in clause.spec():
                    return text
                else:
                    pass  #返り値はpass

def rule_2(text):#ルール2
    knp = KNP()
    if text == None:
        pass
    else:
        result = knp.parse(text)
        target = "<否定表現>"
        target_1 = "<準否定表現>"
        target_2 = "主節"
        if text == None:
            pass
        else:
            for bnst in result.bnst_list():
                if target_2 in bnst.fstring:
                    if target in bnst.fstring or target_1 in bnst.fstring:
                        pass
                    else:
                        return text

#def rule_3(text):
 #   knp = KNP()
  #  result = knp.parse(text)
   # target = 

def rule_4(text):#ルール4
    knp = KNP()
    if text == None:
        pass
    else:
        result = knp.parse(text)
        target = "<主節>"
        target_1 = "<格関係0:ガ:以外>"
        target_2 = "<格関係1:ガ:方>"
        if text == None:
            pass
        else:
            for bnst in result.bnst_list():
                if target in bnst.spec():
                    if target_1 in bnst.spec() or target_2 in bnst.spec():
                        pass
                    else:
                        return text

def rule_5(text):#ルール５
    knp = KNP()
    if text == None:
        pass
    else:
        result = knp.parse(text)
        target = "<SM-人>"
        target_1 = "には"
        target_2 = "にとって"
        target_3 = "<一人称>"
        if text == None:
            pass
        else:
            for bnst in result.bnst_list():
                if target in bnst.fstring:#ルール5(a)
                    if target_1 in text or target_2 in text:#(c)
                        return text 

        



#def rulr_3(text):

list_text = ["私は最高だ","運転するのが初めてな私にとって、楽しかった。","運転するのが初めてな私にとって、楽しくなかった。","免許取り立ての人が多いイメージ","運転が初めてな私でも、楽しく目的地まで到着できた。","日本の新しいスポーツが好きな彼女は友達と遊ぶ","最後までいくと1300段あるので無理だったからお守りがほしかったので売り場までは頑張っていきました。"]
#運転するのが初めてな私にとって、楽しい思い出ができた：だめ

for tasiyou in list_text:   
    print(tasiyou)
    result_rule1 = rule_1(tasiyou)
    result_rule2 = rule_2(result_rule1)
    #result_rule3 = rule_3(result_rule2)
    result_rule4 = rule_4(result_rule2)
    result_rule5 = rule_5(result_rule4)
    print("rule1:",result_rule1)
    print("rule2:",rule_2(result_rule1))
    print("rule4:",rule_4(result_rule2))
    print("rule5:",rule_5(result_rule4))

#違ったらリストに保存

#下記抽出コード

    knp = KNP()
    line = result_rule5
    if line == None:
        pass
    #"運転するのが初めてな私でも、楽しい思い出ができた。"
    #"免許取り立ての人が多いイメージ"
    #"運転が初めてな私でも、安心して目的地まで到着できた。"
    #"日本の新しいスポーツが好きな彼女は友達と遊ぶ"#二回
    #"階段がかなりあるので足腰が弱い人にはきついかもです."
    #最後までいくと1300段あるので無理だったからお守りがほしかったので売り場までは頑張っていきました。
    #そこまでで700段近くありました。次の日は筋肉痛で足がパンパンになったけどいい運動になったかな"
    else:
        result = knp.parse(line)
        #print(result.draw_tag_tree())

        target = "<SM-主体>"
        list_1 = []


        #for po in result.bnst_list():
            #print(po.midasi + ":" + po.fstring)
        for bnst in result.bnst_list():#このforはtargetを探すコード
            parent_x = bnst.parent
            child_rep = bnst.midasi #mrph_list()は形態素で取得、

            
            if parent_x == None:
                pass
            else:
                parent_1 = parent_x.fstring#fstringで意味マーカを取得
                if target in parent_1:#feture(parent_1)に人("<SM-主体>")が含まれてたら下記のコードを実行。人に係っている単語を探していくのが下記のコード
                    print(parent_x.midasi)
                    for i in result.bnst_list():#人に係っている単語を取得するfor
                        if i.midasi == parent_x.midasi:
                            print(child_rep,">>>",parent_x.midasi)
                            print(child_rep + parent_x.midasi)#childは「好きな」
                            list_1.append(child_rep)
                            new = list_1
                            for s in result.bnst_list():#二回目
                                parent_2 = s.parent
                                japan = ""
                                if parent_2 == None:
                                    pass
                                else:
                                    parent_2x = parent_2.midasi
                                    child_rep2 = s.midasi
                                    if parent_2x == child_rep:
                                        print(child_rep2,">>>",parent_2x)
                                        print(child_rep2 + parent_2x)
                                        text_3 = child_rep2 + parent_2x
                                        list_1.append(text_3)
                                        for d in result.bnst_list():
                                            parent_3 = d.parent
                                            if parent_3 == None:
                                                pass
                                            else:
                                                parent_3x = parent_3.midasi
                                                child_rep3 = d.midasi
                                                if parent_3x == child_rep2:
                                                    print(child_rep3,">>>",parent_3x)
                                                    print(japan + child_rep3 + parent_3x + parent_2x,"japan + chiled_rep3 + parent_3x + parent_2x")
                                                    text_1 = japan + child_rep3 + parent_3x + parent_2x
                                                    japan = ""
                                                    print(child_rep3 + parent_3x + parent_2x,"japan + chiled_rep3 + parent_3x + parent_2x")
                                                    text_2 = child_rep3 + parent_3x + parent_2x
                                                    if text_1 == text_2:
                                                    #一緒だったら追加しないコードを記載
                                                        list_1.append(text_1)
                                                    else:
                                                        list_1.append(text_2)
                                                        list_1.append(text_1)
                                                    

                                                    japan = child_rep3
                                                    
        
                                                                
        print(list_1)
