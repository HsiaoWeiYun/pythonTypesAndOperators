import sys
import decimal

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
    # <向左靠齊 >向右靠齊 不指定預設向右靠齊
    print('{0:<5d}除{1:>5d}是{2:.2f}'.format(10, 3, 10 / 3))
    # 位數不足欄位寬度時可補上指定位元在^前面指定
    print('{0:$^5d}除{1:5d}是{2:.2f}'.format(10, 3, 10 / 3))
    print()

    print('format 也可以取得list元素、使用key取map內的值、存取模組內的名稱')
    names = ['A', 'B', 'C']
    print('Names: {n[0]},{n[1]},{n[2]}'.format(n=names))
    data = {'A': 1, 'B': 2, 'C': 3}
    print('A: {n[A]}, B: {n[B]}, C: {n[C]}'.format(n=data))
    print('Platform: {pc.platform}'.format(pc=sys))
    # format
    print(format(3.14159, '.2f'))

    print()

    print('python 3.6 之後開始支援 f-strings, {}內可支援運算式')

    print(f'1 + 1 = {1 + 1}')

    print(f'蕭的ascii: {ascii("蕭")}')

    del names
    name = 'Victor'
    print(f'Hello {"Guest" if name == None else name}')

    print('python 3.8 之後改良了f-strings 直接印出變數的部分, 方便log使用')
    print(f'{name=}')
    print(f'{name.upper()=}')
    print(f'{name.lower()=}')

    print(f'{name.encode("utf8")=}')
    print(f'{type(name.encode("utf8"))=}')

    print()
    print('----------群集型態----------')
    # list
    numbers = [1, 2, 3]
    print(f'{numbers=}')
    numbers.append(4)
    print(f'{numbers=}')
    numbers[0] = 100
    print(f'{numbers=}')
    numbers.remove(100)
    print(f'{numbers=}')
    print(f'{2 in numbers=}')
    del numbers[0]
    print(f'{2 in numbers=}')
    numbers.extend([10, 20, 30])
    print(f'{numbers=}')
    a = list('哈嚕你好')
    print(f'{a=}')
    # {}=set
    a = list({'哈', '嚕', '哈', '嚕'})
    print(f'{a=}')
    a = {1, 2, 3, 3, 4}
    a.add(5)
    print(f'{a=}')
    b = {6, 7}
    r = a.copy()
    r.update(b)
    print(f'{r=}')
    print(f'{a=}')
    print(f'{b=}')
    # 從其他可迭代的物件中建立set可用set()
    print('從其他可迭代的物件中建立set可用set()')
    a = set([1, 2, 3, 4, 4])
    print(f'{a=}')
    a = set((1, 2, 3, 4, 4))
    print(f'{a=}')
    # dict
    print('字典用來儲存兩兩對應的鍵與值')
    a = {'a': 1, 'b': 2, 'c': 3}
    print(f'{a=}')
    print(f'{a.get("a")=}')
    print(f'{a.get("d")=}')
    print(f'{a.get("d", 4)=}')
    print('字典可以利用[]存取')
    print(f'{a["b"]=}')
    a["b"] = 100
    print(f'{a["b"]=}')
    print(f'測試key是否存在: {"c" in a = }')
    print(f'{a.items()=}')
    print(f'{a.keys()=}')
    print(f'{a.values()=}')
    print()

    print('可以使用dict建立字典')
    print(f'{dict(i=1,j=2)=}')
    print(f'list轉dict: {dict([("i",1),("j",2)])=}')
    print(f'key來源為list, 值統一, 建立dict: {dict.fromkeys(["i","j"], 100)=}')

    print()
    print('''
    tuple是有序結構, 可以使用[]取得元素也能使用in查詢算是否存在,
    不過tuple一旦建立就無法更動, 有時候想回傳一組相關的資料但又不想定義一個型態時好用,
    或者希望某method不要修改傳入的資料時好用, 另外tuple所佔記憶體較小.
    ''')

    test = (10, 20)
    print(f'{test=}')
    # 會出錯
    # test[0]=100
    print(f'結尾是逗號也是建立tuple的方法之一 {10,20,30,=}')
    print(f'或者採用括弧的方式,但是注意需要逗號結尾: {type((10,))=}')
    print(f'否則: {type((10))=}')
    q, w, e = (10, 20, 30,)
    print(f'unpack tuple: {q=},{w=},{e=}')
    print()

    print('變數與運算子')
    print('''
    python屬於動態定型語言, 執行時期變數本身沒有型態資訊,
    建立變數不用宣告型態, 變數就是一個參考到值的一個名稱,
    指定運算只不過改變了參考而已, 舉例:
    ''')
    x = 10
    y = 20

    print(f'{id(x)=}, {id(y)=}')
    y = 100
    print(f'{id(x)=}, {id(y)=}')
    list1 = [1,2,3]
    list2 = [1,2,3]
    list3 = list1
    print(f'比較內容是否相等: {list1 == list2=}')
    print(f'比較是否同個參考: {list1 is list2=}')
    print(f'比較是否不同個參考: {list1 is not list2=}')
    print(f'有幾個變數參考至此物件: {sys.getrefcount(list1)=}')

    print()
    print('----- 運算 -----')
    print('處理小數')
    a = decimal.Decimal("3.333")
    b = decimal.Decimal("4.444")
    print(f'{a=}, {b=}, {a+b=}, {type(a+b)=}')

    print()
    print('字串相加')
    a = 'a'
    b = 'b'
    print(f'{a+b=}')
    print(f'{a*10=}')
    print('python不同型態間運算偏向不自動轉型, 所以字串與整數相加會報錯, 需要轉為相同型態才能運算')
    #c = '1' + 1 會報錯

    print('list相加會複製參考產生新的list')
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    #list3[0] 指向list1 ,list3[1] 指向list2, 所以當list1內容改變時list3內容也跟著變了
    #但若是用相加的方式雖然也是複製參考但情況有點不同, 若變更list1[0] 但list3[0]的參考仍是同一個並不會改變
    #我的理解是, 白話點, list1 + list2是參考到元素值, 而[list1, list2]這種方式是參考到list本身
    #list3 = list1 + list2
    list3 = [list1, list2]
    print(f'{id(list3[0])=}, {id(list1[0])=}')
    list1[0] = 'GG'
    print(f'{list3=}, {list1=}')
    print(f'{id(list3[0])=}, {id(list1[0])=}')

    print()
    print('海象運算子 :=')
    print('''海象運算式讓值的賦值可以傳遞到表達式中 下列寫法
    list = [1,2,3]
    count = len(list)
    if count > 2:
        print('list length > 2')
    可更精解為:
    list = [1,2,3]
    if(count:=len(list)) > 2:
        print('list length > 2')
        ''')
    print()
    print()
    list = [1,2,3]
    count = len(list)
    if count > 2:
        print('list length > 2')

    if(count:=len(list)) > 2:
        print('list length > 2')

    print()
    print('索引切片運算子, 只要具備索引特性基本上都能進行切片運算, 但為淺層複製,意思是只複製參考')
    print('索引切片運算格式: [start:end] or [start:end:step] step為間隔')
    list = [1,2,3,4,5,6,7,8]
    print(f'{list[0:2]=}')
    print(f'{list[3:8]=}')
    print(f'{list[-5:-1]=}')
    print(f'{list[5:]=}')
    print(f'{list[:5]=}')
    print(f'{list[:]=}')
    print(f'{list[0:5:2]=}')

    print()
    print('拆解運算子 * **')
    a,*b = list
    print(f'{a=}, {b=}')
    a, *b, c = list
    print(f'{a=}, {b=}, {c=}')

    a, *b = {'a': 1, 'b': 2, 'c': 3}
    print(f'用*運算子拆解dict 得到的是key {a=}, {b=}')