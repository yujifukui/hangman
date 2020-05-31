correct_word = ["m","i","t","o"]
answer_space = ["_","_","_","_"]
num_huseikai = 0
hang_man = ["",
            "--------",
            "|      |",
            "|      |",
            "       o",
            "      / \ ",
            "       |",
            "      / /"]


print("".join(answer_space))


while num_huseikai < 7:
        print(hang_man[0:num_huseikai+1])
        p_kaitou = input("アルファベットを入力してください")

        if p_kaitou in correct_word:
                print("正解です")
                num = correct_word.index(p_kaitou)
                num = int(num)
                answer_space[num] = p_kaitou
                print("".join(answer_space))
        else:
                print("不正解です")
                num_huseikai += 1
                print("".join(answer_space))
