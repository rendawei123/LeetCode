class Solution(object):
    def reverse(self, x):
        if type(x) == int:
            y = 0
            z = False

            if x < 0:
                z = True
                x = -x
            while True:
                if x == 0:
                    break
                else:
                    y = y * 10 + x % 10
                    x //= 10

            if -2147483648 <= y <= 2147483647:
                if z:
                    return -y
                else:
                    return y
            else:
                return 0

        else:
            return 0

if __name__ == '__main__':
    x = -123
    a = Solution()
    print(a.reverse(x))
