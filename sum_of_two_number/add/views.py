from django.shortcuts import render, redirect
from .models import Operation
# from django.http import HttpRequest
# Create your views here.

# all_result = []
# operation_no = 0

def operation_add(request):
    # global all_result, operation_no
    # result = 0
    alart=""
    if request.method == "POST":
        number_one = int(request.POST.get('number_one'))
        number_two = int(request.POST.get('number_two'))
        # operation_no += 1
        if number_one and number_two:
            result = number_one + number_two
            # all_result.append([operation_no, number_one, number_two, result])
            Operation.objects.create(number_one= number_one, number_two = number_two, result = result)
            alart="done"
        else:
            alart="fail"
    all_result = Operation.objects.all()
    context = {
        "all_result":all_result,
        "alart":alart
    }
    return render(request, 'add/index.html', context)

def delete_operstion(request, operation_id):
    # new_all_result=[]
    # global all_result

    # for i in all_result:
    #     if i[0] != operation_id:
    #         new_all_result.append(i)
    # all_result = new_all_result
    Operation.objects.filter(id = operation_id).delete()
    
    return redirect('operation_add')

def edit_operation(request, operation_id):
    # operation_list = []
    # global all_result
    # for i in all_result:
    #     if i[0] == operation_id:
    #         operation_list = i
    #         break
    operation = Operation.objects.get(id = operation_id)
    if request.method =="POST":
        # update_operation_no = int(request.POST.get("update_operation_no"))
        update_number_one = int(request.POST.get("update_number_one"))
        update_number_two = int(request.POST.get("update_number_two"))
        

        if update_number_one and update_number_two:
            operation.number_one = update_number_one
            operation.number_two = update_number_two
            operation.result = update_number_one + update_number_two
            operation.save()
        #     updated_result = update_number_one + update_number_two
            # for j in range(len(all_result)):
            #     if all_result[j][0] == operation_id:
            #         all_result[j] = [update_operation_no, update_number_one, update_number_two, updated_result ]
            #         break
            return redirect('operation_add')
    context={
        "operation_list":operation
    }
    return render(request, 'add/edit.html', context)