# conding:utf-8
#日本語


#********************************************************
def mFileWrite_text(str_filename, str_html_text):
    strNL = '\n'
    str_html_val = '<html>' + strNL + \
                    '<body>' + strNL + \
                    str_html_text + strNL + \
                    '</body>' + strNL + \
                    '</html>'
                    
    print(str_html_val)
    f = open(str_filename, 'w')
    f.write(str_html_text)
    f.close()


#********************************************************
if __name__ == '__main__':
    str_file_name = '/home/pi/_py/index.html'
    str_val = 'text'
    #print(str_val)
    mFileWrite_text(str_file_name, str_val)
    