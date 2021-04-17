# 13. [罗马数字转整数](https://leetcode-cn.com/problems/roman-to-integer)

罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
```
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

 

示例 1:

输入: "III"
输出: 3
示例 2:

输入: "IV"
输出: 4
示例 3:

输入: "IX"
输出: 9
示例 4:

输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.
示例 5:

输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
```

提示：

题目所给测试用例皆符合罗马数字书写规则，不会出现跨位等情况。
IC 和 IM 这样的例子并不符合题目要求，49 应该写作 XLIX，999 应该写作 CMXCIX 。
关于罗马数字的详尽书写规则，可以参考 [罗马数字 - Mathematics](https://b2b.partcommunity.com/community/knowledge/zh_CN/detail/10753/%E7%BD%97%E9%A9%AC%E6%95%B0%E5%AD%97#knowledge_article) 。
通过次数268,248提交次数431,981
## 个人解析

这种类似于写一个简单的罗马数字解析器，哈哈，主要就是找到I和X,V,C,M在左边和右边的关系
这里给出一个c++版本,只是单纯的用了一下string而已哈哈
```
class Solution {

public:
	int romanToInt(string s) {
		int I = 0,V=0,X=0,L=0,C=0,D=0,M=0,other=0;
		int sum = 0;
		for (int i = 0; i < s.size(); i++)//调用size方法获得长度，为了遍历
		{
			//下面开始细数各种可能，例如III=3
			//创建一个I的状态，并且这个是个位数的状态，之前和之后的字母会影响，例如VI=6  IV=4
			switch (s[i])
			{//判断是否I的数目为1，如果为1的话可以去判断是否特殊情况
			case 'I':
				if (s[i + 1] == 'V')
				{
					sum += 4;
					V--;
				}
				else if (s[i + 1] == 'X')
				{
					sum += 9;
					X--;
				}
				else
					I++;
				break;
			case 'V':
				V++;
				break;
			case 'X':
				if (s[i + 1] == 'L')
				{
					sum += 40;
					L--;
				}
				else if (s[i + 1] == 'C')
				{
					sum += 90;
					C--;
				}
				else
					X++;
				break;
			case 'L':
				L++;
				break;
			case 'C':
				if (s[i + 1] == 'D')
				{
					sum += 400;
					D--;
				}
				else if (s[i + 1] == 'M')
				{
					sum += 900;
					M--;
				}
				else
					C++;
				break;
			case 'D':
				D++;
				break;
			case 'M':
				M++;
				break;
			default:
				break;
			}
			
		}
		sum += I+V*5+X*10+L*50+C*100+D*500+M*1000;
		return sum;
	}
};
```
最主要是要知道最终的结果是怎么组成的，其实是把罗马字母翻译成数字的意思，这样比实际上去算会快很多，而不是像愣头青一样一个个去分析  
