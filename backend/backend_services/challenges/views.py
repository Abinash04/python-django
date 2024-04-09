from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from backend_services.dynamodb import DynamoDBTable
from backend_services.dynamodb import dynamodb_client, put_item

# Create your views here.

def calculate():
    x = 2
    y = 4
    return x
def say_hello(request):
    x = calculate()
    # return HttpResponse('Hello World')
    return render(request, 'hello.html', {"name": "Piku"})

def get_products(request):
    table_name = 'MyDynamoDBTable'
    dynamodb_table = DynamoDBTable(table_name, dynamodb_client=dynamodb_client)

    # Create the DynamoDB table
    dynamodb_table.create_table()

    # Put an item into the DynamoDB table
    item = {'id': {'S': '1'}, 'name': {'S': 'John'}}
    response = put_item(dynamodb_client, table_name, item)
    return JsonResponse({'message':response})
