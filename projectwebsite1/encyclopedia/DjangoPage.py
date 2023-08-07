from django.core.paginator import Paginator
from django.shortcuts import render

def page_list_view(request):
    # 获取所有的数据对象
    data_objects = YourModel.objects.all()

    # 每页显示的数量
    items_per_page = 10

    # 创建分页器对象
    paginator = Paginator(data_objects, items_per_page)

    # 获取当前页码
    page_number = request.GET.get('page')

    # 获取当前页的数据对象
    page_obj = paginator.get_page(page_number)

    # 获取排序参数
    sort_by = request.GET.get('sort_by')

    # 进行排序
    if sort_by:
        page_obj = data_objects.order_by(sort_by)

    context = {
        'page_obj': page_obj,
    }

    return render(request, 'your_template.html', context)
在这个示例中，我们首先从数据库中获取所有的数据对象，然后使用Paginator类创建一个分页器对象。然后，我们通过request.GET.get('page')来获取当前页码，并使用paginator.get_page()方法获取当前页的数据对象。

接下来，我们可以通过request.GET.get('sort_by')获取排序参数，并使用order_by()方法对数据进行排序。你可以根据自己的需求定义排序参数，并根据不同的参数进行不同的排序操作。

最后，我们将数据对象添加到上下文（context）中，并将上下文传递给渲染模板。在模板文件（your_template.html）中，你可以使用page_obj来访问当前页的数据对象，并在页面中展示它们。