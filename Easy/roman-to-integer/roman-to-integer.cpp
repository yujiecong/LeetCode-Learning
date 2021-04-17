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