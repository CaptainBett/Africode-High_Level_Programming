
import sys
max_recusion = sys.getrecursionlimit()
print(max_recusion)
def hello():
    print(hello)
    hello()
hello()


# def countdown(start):
#     """
#     countdown from a number
#     """
#     print(start)
#     if start < 10:
#         countdown(start+1)
# countdown(1)
