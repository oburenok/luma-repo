

def test_name1(request):
    testname = request.node.name
    assert testname == 'test_name1'