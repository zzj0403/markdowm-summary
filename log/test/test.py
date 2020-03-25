useragent = 'NEngine/1.0 (compatible; MSIE 6.0; Windows NT 5.1)'


def analysis_agent(useragent):
    if 'iOS' in useragent:
        agent = 'iOS'
    elif 'Windows' in useragent:
        agent = 'Windows'
    elif 'Android' in useragent:
        agent = 'Android'
    else:
        agent = 'other'

    return agent


res = analysis_agent(useragent)
print(res)
