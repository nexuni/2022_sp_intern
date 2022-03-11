import string

# please reference https://www.trust.org.tw/upload/1100002250002.pdf
# or code in C++ https://cynthiachuang.github.io/Check-Tax-ID-Number/

def check_taiwan_tax_id(tax_id):
    """
    Input
        - tax_id: str
    Output
        - boolean
    """
    weight = [1, 2, 1, 2, 1, 2, 4, 1]
    id_list = [int(a) for a in str(tax_id)]
    if len(weight) != len(id_list):
        return False
    else:
        product = list(map(lambda x,y: x*y ,weight,id_list))
        summation = sum(map(lambda x: x%10+ x//10, product))
        if summation%10==0:
            return True
        elif id_list[6] == 7 and (summation+1)%10 ==0:
            return True
        else:
            return False




# Test data
print(check_taiwan_tax_id("53619559"))
print(check_taiwan_tax_id("53619549"))
print(check_taiwan_tax_id("64387543"))
print(check_taiwan_tax_id("23328674"))
print(check_taiwan_tax_id("23328673"))
print(check_taiwan_tax_id("23673"))

