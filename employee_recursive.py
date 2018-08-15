import json

employee_list = '{"A1234":{"name":"john wick","title":"assasain","reports":["B1234","C1234"]},"B1234":{"name":"H ford","title":"badass","reports":[]},"C1234":{"name":"j trump","title":"fool","reports":["D1234"]},"D1234":{"name":"E walker","title":"littl guy","reports":[]}}'

employee_list = json.loads(employee_list)

def getemployee(id, indent=''):
    employee = employee_list[id]
    accumulated_indent = indent + '    '
    print(accumulated_indent + employee['name'] + ' - ' + employee['title'])
    for r in employee['reports']:
        accumulated_indent = accumulated_indent + indent
        getemployee(r, indent=accumulated_indent)

getemployee('A1234')
