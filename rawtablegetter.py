import bs4 as bs

pages = 0
with open('tempfiles/pages.txt') as f:
    pages = int(f.read())

sitepath = ''
with open('tempfiles/sitepath.txt') as f:
    sitepath = f.read()

with open("tempfiles/result/rawtable.txt", 'w') as make:
    make.write('')

for i in range(pages):
    site = ""
    with open('tempfiles/site/'+sitepath+'_start_'+str(i)+'.html', 'r', encoding='utf-8') as f:
        site = f.read()
    ps = bs.BeautifulSoup(site, 'html.parser')  # parsed site
    for i in range(100):
        rawwrite = '#tableend#'.join([str(s)
                                      for s in ps.select("table.tables"+str(i))])
        with open("tempfiles/result/rawtable.txt", 'a') as rawres:
            towrite = '#'
            for j in rawwrite.split('#tableend#'):
                pp = bs.BeautifulSoup(j, features="lxml")  # parsed piece
                towrite += '#lineend#'.join([str(s)
                                            for s in pp.select("tr")])
                towrite += '#tableend#'*(towrite[-1] != '#')
            rawres.write(towrite[1:])
