import os
print('linux需要wget')
while True:
    u = input('输入问题')
    s = os.name
    if s == 'posix':
        os.system('wget https://github.com/CZB666-wdnmd/chatczb/raw/main/hklmix_agadfaeaak4wqvy.png -O /tmp/out.png')
        print('回答在/tmp/out.png')
    else:
        os.system('start https://github.com/CZB666-wdnmd/chatczb/raw/main/hklmix_agadfaeaak4wqvy.png')
