#!/usr/bin/env python
# coding: utf-8

# In[1]:


def conflict(state, nextColumn):
    nextRow = rows = len(state)  
    """
        nextRow代表下一个Row
        state代表的是已经被确定的皇后
        rows作为存储的中间变量，对循环进行控制
    """
    for row in range(rows): 
        column = state[row]
        if abs(column - nextColumn) in (0, nextRow - row):
            """
                如果差值等于0，两个皇后在同一列， 则代表冲突， 返回True;
                如果列的差值等与行的差， 两个皇后在对角线上， 则代表冲突， 返回True;
            """
            return True
    return False


# In[17]:


def queens(num, state=()):
    """
    采用生成器的方式来产生每一个皇后的位置，并用递归来实现下一个皇后的位置。
    num: 皇后的数量
    state: 标记已经排好的每个皇后的位置
    """
    for pos in range(num): 
        """
        皇后的数量num，你要在哪一列放置皇后
        如果不冲突，则递归构造棋盘。
        """
        if not conflict(state, pos):  
            """
            判定是否冲突
            回溯法的体现，只有当这个棋盘中没有棋子触发重复，才会进行下一个棋子的判定和存储
            如果棋盘状态state已经等于num-1，即到达倒数第二行，而这时最后一行皇后又没冲突，直接yield，打出其位置(pos, )
            """
            if len(state) == num - 1:  # state=()
                yield (pos,)
            else:  # (0, )
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


# In[18]:


def prettyprint(solution): 
    """
    为了直观表现棋盘，用X表示每个皇后的位置
    """
    def line(pos, length=len(solution)): 
        return ' . ' * (pos) + ' x ' + ' . ' * (length - pos - 1)

    for pos in solution:
        print(line(pos))


# In[24]:


if __name__ == '__main__':
    solutions = queens(8)
    print("There are a total of %d solutions"% (index + 1))
    for index, solution in enumerate(solutions):
        print("solution:%d" % (index + 1), solution)
        prettyprint(solution)
        print('*' * 100)


# In[ ]:




