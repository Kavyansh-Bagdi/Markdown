# function for dot product
def dotProduct(vect_A, vect_B):

    product = 0

    # Loop for calculate dot product
    for i in range(0, 3):
        product = product + vect_A[i] * vect_B[i]

    return product

if __name__=='__main__':
    vect_A = [3, -5, 4]
    vect_B = [2, 6, 5]
    cross_P = []

# dotProduct function call
    print("Dot product:", end =" ")
    print(dotProduct(vect_A, vect_B))