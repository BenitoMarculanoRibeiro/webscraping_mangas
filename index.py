#import pymysql
import requests


#con = pymysql.connect(host='remotemysql.com', user='aEe2LdBimG', password='SvfgdVTUw5',database='aEe2LdBimG', cursorclass=pymysql.cursors.DictCursor)
'''
HEADERS = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
           'Accept-Language': 'pt-br, pt;q=0.5'})
'''
'''while(True):
    pagina = 1
    status = True
    cont = 0'''
    #while(status):
'''url = 'https://mangayabu.top/ler/omniscient-readers-viewpoint-capitulo-03-my200710/'
pages = requests.get(url, headers=HEADERS)
print(pages.text)'''
            #print(pages.headers)
'''if(None != pages):
                vagas = []
                for page in pages:
                    titulo = page['tt']
                    link = f'https://www.trabalhabrasil.com.br/{page["u"]}'
                    cidade = page['uf']
                    descricao = page['d']
                    vagas.append((str(titulo), str(link), str(
                        cidade), str(descricao), str(link)))
                if len(vagas) > 0:
                    with con.cursor() as c:
                        sql = "INSERT INTO `vagas` (`titulo`, `link`, `cidade`, `descricao`) SELECT %s, %s, %s, %s WHERE NOT EXISTS(SELECT 1 FROM `vagas` WHERE `link` = %s)"
                        c.executemany(sql, vagas)
                        con.commit()
                        print(c.rowcount, "record(s) inserted.")
                cont += 1
                pagina += 1
                print("Pagina: " + str(pagina))'''

from lxml import html
import requests
HEADERS = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
           'Accept-Language': 'pt-br, pt;q=0.5'})
page = requests.get('https://mangayabu.top/ler/omniscient-readers-viewpoint-capitulo-03-my200710/', headers=HEADERS)
tree = html.fromstring(page.content)
print(tree)
trs = tree.xpath('//img[contains(@alt,"Página")]')
print(trs)
for tr in trs:
    #print(tr.get('href'))
    print(tr.attrib.get('id'))
    

from lxml import html
import requests
session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
           'Accept-Language': 'pt-br, pt;q=1'})

#session.get('https://httpbin.org/headers')
page = requests.get('https://mangayabu.top/ler/omniscient-readers-viewpoint-capitulo-03-my200710/', headers=HEADERS)
tree = html.fromstring(page.content)
#print(page.json())
currencies = [curr for curr in tree.xpath('//img[contains(@alt,"Página")]')]
print(currencies)