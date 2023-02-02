import os
print('注：linux需要wget')
while True:
    u = input('输入问题(ctrl+c退出)')
    s = os.name
    if s == 'posix':
        os.system('wget https://github.com/CZB666-wdnmd/chatczb/raw/main/hklmix_agadfaeaak4wqvy.png -O /tmp/out.png')
        print('回答在/tmp/out.png')
    elif s == 'nt':
        os.system('start https://github.com/CZB666-wdnmd/chatczb/raw/main/hklmix_agadfaeaak4wqvy.png')
    else:
        print('不支持的系统')
        break
