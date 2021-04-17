# 14. 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:
```
输入: ["flower","flow","flight"]
输出: "fl"
```
示例 2:
```
输入: ["dog","racecar","car"]
输出: ""
```
解释: 输入不存在公共前缀。
说明:
```
所有输入只包含小写字母 a-z 。
```
通过次数380,204提交次数978,549
## 个人解析
像这种简单题，一般都会有一个比较直观的思路，即两个for循环去比较
这里给出一个cpp版本
### c++
```
class Solution {
public:
	//创建一个向量存储容器 int
//如果想要比较n个，就用容器装着所有的字符串，然后遍历每一个字符串
	//这里代表函数参数为一个容器vector，是string类型的。
	//这里用的是引用，闫大顺经常说的那个，取地址过来的
	string longestCommonPrefix(vector<string>& strs) {
		//拿到之后，按最简单的方法来，遍历vector里的所有字符串
		//遍历直接取索引即可,vector长度可以用size方法得到，顺便说一下，vector也是一个对象，size是他的方法，返回长度
		//由于这个跟木桶效应很像，所以先取最短的那个字符串

		//另外，题目要求判断是否为空，那就这样
		if (strs.size() == 0)
		{
			return "";
		}


		string temp = strs[0];
		string result="";
		//判断是否相同的布尔值
		bool whether;
		

		for (int i = 1; i < strs.size(); i++)
		{
			if (temp.size() > strs[i].size())
			{
				temp = strs[i];
			}
		}
		//temp储存的是最小长度的字符串
		//现在取到每一个字符串
	
		int i = 0;
		for (; i < temp.size(); i++)
		{
			
			for (int j=0; j < strs.size(); j++)
			{
				//现在比较即可,注意的是，需要全部的字符串的对应字符相同，才能算是正确
				if (temp[i] == strs[j][i])
				{
					whether = true;
				}
				//如果不对直接break
				else
				{
					whether = false;
					break;
				}
			}
			if (whether)
			{
				result += temp[i];
			}
            			else
			{
				if (i == 0)
					return "";
			}

		}
		return result;
	}
};

```
![img](img/cpp.png)  
话说这也是很一般的方法，就是直观得出的，并没有任何的trick
### python
若是用python来做，那么应该是这样的，思路也非常简单，就是获取最小长度的字符串，再每一个都遍历确认。跟上面的思路一样
```
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str

        """
        #首字母
        if (not strs):
            return ""
        rleng=0
        minstr=strs[0]

        for str in strs:
           if(len(str)<len(minstr)):
               minstr=str

        for chari,singlechar in enumerate(minstr):
            flag = 0
            for str in strs:

                if(str!=minstr and str[chari]!=singlechar):
                    return minstr[:rleng]
                else:
                    flag=1
            if (flag):
                rleng+=1
        return  minstr[:rleng]
```
速度还可以，但是内存怎么用的这么多..  
![img](img/cpp.png)  

那么还可以改进，就是直接拿这个最小长度的字符串去比较
```
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str

        """
        #首字母
        if (not strs ):
            return ""
        minstr=strs[0]
        if (not minstr):
            return ""
        for str in strs:
           if(len(str)<len(minstr)):
               minstr=str
        flag = 0
        rleng=len(minstr)
        while(flag!=1):

            for str in strs:
                if minstr[:rleng] == str[:rleng]:
                    print(minstr[:rleng] ,str[:rleng])
                    flag=1
                else:
                    flag=0
                    break
            rleng-=1
        if (flag):
            return minstr[:rleng+1]
        else:
            return ''
```
![img](img/py2.png)  
妈的并无差别..