import sys

if __name__ == '__main__':
    # 0b開頭為二進位
    print("0b1010: ", 0b1010)

    # 0o開頭為八進位
    print("0o12: ", 0o12)

    # 0x開頭為十六進位
    print("0x0A: ", 0x0A)

    # python會自動依照整數大小選擇記憶體長度
    print(f"數字10的記憶體大小為: {sys.getsizeof(10)} bytes")
    print(f'數字1234567890的記憶體大小為: {sys.getsizeof(1234567890)} bytes')

    # 想知道型態可以用type
    print(f"數字10的型態為: {type(10)}")
    print(f"數字0b1010的型態為: {type(0b1010)}")
    print(f"數字0o12的型態為: {type(0o12)}")

    # 建立整數
    print(f'int(\'10\'): {int("10")}')
    print(f'int(3.14): {int(3.14)}')
    print(f'int(True): {int(True)}')
    # 8進位
    print('oct(10):', oct(10))
    print('hex(10):', hex(10))

    # 指定基底
    print('int(\'10\', 2):', int('10', 2))
    print('int(\'10\', 8):', int('10', 8))
    print('int(\'10\', 16):', int('10', 16))

    # 浮點數
    print('type(3.14):', type(3.14))
    print('type(3.14e-10):', type(3.14e-10))
    print('float(\'1.414\'):', float('1.414'))
    # print('', int('3.14')) 這樣會錯, 要下面這樣
    # print('', int(float('3.14')))

    # 布林型態
    # False
    print('bool(0):', bool(0))
    print('bool(0.0):', bool(0.0))
    print('bool(0j):', bool(0j))
    print('bool(""):', bool(''))
    print('bool(()):', bool(()))  # Empty Tuple
    print('bool([]):', bool([]))  # Empty List
    print('bool({}):', bool({}))  # Empty Dict
    print('bool(\'None\'):', bool(None))

    print()

    # 其餘為True
    print('bool(1):', bool(1))
    print('bool(100):', bool(100))
    print('bool(asdfafdasf):', bool('asdfafdasf'))

    # 複數
    print('type(3+2j):', type(3 + 2j))

    # 字串
    print('type(\'abc123\')', type('abc123'))
    print('8進位數字 \\101 Code Point: ', '\101')
    print('16進位數字 \\x41 Code Point: ', '\x41')
    print('空字元 \\0', '\0')
    print('換行 \\n', '\n')
    print('a \\t b', 'a\tb')
    print()

    print('r開頭表示 raw string')
    print('r\\t:', r'\t')
    print('''1
    2
    3''')

    print('str(3.14):', str(3.14))
    print('str(3.14):', type(str(3.14)))
    print('用ord(\'你\')得知point code:', ord('你'))
    print('從point code轉換為文字 chr(20320): ', chr(20320))

    print()

    print('print 預設是空白分隔, 可指定sep參數變更, 如下')
    print('Hello', 'Victor', sep=', ')
    print('print 預設是字串結束後換行, 可指定end參數變更, 如下')
    print('Hello', 'Victor', sep=', ', end='')
    print(' !! <--已經是第二個print了')

    print()

    # 舊式字串格式化
    print('舊式字串格式化, 使用 string % data 或 string % (data1, data2)')
    print('你好! %s' % 'Victor')
    print('您的帳戶剩下%f元' % (100 / 3))
    print('您的帳戶剩下%.2f元' % (100 / 3))
    print('%d除以%d=%.2f元' % (100, 3, 100 / 3))
    print('%-5d除以%-5d=%.2f元' % (100, 3, 100 / 3))
    print('%5d除以%5d=%10.2f元' % (100, 3, 100 / 3))

    print()

    # 新式字串格式化
    print('新式字串格式化')
    print('{}除{}是{}'.format(10, 3, (10 / 3)))
    print('{1}除{0}是{2}'.format(3, 10, (10 / 3)))
    print('{n1}除{n2}是{n3}'.format(n1=10, n2=3, n3=10 / 3))
    print('同樣也可以在{}裡面指定格式與型態')
    print('{0:d}除{1:d}是{2:f}'.format(10, 3, 10 / 3))
    print('{0:5d}除{1:5d}是{2:.2f}'.format(10, 3, 10 / 3))
    #<向左靠齊 >向右靠齊 不指定預設向右靠齊
    print('{0:<5d}除{1:>5d}是{2:.2f}'.format(10, 3, 10 / 3))
    #位數不足欄位寬度時可補上指定位元在^前面指定
    print('{0:$^5d}除{1:5d}是{2:.2f}'.format(10, 3, 10 / 3))
    print()

    print('format 也可以取得list元素、使用key取map內的值、存取模組內的名稱')
    names = ['A', 'B', 'C']
    print('Names: {n[0]},{n[1]},{n[2]}'.format(n = names))
    data = {'A': 1,'B': 2,'C': 3}
    print('A: {n[A]}, B: {n[B]}, C: {n[C]}'.format(n = data))
    print('Platform: {pc.platform}'.format(pc = sys))
    #format
    print(format(3.14159, '.2f'))