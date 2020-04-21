from Scrapping_A import amazon
from Scrapping_E import eci
from Scrapping_M import msh
from Scrapping_total import total


url_list = [url1, url2, url3]

products_e = ['p1', 'p2', 'p3']
url_e = "url4"

products_msh = ['p4', 'p5', 'p6']
url_m = "url5"

path = "C:/path"

def main():
    df_a = a(url_list)
    df_e = e(products_eci, url_e )
    df_m = m(products_msh, url_m)
    total(path)




if __name__ == '__main__':
    main()