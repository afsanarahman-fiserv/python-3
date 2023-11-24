# import boto3
# from botocore.exceptions import ClientError

def calculate():
    with open("../files/calculator-log.txt", "w") as f:
        while True:
            num_1 = input("Enter first number: ")
            if num_1 == "q":
                break
            num_2 = int(input("Enter second number: "))
            sum = int(num_1) + num_2
            expr = f"{num_1} + {num_2} = {sum}"
            print(expr)
            f.write(expr + '\n')

    # s3_client = boto3.client('s3')
    # file = '../files/calculator-log.txt'
    # bucket_name = 'sia-test-bucket'
    # key_path = '2023/March/Meeting Minutes/calculator-log.txt'

    # try:
    #     response = s3_client.upload_file(file, bucket_name, key_path)
    #     print("*** Uploaded to S3 ***")
    # except ClientError as e:
    #     print(e)

def ex4():
    calculate()

ex4()
