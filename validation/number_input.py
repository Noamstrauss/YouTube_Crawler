
def number_vali(question):
  while True:
    try:
       answer = int(input(question))
    except ValueError:
       print("Not an Number! Try again.")
       continue
    else:
       return answer


if __name__ == '__main__':
    number_vali("Please Enter A Number:")