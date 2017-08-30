from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, HttpResponse
from .forms import FilesForm
import xlrd

def page(request):
    form = FilesForm(request.POST or None, request.FILES)

    if request.method == "POST":
        if form.is_valid():
            if form.cleaned_data['file'].name[::-1][:4] == 'xslx' or form.cleaned_data['file'].name[::-1][:3] == 'slx':
                new_form = form.save()
                file_xl = xlrd.open_workbook(new_form.file.path)
                sheet = file_xl.sheet_by_index(0)

                coordsstring = ""
                colx = sheet.col_values(0)
                coly = sheet.col_values(1)

                for i in range(sheet.nrows):
                    if i != 0:
                        coordsstring += "," + str(colx[i])
                    else:
                        coordsstring += str(colx[i])

                coordsstring += "\n"

                for i in range(sheet.nrows):
                    if i != 0:
                        coordsstring += "," + str(coly[i])
                    else:
                        coordsstring += str(coly[i])
                return HttpResponse(coordsstring)
            return HttpResponse("Неверный формат файла! (" + form.cleaned_data['file'].name + ")")
        return HttpResponse('Неверная форма!')
    if request.method=='GET':
        return render(request, 'page/page.html', {'form': form})