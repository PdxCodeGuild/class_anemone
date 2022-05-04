
"""در تمام دنیا"""
import sys
def case1(text):
    print(text)

def case2(text):
    print(text.encode("utf-8"))

def case3(text):
    sys.stdout.buffer.write(text.encode("utf-8"))

if __name__ == "__main__":
    text = "چرا کار نمیکنی؟"        

    for case in [case1, case2, case3]:
        try:
            print("Running {0}".format(case.__name__))
            case(text)
        except Exception as e:
            print(e)    

        print('-'*80)    