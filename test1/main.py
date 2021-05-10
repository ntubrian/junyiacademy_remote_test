# func A
def reverse_str(input):
    result = input[::-1]
    print(result)
    return result


# func B
def reverse_str_in_order(a_sentence):
    choped_sentence = a_sentence.split()
    resemble = " ".join([reverse_str(ele) for ele in choped_sentence])
    print(resemble)
    return(resemble)
    

if __name__ == "__main__":
    reverse_str_in_order(input())
