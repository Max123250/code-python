'''
时间限制： 3000MS
内存限制： 589824KB
题目描述：
(注.input()输入函数的括号中不允许添加任何信息)
编程实现：
六月一日是国际儿童节，小蓝的学校为迎接儿童节要在学校的一块正方形空地上使用不同颜色的花卉摆放图案。
为了摆放的更精准，图案更漂亮，小蓝把这块正方形空地同比例缩小将其画在纸上，并平分成100*100的方格，每个方格的坐标点为（1,1）...... (100,100)，如下图：
首先在指定坐标的方格内放置红色的花卉（每个方格放一盆），完成后，找出最多有多少盆红色花卉在同一条直线上。（同一直线包含同一列、同一行、同一对角线，红色花卉可以连续也可以不连续）
如：随机指定坐标(2,1)、(3,2)、(5,2)、(4,3)、(3,4)、(6,5)的方格内放置红色的花卉，其中最多的红色花卉在同一条直线上的坐标点为(2,1)、(3,2)、(4,3)、(6,5)，故最多有4盆红色的花卉在同一条直线上。
输入描述
输入n对正整数，每一对正整数之间以一个空格隔开，代表放置红色花卉的方格位置。每对正整数中的两个数字以英文逗号隔开
输出描述
输出最多有多少盆红色花卉在同一条直线上
样例输入
2,1 3,2 5,2 4,3 3,4 6,5
样例输出
4
提示
评分标准：
20分：能正确输出一组数据；
20分：能正确输出两组数据；
20分：能正确输出三组数据；
20分：能正确输出四组数据；
20分：能正确输出五组数据。
'''

pos = input()
pos = pos.split(" ")
for i in range(len(pos)):
    pos[i] = pos[i].split(",")
ground = [[0 for i in range(100)]for i in range(100)]
for l_pos in pos:
    y = int(l_pos[0])
    x = int(l_pos[1])
    ground[y][x] = 1
print(ground[0][0])

