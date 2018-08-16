#!/usr/bin/env python
#coding=utf-8

# 載入operator模組
import operator

# 加法運算
print("1 + 2 = operator.add(1,2) = ", operator.add(1,2))

# 連續型態資料相加（tuple或list）
print("[1,2,3] + [4,5,6] = operator.concat([1,2,3],[4,5,6]) = ", operator.concat([1,2,3],[4,5,6]))

# 容積運算
print("'a' in ['b', 'a', 'c'] = operator.contains(['b', 'a', 'c'],'a') = ", operator.contains(['b', 'a', 'c'],'a'))

# 除法運算 Python 3.0已經移除
#print("4 / 2 = operator.div(4,2) = ", operator.div(4,2))

# 除法運算
print("4 / 2 = operator.truediv(4,2) = ", operator.truediv(4,2))

# 除法運算
print("4 // 2 = operator.floordiv(4, 2) = ", operator.floordiv(4, 2))

# 二進位AND運算
print("0x0010 & 0x0011 = operator.and_(0x0010, 0x0011) = ", operator.and_(0x0010, 0x0011))

# 二進位XOR運算
print("0x0010 ^ 0x0011 = operator.xor(0x0010, 0x0011) = ", operator.xor(0x0010, 0x0011))

# 二進位NOT運算
print("~ 0x1000 = operator.invert(0x1000) = ", operator.invert(0x1000))

# 二進位OR運算
print("0x0010 | 0x0011 = operator.or_(0x0010, 0x0011) = ", operator.or_(0x0010, 0x0011))

# 次方運算
print("2 ** 16 = operator.pow(2, 16) = ", operator.pow(2, 16))

# 辨識運算
print("1 is 1 = operator.is_(1,1) = ", operator.is_(1,1))

# 辨識運算
print("1 is not 2 = operator.is_not(1,2) = ", operator.is_not(1,2))

# 以索引指派值
obj = [1,2,3]
operator.setitem(obj, 1, 4)
print("obj[1] = 4 = operator.setitem(obj, 1, 4) = ", obj)

# 以索引刪除值
operator.delitem(obj, 1)
print("del obj[1] = operator.delitem(obj, 1) = ", obj)

# 以索引取值
print("obj[1] = operator.getitem(obj,1) = ", operator.getitem(obj, 1))

# 左移運算
print("16 << 1 = operator.lshift(16, 1) = ", operator.lshift(16, 1))

# 乘法運算
print("2 * 8 = operator.mul(2, 8) = ", operator.mul(2, 8))

# 負數運算
print("-10 = operator.neg(10) = ", operator.neg(10))

# 否定運算
print("not 0 = operator.not_(0) = ",  operator.not_(0))

# 右移運算
print("16 >> 1 = operator.rshift(16, 1) = ", operator.rshift(16, 1))

# 連續型態值乘法運算（tuple或list） Python 3.0已經移除
#print("'-' * 10 = operator.repeat('-', 10) = ", operator.repeat('-', 10))

# 以切片指派值
seq = [1,2,3]
seq[2:3] = [4]
print("seq[2:3] = [4] = operator.setslice(seq,2,3,[4]) = ", seq)

# 以切片刪除值 Python 3.0已經移除
#operator.delslice(seq,1,2)
#print("del seq[1:2] = operator.delslice(seq,1,2) = ", seq)

# 取得切片值
#print("seq[1:2] = operator.getslice(seq,1,2) = ", operator.getslice(seq,1,2))

# 餘數運算
print("10 % 3 = operator.mod(10, 3) = ", operator.mod(10, 3))

# 減法運算
print("4 - 2 = operator.sub(4, 2) = ", operator.sub(4, 2))

# 真值運算（True或False）
print("1 == True, 0 == False = operator.truth(1), operator.truth(0) = ", operator.truth(1), operator.truth(0))

# 比較運算
print("1 < 11 = operator.lt(1,11) = ", operator.lt(1,11))

# 比較運算
print("1 <= 11 = operator.le(1,11) = ", operator.le(1,11))

# 等價運算
print("[1,2,3] == [1,2,3] = operator.eq([1,2,3],[1,2,3]) = ", operator.eq([1,2,3],[1,2,3]))

# 差異運算
print("[2,1,3] != [3,2,1] = operator.ne([2,1,3],[3,2,1]) = ", operator.ne([2,1,3],[3,2,1]))

# 比較運算
print("11 >= 1 = operator.ge(11,1) = ", operator.ge(11,1))

# 比較運算
print("11 > 1 = operator.gt(11,1) = ", operator.gt(11,1))
