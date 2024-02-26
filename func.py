strr=''

class funcc:
    @staticmethod
    def work(stri):
        strr = ''
        count=1

        for i in stri:
            strr += i
            if count % 3 == dar:
                if count!=len(stri):
                    strr+='/'

            count+=1
        strrb=strr
        strr=''
        return strrb
    @staticmethod
    def az(stri):
        strr=stri
        for i in stri:
            if i=='0':
                i=''
                strr=stri.replace('0','',1)
                stri=strr
            else:
                break
        return strr
    @staticmethod
    def ad(a,b):
        """for i in a:
            if   :
                count+=
            if count==finded:"""
        return a
    @staticmethod
    def aad(a,b,c):
        p=''
        if b ==0:
            p=a[:c]+'.'+a[c:]
        return p




f='3542352.52'
finded = f.find('.')

f=f.replace('.','')
if len(f) % 3 == 0:
    dar = 0
elif len(f) % 3 == 1:
    dar = 1
elif len(f) % 3 == 2:
    dar = 2
f=funcc.aad(f,dar,finded)
f=funcc.az(f)
f=funcc.work(f)
f=funcc.ad(f,finded)
print(f)
