consumption_file = open('用电量.txt', 'r')
consumption_lines = consumption_file.readlines()
fee_file = open('电费.txt', 'w')

for consumption_line in consumption_lines:
    consumption = int(consumption_line)
    if 0 <= consumption <= 50:
        fee = 0.53 * consumption
    elif 50 < consumption <= 100:
        fee = 1.11 * consumption - 29
    elif 100 < consumption:
        fee = 1.79 * consumption - 97
    else:
        print("结束计算")
        break
    fee_file.write(str(fee) + '\n')
    print("用电量为" + str(consumption) + "千瓦时，应付电费为：", round(fee, 2), "元，已写入文件。")
