# O(log(n))
def func2(n):
    if n<=1:
        return
    else:
        print(n)
        func2(n/2)
# O(nlog(n))
def func4(n):
    for i in range(int(n)):
        print(i, end=" ")
    print()
    if n<=1:
        return
    func4(n/2)
if __name__=="__main__":
    func2(10)
    func4(10)