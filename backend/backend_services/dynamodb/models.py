import connection
import pandas as pd
import openpyxl

class DynamoDBTable:

    def __init__(self, table_name, dynamodb_client=None):
        self.table_name = table_name
        self.dynamodb_client = dynamodb_client

    def get_table(self):
        table = connection.get_dynamodb_resource().Table(self.table_name)
        return table

    def create_table(self):
        if self.dynamodb_client is None:
            self.dynamodb_client = connection.get_dynamodb_client()

        try:
            create_table_response = self.dynamodb_client.create_table(
                TableName=self.table_name,
                KeySchema = [
                    {
                        'AttributeName': 'EEID',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'Full_Name',
                        'KeyType': 'RANGE'
                    },
                    # {
                    #     'AttributeName': 'Job_Title',
                    #     'KeyType': 'HASH'
                    # },
                    # {
                    #     'AttributeName': 'Department',
                    #     'KeyType': 'HASH'
                    # },
                    # {
                    #     'AttributeName': 'Business_Unit',
                    #     'KeyType': 'HASH'
                    # },
                    # {
                    #     'AttributeName': 'Gender',
                    #     'KeyType': 'HASH'
                    # },
                    # {
                    #     'AttributeName': 'Age',
                    #     'KeyType': 'RANGE'
                    # },
                    # {
                    #     'AttributeName': 'Hire_Date',
                    #     'KeyType': 'HASH'
                    # },
                    # {
                    #     'AttributeName': 'Annual_Salary',
                    #     'KeyType': 'HASH'
                    # },
                    # {
                    #     'AttributeName': 'Bonus',
                    #     'KeyType': 'HASH'
                    # },
                    # {
                    #     'AttributeName': 'City',
                    #     'KeyType': 'HASH'
                    # },
                    # {
                    #     'AttributeName': 'Exit_Date',
                    #     'KeyType': 'HASH'
                    # }
                ],
                AttributeDefinitions = [
                    {
                        'AttributeName': 'EEID',
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': 'Full_Name',
                        'AttributeType': 'S'
                    },
                    # {
                    #     'AttributeName': 'Job_Title',
                    #     'AttributeType': 'S'
                    # },
                    # {
                    #     'AttributeName': 'Department',
                    #     'AttributeType': 'S'
                    # },
                    # {
                    #     'AttributeName': 'Business_Unit',
                    #     'AttributeType': 'S'
                    # },
                    # {
                    #     'AttributeName': 'Gender',
                    #     'AttributeType': 'S'
                    # },
                    # {
                    #     'AttributeName': 'Age',
                    #     'AttributeType': 'N'
                    # },
                    # {
                    #     'AttributeName': 'Hire_Date',
                    #     'AttributeType': 'S'
                    # },
                    # {
                    #     'AttributeName': 'Annual_Salary',
                    #     'AttributeType': 'S'
                    # },
                    # {
                    #     'AttributeName': 'Bonus',
                    #     'AttributeType': 'S'
                    # },
                    # {
                    #     'AttributeName': 'City',
                    #     'AttributeType': 'S'
                    # },
                    # {
                    #     'AttributeName': 'Exit_Date',
                    #     'AttributeType': 'S'
                    # }
                ],
                ProvisionedThroughput = {
                    'ReadCapacityUnits':5,
                    'WriteCapacityUnits':5
                }
            )

            self.dynamodb_client.get_waiter('table_exists').wait(TableName=self.table_name)
            # create_table_response.meta.client.get_waiter('table_exists').wait(TableName=self.table_name)
            print(f" create_table_response:{create_table_response}")

            print(f"Table {self.table_name} Created Successfully")
        
        except Exception as e:
            print("Create Table Error: ",e)

    
    def insert_data(self, data):
        # print(data)
        response = self.get_table().put_item(Item=data)
        return response

ddb = DynamoDBTable("employee-db")
ddb.create_table()


# read excel file
df = pd.read_excel("/Users/ab067240/Downloads/Employee_Sample_Data.xlsx")
column_headers_list = df.columns.to_list()
print(column_headers_list)
for index, row in df.iterrows():
    ddb.insert_data({
        'EEID': row['EEID'],
        'Full_Name': row['Full_Name']
    })
