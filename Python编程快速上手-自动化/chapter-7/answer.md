1. `re.compile`
2. 使用原始字符串可以省去\
3. Match对象
4. mo.group()
5. 分组0代表整个匹配的字符串，分组1是(\d\d\d)匹配的，分组2是(\d\d\d-\d\d\d\d)匹配的
6. \( \) \.
7. 匹配的模式中是否有分组
8. 通道，其实就是或的关系
9. 非贪心匹配或者0或1次
10. +是1次或多次，*是0次或多次
11. {3}是指分组匹配3次，{3,5}是指分组匹配3到5次
12. \d——任意一个数字，\w——任意一个字母，\s——任意一个空格
13. 与上面相反
14. 第二个属性加上,re.I 或re.IGNORECASE
15. .匹配除了换行符之外的任意字符，传递re.DOTALL后可以匹配任意字符
16. .*  匹配所有字符     *?(不知道)
17. [0-9a-z]
18. 'X drummers, X pipers, five rings, X hens'
19. 可以写多行，可以写注释
20. numRegex = re.compile(r'(\d{1,3}\,)?(\d\d\d\,)*\d{1,3}')
21. nameRegex = re.compile(r'[A-Z]\w+ Nakamoto')
22. sentenceRegex = re.compile(r'Alice|Bob|Carol eats|pets|throws apples|cats|baseballs.', re.IGNORECASE)