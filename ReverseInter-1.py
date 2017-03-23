
class Solution(object):
    def reverse(self, x):
        strx = str(x)

        if x < -2147483648 or x > 2147483647:
            return 0
        elif strx[0] == '-':
            if int('-' + (strx[1:])[::-1]) >= -2147483648:
                return int('-' + (strx[1:])[::-1])
            else:
                return 0
        else:
            if int(strx[::-1]) <= 2147483647:
                return int(strx[::-1])
            else:
                return 0


if __name__ == '__main__':
    x = -123
    a = Solution()
    print(a.reverse(x))