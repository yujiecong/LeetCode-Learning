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