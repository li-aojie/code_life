from code.eat_v2 import *

content = """
#接龙
01.16

1. 郎国竣 中饭  6号楼 不辣
2. 马菲菲 中饭 晚饭 5号楼 辣
3. 朱丽香 中饭 晚饭5号楼 辣
4. 赵丽 中饭 6号楼 不辣
5. 胡凤娥 中饭   6号楼  辣
6. 申正荣 中饭 晚饭 6号楼 不辣
7. 程小利  中饭  6号楼   辣
8. 张强 中饭 晚饭  5号楼  辣
9. 郭惠惠 中饭 6号楼  辣
10. 黄成铖 中饭  6号楼 辣
11. 周明明 中饭 晚饭 5号楼 不辣
12. 鲍芳华 中饭 6号楼 不辣
13. 刘秋香   中饭  晚饭  6号楼  不辣
14. 车明月 中饭 晚饭 5号楼 不辣
15. 李凯迪 中饭 一楼 辣
16. 高小静 中饭 1楼 不辣
17. 杜嗣瑛  中饭 晚饭 6号楼 辣
18. 李倩倩 中饭 6号楼 辣
19. 朱晓红  中饭  晚饭  6号楼  辣
20. 朱蓥 中饭  6号楼 不辣
21. 彭细娥 中饭 6号楼 辣
22. 高瑾 中饭 一楼 辣
23. 韦加幸 中饭 晚饭 5号楼 辣
24. 魏仕川  中饭 晚饭 5号楼 辣
25. 张庭丽 中饭 5号楼 辣
26. 杜秋霞 中饭 6号楼 辣
27. 周梅 中饭 晚饭 1楼 辣
28. 陈克让 中饭 晚饭 5号楼 不辣
29. 熊小倩 中饭 5号楼 辣
30. 胡宇豪 中饭 6号楼 不辣
31. 商红成 中饭 6号楼 不辣
32. 郑海亮 中饭 6号楼 辣
33. 殷艳艳 中饭 晚饭 5号楼 不辣
34. 黄晶 中饭 晚饭 5号楼 辣
35. 王瑞娜 中饭 晚饭 6号楼 辣
36. 陈怡吉 中饭 晚饭 5号楼 辣
37. 胡建文  中饭 晚饭 5号楼 不辣
38. 任淞泽 中饭 晚饭 5号楼 辣
39. 方滢 中饭 晚饭 5号楼 辣
40. 李秀琦 中饭 晚饭 5号楼 不辣
41. 陈小华  中饭   晚饭   5号楼  辣
42. 汪俏  中饭 晚饭 5号楼 辣
43. 任胜杰 中饭 晚饭 5号楼
44. 左芳芳 中饭 晚饭 5号楼 辣
45. 鲁浩天 中饭 6号楼 不辣
46. 刘群 中饭  晚饭 5号楼  辣
47. 汪丝雨 中饭 6号楼 辣
48. 李超群 中饭 6号楼 辣
49. 符智祥 中饭 6号楼 辣
50. 刘巧玲 中饭 1楼 辣
51. 曹欣欣 中饭 6号楼 不辣
52. 尚瑞沙 中饭 6号楼 辣
53. 张腾腾 中饭 6号楼 辣
54. 王小银 中饭 一楼 不辣
55. 兰建霞 中饭 晚饭 5号楼 辣
56. 樊英英 中饭 晚饭5号楼 辣
57. 邓永恒 中饭  晚饭 6号楼 辣
58. 韩晓刚 中饭 6号楼 辣
59. 彭园园 中饭  6号楼 辣
60. 王兵兵 中饭 5号楼 辣
61. 谭祥梅 中饭 6号楼 辣
62. 林磊 中饭 晚饭 FM1-5号楼 辣
63. 尹江峰 中饭 1楼 不辣
64. 卢艳青 中饭 6号楼 辣
65. 王娇   中饭  5号楼 辣
66. 唐紧 中饭 晚饭 6号楼 辣
67. 张宇然 中饭 一楼 辣








"""



eat_date, result = tidy_data(content)
res = sort_data(result)
gen_excel(eat_date, res)