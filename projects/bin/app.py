import web
import re
import os

urls = (
    '/', 'Index'
)

app = web.application(urls, globals())
render = web.template.render('templates/', base="layout")


class Index(object):

    def GET(self):
        return render.header()

    def POST(self):
        form = web.input(myfile={})

        filedir = os.path.dirname(__file__) + '/temp'
        if 'myfile' in form:
            filepath = form.myfile.filename.replace('\\', '/')
            filename = filepath.split('/')[-1]
            fout = open(filedir + '/' + filename, 'wb')
            fout.write(form.myfile.file.read())
            fout.close()

            # Read lines
            file = open("temp/" + filename, 'r')
            Lines = file.readlines()

            Customers = []
            count = 0
            for line in Lines:
                if count > 0:
                    arr = re.split("(\s+)", line.strip())
                    col_num = len(arr)
                    c_email = col_num - 3
                    c_phone=col_num-1
                    c_name = 2
                    name =""
                    while c_name < c_email :
                      name = name +" "+ arr[c_name]
                      c_name=c_name+1
                    Customers.append([arr[0], name, arr[c_email], arr[c_phone]])

                count = count + 1

        info = sorted(Customers, key=lambda x: x[1])

        return render.index(data=info)


if __name__ == "__main__":
    app.run()
