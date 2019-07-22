def replaceSpace(s):
        # write code here
        if s==None:
            return False
        else:
            n=len(s)
            j=0
            for i in range(n):
                k=i+j
                if s[k] == ' ':
                    j=j+2
                    s =s[:k] + '%20' + s[k+1:]
                    print(s)


s='We Are Happy'
replaceSpace(s)